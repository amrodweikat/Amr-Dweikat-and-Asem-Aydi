

from flask import Flask,jsonify
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn



@app.route('/query_by_subject/distributed',methods=['GET'])
def query_by_subject():
	conn   = db_connection()
	cursor = conn.cursor()
	cursor = conn.execute("SELECT id,title FROM book WHERE topic='distributed systems'")
	books = [
		dict(id=row[0],title=row[1])
		for row in cursor.fetchall()
	]
	if books is not None:
		return jsonify(books)

	

@app.route('/query_by_subject/graduate',methods=['GET'])
def query_by_subject_2():
	conn   = db_connection()
	cursor = conn.cursor()
	cursor = conn.execute("SELECT id,title FROM book WHERE topic='graduate school'")
	books = [
		dict(id=row[0],title=row[1])
		for row in cursor.fetchall()
	]
	if books is not None:
		return jsonify(books)

	
	
@app.route('/query_by_item/1',methods=['GET'])
def query_by_item():
	conn   = db_connection()
	cursor = conn.cursor()
	cursor = conn.execute("SELECT title,quantity,price FROM book WHERE id=1")
	books = [
		dict(title=row[0],quantity=row[1],price=row[2])
		for row in cursor.fetchall()
	]
	if books is not None:
		return jsonify(books)







if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True,port=5002)   



