from flask import Flask


app = Flask(__name__)



@app.route('/query_by_subject/distributed systems',methods=['GET'])
def query_by_subject():
	return "hello_world"
   
 


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True,port=5001)   



