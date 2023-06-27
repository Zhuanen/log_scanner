from flask import Flask, render_template, request
from test import show_pk

app = Flask(__name__)

@app.route('/')
def index():
    show = "POKEMON"
    return render_template("index.html",testPk = show)




# @app.route('/process', methods=['POST'])
# def process():
#     num1 = float(request.form['num1'])
#     num2 = float(request.form['num2'])
#     result = show_pk(num1, num2)
#     print(result)
#     return render_template("index.html",result = result)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the uploaded file
    file = request.files['fileUpload']
    data = file.read().decode('utf-8') 
    lines = data.split("\n")
    

    result = show_pk(lines)
    return render_template("index.html",result = result )

# @app.route('/user/<name>')
# def member(name):
#     return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)