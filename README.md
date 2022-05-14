# Efficient Keyword Search

In order to find the keywords in a large number of documents, we introduce two search algorithms based on Tire-Tree ( also known as Prefix Tree) to reduce the search time complexity from $O(n)$ to $O(1)$.

# 📽️ Quick Demo

1. Install `requirements`
    
    ```bash
    pip install requirements.txt
    ```
    
2. Pytest
    
    ```bash
    cd efficient-keyword-search
    pytest --cov=src/
    ```
    
    ```bash
    ---test reporting---
    plugins: cov-3.0.0
    collected 5 items                                                                                                                                 
    
    test_full_keyword_search.py ..                                                                                                              [ 40%]
    test_keyword_search.py ...                                                                                                                  [100%]
    
    ----------- coverage: platform linux, python 3.7.5-final-0 -----------
    Name                          Stmts   Miss  Cover
    -------------------------------------------------
    KeywordSearch.py                100      3    97%
    test_full_keyword_search.py      18      1    94%
    test_keyword_search.py           25      1    96%
    utils.py                         47      3    94%
    -------------------------------------------------
    TOTAL                           190      8    96%
    ```
    

# 📐 Algorithms

Suppose we want to find our documents that contain the keywords of apple, avocado, and banana.

1.  Build a Tire-Tree by the keyword list.
    
    
    <img src="https://github.com/luli0034/efficient-keyword-search/blob/main/img/TrieTree.png" width="250" />
    
    
    
2. If we input a document namely `avocado` into the tree, once we meet the leaf means this document has the keyword of the current path.
    
    <img src="https://github.com/luli0034/efficient-keyword-search/blob/main/img/TrieTree_found.png" width="250" />
    ![TrieTree_found.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/817d9192-1346-4fc4-b43d-fdb5c35e7bc5/TrieTree_found.png)
    
3. If we input a document namely `avoc` into the tree, the traversal will stop in the middle of the path, which means that the keyword of the current path is not satisfied.
    
    <img src="https://github.com/luli0034/efficient-keyword-search/blob/main/img/TrieTree_notfound.png" width="250" />
    

# ⌚ Test Execution Time

- The following two methods are tested in 25 casees, number of texts from 340 to 68340, number of keywords from 8 to 1008.
- The results showed that TrieTree will be more efficient when a large scale keywords is present.

## Trie Tree Search
|      |        340 |     17340 |    34340 |    51340 |    68340 |
|-----:|-----------:|----------:|---------:|---------:|---------:|
|    8 | 0.0016973  | 0.075026  | 0.144685 | 0.217373 | 0.286705 |
|  258 | 0.00222325 | 0.0754781 | 0.149278 | 0.221971 | 0.294353 |
|  508 | 0.00281191 | 0.0747848 | 0.149163 | 0.220198 | 0.295152 |
|  758 | 0.00323772 | 0.0738354 | 0.145732 | 0.217291 | 0.292947 |
| 1007 | 0.0192423  | 0.0775256 | 0.150745 | 0.223519 | 0.301813 |
## Brute-force Search

|      |         340 |     17340 |     34340 |     51340 |     68340 |
|-----:|------------:|----------:|----------:|----------:|----------:|
|    8 | 0.000220537 | 0.0109131 | 0.0216031 | 0.0322795 | 0.0431697 |
|  258 | 0.00570846  | 0.29265   | 0.581531  | 0.86897   | 1.15168   |
|  508 | 0.0112755   | 0.572185  | 1.13525   | 1.69636   | 2.25317   |
|  758 | 0.016731    | 0.852622  | 1.68878   | 2.52411   | 3.3522    |
| 1007 | 0.0221889   | 1.12994   | 2.24023   | 3.34907   | 4.45298   |
