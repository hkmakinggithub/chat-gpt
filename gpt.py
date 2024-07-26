from flask import Flask, render_template ,jsonify ,request
from flask_pymongo import PyMongo
app = Flask(__name__)

mongo = PyMongo(app)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api",methods=["GET","POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        data ={"resulat":f"anser of  {question}"}
        return jsonify(data)
         
    data ={"resulat":"that is oihdlgfouf"}
    return jsonify(data)


app.run(debug=True)