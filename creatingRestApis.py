from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    jsonResult = {
        "Name":"Ishan",
        "Age":17,
        "Field":"Information Technology",
        "Mail":"studentofgpg@gmail.com"
    }
    return jsonify(jsonResult)



if __name__ == "__main__":
    app.run(debug=True)