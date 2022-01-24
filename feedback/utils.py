from flask_mail import Message
from feedback import mail

def send_mail(email, name, dealer, feedback):
    msg = Message(subject='noreply-flask', recipients=[email], sender='noreply@demo.com')
    msg.html = f'<h2>Customer: {name}.</h2>\n<h3>Dealer: {dealer}.</h3>\n<h4>Feedback: {feedback}.</h4>'
    mail.send(msg)

    return msg