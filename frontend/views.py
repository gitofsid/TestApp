from flask import Flask, url_for, request, render_template, redirect
from frontend import app #,my_sqlclient


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def welcomeToOrganDontation():
    return render_template('home.html')
