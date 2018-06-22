from flask import Flask, render_template, request
app = Flask(__name__, static_folder='static')

@app.route('/')
def hello_world():
    #return 'Hello World'
    return render_template('cover.html')
    
@app.route('/foo')
def return_foo():
    #return 'Hello World'
    return 'The actual Result'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
