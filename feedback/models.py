from feedback import db

class FeedBackModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    feedback = db.Column(db.Text(), nullable=False)
    dealer = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'My name is {self.name}, with an email of {self.email}'