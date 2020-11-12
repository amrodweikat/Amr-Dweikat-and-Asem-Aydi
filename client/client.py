
import urllib

from flask import Flask,jsonify 


app = Flask(__name__)



@app.route('/', methods=['GET'] )
def hello_world():
	return urllib.request.urlopen('http://0.0.0.0:5001/query_by_subject/distributed systems').read()
   

	
if __name__ == '__main__':
    app.run(debug = True)    