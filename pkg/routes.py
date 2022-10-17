from flask import render_template,request,flash,session,make_response
from pkg import ager

@ager.route('/')
def indexx():
    return render_template('index.html')


@ager.route('/field officer dashboard/')
def fo_dashboard():
    return render_template('fo_dashboard.html')


@ager.route('/register farmer/')
def register_farmer():
    return render_template('farmer_reg.html')


@ager.route('/field officer dashboard/my farmers/')
def myfarmers():
    return render_template('my_farmers.html')

@ager.route('/view farmer profile/')
def seefarmerprofile():
    return render_template('seefarmers.html')