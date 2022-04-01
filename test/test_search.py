from tests import TestWebAppClient

class TestSearch():
    def test_home_search(self):
        response = TestWebAppClient.post('/search', data={'search': 'Praise'})
        assert response.status_code == 200
        html =  response.get_data(True)

        assert 'Praise' in html
        assert '<td>' in html
        assert 'Searched Result' in html
        assert 'Faith' in html