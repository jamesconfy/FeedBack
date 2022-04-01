import unittest
from flask import current_app, session
# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/mac/Downloads/Python Projects/FeedBack/')
from feedback import create_app, db
from feedback.models import FeedBackModel

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite://'})
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.populate_db()

        return self.app

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def populate_db(self):
        myfeedback = FeedBackModel(name='James Confidence', feedback='The service was very nice, yunno.', email='bobdence@gmail.com', dealer='Praise')
        myfeedback1 = FeedBackModel(name='Ugwudike Confidence', feedback='The service was definitely nice.', email='bobdence@live.com', dealer='Peculiar')
        myfeedback2 = FeedBackModel(name='Praise James', feedback='Yo man, the service was dope.', email='jammzy0@gmail.com', dealer='Faith')

        db.session.add(myfeedback)
        db.session.add(myfeedback1)
        db.session.add(myfeedback2)
        db.session.commit()


    def test_app(self):
       assert self.app is not None
       assert current_app == self.app

TestWebAppClient = TestWebApp().setUp().test_client()