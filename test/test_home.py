from tests import TestWebAppClient

class TestHome():
    def test_home_page_redirect(self):
            response = TestWebAppClient.get('/home' or '/')
           # print(response.data)
            assert response.status_code == 200
            html = response.get_data(True)

            assert 'Praise' in html
            assert 'jammzy0@gmail.com' in html
            assert 'yunno.' in html