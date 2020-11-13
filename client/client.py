
import urllib

from flask import Flask,jsonify 


app = Flask(__name__)



@app.route('/search/distributed systems', methods=['GET'] )
def search_dos():
	return  urllib.request.urlopen("http://127.0.0.1:5001/query_by_subject/distributed").read()
	 
   


@app.route('/search/graduate school', methods=['GET'] )
def search_dos_2():
	return urllib.request.urlopen('http://127.0.0.1:5001/query_by_subject/graduate').read()


@app.route('/lookup/1', methods=['GET'] )
def lookup_1():
	return urllib.request.urlopen('http://127.0.0.1:5001/query_by_item/1').read()


@app.route('/lookup/2', methods=['GET'] )
def lookup_2():
	return urllib.request.urlopen('http://127.0.0.1:5001/query_by_item/2').read()


@app.route('/lookup/3', methods=['GET'] )
def lookup_3():
	return urllib.request.urlopen('http://127.0.0.1:5001/query_by_item/3').read()	


@app.route('/lookup/4', methods=['GET'] )
def lookup_4():
	return urllib.request.urlopen('http://127.0.0.1:5001/query_by_item/4').read()

@app.route('/buy/1', methods=['POST'] )
def look():
	return urllib.request.urlopen('http://127.0.0.2:5002/buy/1').read()

	
if __name__ == '__main__':
    app.run(debug = True,host = "127.0.0.2", port ="5001")    