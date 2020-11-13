

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
	return jsonify({'id': 3,'title':'Xen and the Art of Surviving Graduate School'},{"id" : 4,'title':'Cooking for the Impatient Graduate Student'}) 






if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True,port=5002)   



