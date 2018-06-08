from flask import Flask, request, render_template

app = Flask(__name__)

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
	args = [w0, w1, w2]

	print(":".join(args))

	return ' sending ' +  ':'.join(args)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000, debug=True)	