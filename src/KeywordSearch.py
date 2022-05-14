from utils import create_logger, timed, exception
from typing import List
from itertools import compress
import logging

logger = create_logger('keyword-search')
logger.setLevel(logging.DEBUG)
class KeywordSearch():

    class TrieNode:
        def __init__(self):
            self.child = {}
            self.is_end = False

    def __init__(self):
        self._root = self.TrieNode()
        logger.info(f"Use {self.__class__.__name__} for seaching task.")
    
    @timed(logger)
    @exception(logger)
    def fit(self, 
            words:List[str]):
        """
        Initial trie-tree with your keywords. Fit a list of words(string) to build trie-tree. 
        This will insert a list of TrieNode into self._root consequentlty. 

        :param words: Those queries users want to search in target documents.
        :type words: List[str]
        """
        
        for word in words:
            self._insert(word)
            
        logger.info(f"Building {self.__class__.__name__} successfully, within {len(words)} words.")
    
    @timed(logger)
    @exception(logger)
    def transform(self, 
                  docs:List[str], hits:int=1) -> List[str]:
        """Transform a initialize tree into search documents. The keywords which initial in fit() will be searched in each
        document until a keyword be found or end of the document.
        keys = ['ddt','ds']
        docs = ['ddtds','ddtdd', 'aa']
        => transform(docs, 2) = ['ddtds']

        Parameters
        ----------
        docs : List[str]
            Input documents, which users want to filter with the keywords.
        hits : int
            Minimum hit count, return docs need to hit keywords at least what times.

        Returns
        -------
        List[str]
            A list of documents which are hit the keywords at least once or {hits} times.

        Raises
        ------
        ValueError
            _description_
        """

        if len(self._root.child)<1:
            raise ValueError("Please fit your target word to build trie-tree befor transform your documents: \n"
                             "`from __ import TrieTreeSearcher` \n"
                             "`searcher = TrieTreeSearcher()` \n"
                             "`searcher.fit(__your data__)` \n")
        is_matches = []
        for doc in docs:
            is_matches.append(self._find(doc, hits))
        
        res = list(compress(docs, is_matches))

        if len(res) < 1:
            logger.warning(f"Document Not Found!")
        else:
            logger.info(f"Find {len(res)} documents.")

        logger.debug(f"res: "+ str(res)) 

        return res
        
    def _insert(self, word):

        node = self._root
        
        for char in word:
            if char not in node.child:
                node.child[char] = self.TrieNode()
            node = node.child[char]
        node.is_end = True

    def _find(self, doc, hits):
        
        node = self._root
        doc_hits = 0
        for char in doc:
            node = node.child.get(char)
            if not node and char in self._root.child:
                node = self._root.child.get(char)
            elif not node:
                node = self._root
            if node.is_end:
                doc_hits += 1
                if doc_hits >= hits:
                    logger.debug(f"docs hits: " + str(doc_hits) + ' hits: ' + str(hits))
                    self.hits = 0
                    return True    

class FullKeywordsSearch():

    class TrieNode:
        def __init__(self):
            self.child = {}
            self.is_end = False
            self.keyword = None

    def __init__(self):
        self._root = self.TrieNode()
        logger.info(f"Use {self.__class__.__name__} for seaching task.")
    
    @timed(logger)
    @exception(logger)
    def fit(self, 
            words:List[str]):
        """Initial trie-tree with your keywords. Fit a list of words(string) to build trie-tree. 
        This will insert a list of TrieNode into self._root consequentlty. 

        :param words: Those queries users want to search in target documents.
        :type words: List[str]
        """
        
        for word in words:
            self._insert(word)
            
        logger.info(f"Budding {self.__class__.__name__} successfully, within {len(words)} words.")
    
    @timed(logger)
    @exception(logger)
    def transform(self, 
                  docs:List[str]) -> List[str]:
        """
        Give a list of documents, return a list if elements hit keywords.
        keys = ['ddt','ds']
        docs = ['ddtds','ddtdd']
        => res = [['ddt','ds], ['ddt']]

        Parameters
        ----------
        docs : List[str]
            Input documents, which users want to filter with the keywords.

        Returns
        -------
        List[List]
            

        Raises
        ------
        ValueError
            [description]
        """

        if len(self._root.child)<1:
            raise ValueError("Please fit your target word to build trie-tree befor transform your documents: \n"
                             "`from __ import TrieTreeSearcher` \n"
                             "`searcher = TrieTreeSearcher()` \n"
                             "`searcher.fit(__your data__)` \n")
        hit_list = []
        for doc in docs:
            hit_list.append(self._find(doc))

        return hit_list
        
    def _insert(self, word):

        node = self._root
        
        for char in word:
            if char not in node.child:
                node.child[char] = self.TrieNode()
            node = node.child[char]
        node.is_end = True
        node.keyword = word

    def _find(self, doc):
        
        node = self._root
        
        hits = []
        for char in doc:
            node = node.child.get(char)
            if not node and char in self._root.child:
                node = self._root.child.get(char)
            elif not node:
                node = self._root
            if node.is_end:
                hits.append(node.keyword)

        return hits