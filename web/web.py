from flask import Flask, render_template, request, Response, send_from_directory
import os
import sys
sys.path.append('../')
from gloveUtils.gloveAnal import gloveVec




app = Flask(__name__, static_folder='static')


#preload the gloveVector
gloveVecAnalogy = gloveVec()


@app.route('/')
def hello_world():
    #return 'Hello World'
    return render_template('index.html')
    
@app.route('/foo')
def return_foo():
    #return 'Hello World'
    return Response('fooResult', mimetype='text/plain')


@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/result')
def result():
	#return 'Input =' + request.args.get('w0') + ':' + request.args.get('w1') + '=' + request.args.get('w2') + '?'
	w0 = request.args.get('w0')
	w1 = request.args.get('w1')
	w2 = request.args.get('w2')


	if not w0 or not w1 or not w2:
	  return "make sure there are all arguments e.g. /result?w1=foo&w0=ppp&w2=rma"

	print('input :' + w0 + ':' + w1 + ' --> ' + w2 + ': ? ')

	w3=gloveVecAnalogy(w0,w1,w2)

	print(w0 + ':' + w1 + ' --> ' + w2 + ':' + w3)

	return Response(w3, mimetype='text/plain')


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)	