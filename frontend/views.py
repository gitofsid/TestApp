from flask import Flask, url_for, request, render_template, redirect
from frontend import app #,my_sqlclient


@app.route('/home', methods=['GET'])
def welcomeToOrganDontation():
    return render_template('home.html')


@app.route('/', methods=['GET'])
@app.route('/google', methods=['GET'])
def takeToGoole():
    return redirect('http://www.google.com')

@app.route('/another', methods=['GET'])
def takeToAnother():
    return render_template('another.html')