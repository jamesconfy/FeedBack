from tests import TestWebAppClient
# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/Users/mac/Downloads/Python Projects/FeedBack/')
from feedback.utils import send_mail

data = {
    'name': 'James Confidence',
    'feedback': 'The service was very nice, yunno.',
    'email': 'bobdence@gmail.com',
    'dealer': 'None'
}

class TestUtils():
    def test_utils(self):
        msg = send_mail(email=data['email'], name=data['name'], feedback=data['feedback'], dealer=data['dealer'])
        assert msg.sender == 'noreply@demo.com'
        assert msg.recipients == [data['email']]