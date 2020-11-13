from flask import Flask,jsonify


app = Flask(__name__)



@app.route('/query_by_subject/distributed',methods=['GET'])
def query_by_subject():
	return jsonify({'id': 1,'title':'How to get a good grade in DOS in 20 minutes a day'},{"id" : 2,'title':'RPCs for Dummies'})
   

@app.route('/query_by_subject/graduate',methods=['GET'])
def query_by_subject_2():
	return jsonify({'id': 3,'title':'Xen and the Art of Surviving Graduate School'},{"id" : 4,'title':'Cooking for the Impatient Graduate Student'}) 


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True,port=5002)   



