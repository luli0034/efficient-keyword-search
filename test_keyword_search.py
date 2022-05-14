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
    pytest.ans_1_hit = [
        '薪水不夠R',
        '很抱歉資金不足',
        '外包的資金為什麼不給員工當薪水就好'
    ]
    pytest.ans_2_hit = [
        '外包的資金為什麼不給員工當薪水就好'
    ]
def test_raises_no_builed_tree(data):
    from KeywordSearch import KeywordSearch
    with pytest.raises(ValueError) as e:
        tree = KeywordSearch()
        tree.transform(pytest.documents)

def test_search_at_least_1_hit(data):
    from KeywordSearch import KeywordSearch
    tree = KeywordSearch()
    tree.fit(pytest.keywords)
    res = tree.transform(pytest.documents)
    assert res==pytest.ans_1_hit

def test_search_at_least_2_hit(data):
    from KeywordSearch import KeywordSearch
    tree = KeywordSearch()
    tree.fit(pytest.keywords)
    res = tree.transform(pytest.documents, hits=2)
    assert res==pytest.ans_2_hit

if __name__ == '__main__':
    pytest.main()