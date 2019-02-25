from flask import Flask, render_template, request
import InformationRetrieval as ir

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("input-form.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        word = request.form.get("Search")
        res = ir.invertedIndex(word)
    return render_template("result.html", result=res)


if __name__ == '__main__':
    app.run(debug=True)
