#!/usr/bin/env

import sqlite3
import operator
import os

database = 'birds.db'

def connect_db():
	if not os.path.exists(database):
		connection = sqlite3.connect(database,check_same_thread=False)
		cursor = connection.cursor()

		cursor.execute(
			"""CREATE TABLE users(
				username TXT PRIMARY KEY
			);"""
		)

		cursor.execute(
			"""CREATE TABLE tweets(
				pk INTEGER PRIMARY KEY AUTOINCREMENT,
				tweet TEXT,
				tweet_username TEXT,
				FOREIGN KEY(tweet_username) REFERENCES user(username)
			);"""
		)

		cursor.close()
		connection.close()
	else:
		pass

def login(username):
    connection = sqlite3.connect(database, check_same_thread = False)
    cursor = connection.cursor()
    query = 'SELECT count(*) FROM users WHERE username = "{}";'.format(username)
    cursor.execute(query)
    result_tuple = cursor.fetchone()
    cursor.close()
    connection.close()
    if result_tuple[0] == 0:
        return False
    elif result_tuple[0] == 1:
        return True
    else:
        pass

def create(new_user):
    connection = sqlite3.connect(database, check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO users(
            username
            ) VALUES(
            '{}'
        );""".format(new_user)
    )
    connection.commit()
    cursor.close()
    connection.close()

def gettweets_all():
	connection = sqlite3.connect(database, check_same_thread = False)
	cursor = connection.cursor()
	query = 'SELECT tweet, tweet_username FROM tweets ORDER BY pk;'
	cursor.execute(query)
	fetched_result = cursor.fetchall()
	cursor.close()
	connection.close()
	return fetched_result

def gettweets_user(username):
    connection = sqlite3.connect(database, check_same_thread = False)
    cursor = connection.cursor()
    query = 'SELECT tweet FROM tweets WHERE tweet_username = "{}";'.format(username)
    cursor.execute(query)
    fetched_result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return fetched_result

def tweet(tweet, username):
	connection = sqlite3.connect(database,check_same_thread = False)
	cursor = connection.cursor()
	cursor.execute("""
		INSERT INTO tweets(
		tweet,
		tweet_username
		) VALUES(
		"{}","{}"
		)""".format(tweet, username)
	)
	connection.commit()
	cursor.close()
	connection.close()
	return True

