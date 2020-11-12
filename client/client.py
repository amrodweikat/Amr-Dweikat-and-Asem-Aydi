
import urllib

from flask import Flask,jsonify 


app = Flask(__name__)



@app.route('/serach/distributed systems', methods=['GET'] )
def hello_world():
	return urllib.request.urlopen('http://0.0.0.0:5001/').read()
   
@app.route('/serach/graduate school', methods=['GET'] )
def hello_world():
	return urllib.request.urlopen('http://0.0.0.0:5001/').read()
	
if __name__ == '__main__':
    app.run(debug = True)    