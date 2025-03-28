from flask import Flask,render_template, request

app = Flask(__name__,template_folder="templates")

@app.route("/")
def hello():
    return render_template('start.html')

@app.route("/create")
def create():
    return render_template('create.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    # process the data using Python code
    result = data.upper()
    return result

if __name__ == '__main__':
    app.run(debug=True)
