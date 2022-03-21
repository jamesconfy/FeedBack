from flask import render_template, redirect, url_for, request, flash
from feedback import db
from flask import current_app as app
from feedback.forms import FeedBack
from feedback.models import FeedBackModel
from feedback.utils import send_mail

@app.route('/')
@app.route('/home')
def home():
    feed = FeedBackModel.query.all()
    return render_template('index.html', title='Dashboard', feeds=feed)

@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    form = FeedBack()
    if request.method == "POST":
        if form.validate_on_submit():
            if form.dealer.data == 'None':
                dealer_data = ' '
            else:
                dealer_data = form.dealer.data
            feed = FeedBackModel(name=form.name.data, email=form.email.data, dealer=dealer_data, feedback=form.feedback.data)
            send_mail(name=form.name.data, email=form.email.data, dealer=dealer_data, feedback=form.feedback.data)
            db.session.add(feed)
            db.session.commit()
            flash('Correct Guy', 'success')
            return redirect(url_for('home'))
    return render_template('feedback.html', title='Feed Back', form=form)

@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "POST":
        name = f'{request.form["search"]}'
        feed = FeedBackModel.query.filter(FeedBackModel.name.contains(name)).all()
        return render_template('index.html', title='Searched Result', feeds=feed)



if __name__ == '__main__':
   app.run(debug = True)