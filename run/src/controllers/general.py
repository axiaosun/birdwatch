#!/usr/bin/env python3

from flask import Blueprint, render_template, request, redirect, session
import operator
from . import models

controller = Blueprint('bird', __name__, url_prefix='/bird')

@controller.route('/home', methods = ['GET','POST'])
def home():
	if request.method == 'GET':
		models.connect_db()
		tweets_list = models.gettweets_all()
		return render_template('home.html', tweets_list=tweets_list)
	else:
		submitted_username = request.form['username']
		if models.login(submitted_username):
			session['username'] = submitted_username
			return redirect ('/bird/user')
		else:
			session['username'] = submitted_username
			models.create(submitted_username)
			return redirect ('/bird/user')

@controller.route('/user', methods = ['GET','POST'])
def user():
	user = session['username']
	if request.method == 'GET':
		tweets_list = models.gettweets_user(user)
		return render_template('user.html', user=user, tweets_list=tweets_list)
	else:
		new_tweet = request.form['tweet']
		if models.tweet(new_tweet, user):
			tweets_list = models.gettweets_user(user)
			return render_template('user.html', user=user, tweets_list=tweets_list)
		else:
			return render_template('user.html', user=user, tweets_list=tweets_list)

@controller.route('/logout', methods = ['GET'])
def logout():
	if session:
		session.clear()
	return redirect('/bird/home')