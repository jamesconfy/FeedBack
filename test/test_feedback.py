from unicodedata import name
from tests import TestWebAppClient
# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/mac/Downloads/Python Projects/FeedBack/')
from feedback import db
from feedback.models import FeedBackModel

data = dict(name='James Lovely',
                feedback='The service was very nice, yunno.',
                email='replymethis.com',
                dealer='None')

class TestFeedBack():
    def test_feedback_page(self):
        response = TestWebAppClient.get('/feedback')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="feedback"' in html
        assert 'name="dealer"' in html

    def test_database(self):
        myfeedback = FeedBackModel.query.filter_by(
            email='bobdence@gmail.com').first()

        assert myfeedback is not None
        assert myfeedback.name == 'James Confidence'
        assert myfeedback.feedback == 'The service was very nice, yunno.'
        assert myfeedback.email == 'bobdence@gmail.com'
        assert myfeedback.dealer == 'Praise'

    def test_feedback_and_redirects(self):
        response = TestWebAppClient.post(
            '/feedback',
            data=data,
            follow_redirects=True)

        myfeedback = FeedBackModel(name=data['name'], email=data['email'], feedback=data['feedback'], dealer=data['dealer'])
        db.session.add(myfeedback)
        db.session.commit()

        checkall = FeedBackModel.query.filter_by(name=data['name']).first()
        assert response.status_code == 200
        assert checkall is not None
        assert checkall.email == 'replymethis.com'
        #html = response.get_data(as_text=True)
        #print(html)

        #assert response.request.path == '/'