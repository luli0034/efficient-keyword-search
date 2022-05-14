import pytest

@pytest.fixture
def data():
    pytest.keywords = ['資金','薪水']
    pytest.documents = [
        '今天天氣真好',
        '這錢也太少，你有沒有搞錯',
        '可以給我加薪嗎',
        '老闆不要鬧',
        '薪水不夠R',
        '很抱歉資金不足',
        '外包的資金為什麼不給員工當薪水就好'
    ]
    pytest.ans = [
        [],
        [],
        [],
        [],
        ['薪水'],
        ['資金'],
        ['資金','薪水'],
    ]
def test_raises_no_builed_tree(data):
    from KeywordSearch import FullKeywordsSearch
    with pytest.raises(ValueError) as e:
        tree = FullKeywordsSearch()
        tree.transform(pytest.documents)

def test_full_keyword_search(data):
    from KeywordSearch import FullKeywordsSearch
    tree = FullKeywordsSearch()
    tree.fit(pytest.keywords)
    res = tree.transform(pytest.documents)
    assert res==pytest.ans


if __name__ == '__main__':
    pytest.main()