from flask import Flask, request, render_template
from glovevec_analogy import gloveVec

app = Flask(__name__)

#preload the gloveVector
gloveVecAnalogy = gloveVec()


@app.route('/')
def homepage():
	return render_template('index.html')

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

	return w3


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)	