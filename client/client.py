
import urllib

from flask import Flask,jsonify 


app = Flask(__name__)



@app.route('/search/distributed systems', methods=['GET'] )
def search_dos():
	return  urllib.request.urlopen("http://127.0.0.1:5001/query_by_subject/distributed").read()
	 
   


@app.route('/search/graduate school', methods=['GET'] )
def search_dos_2():
	return urllib.request.urlopen('http://0.0.0.0:5001/query_by_subject/graduate school').read()


	
if __name__ == '__main__':
    app.run(debug = True,host = "127.0.0.2", port ="5001")    