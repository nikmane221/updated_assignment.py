from flask import Flask,request,jsonify,json
from bson import ObjectId
from flask_pymongo import PyMongo, MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydb_1"
mydb = PyMongo(app)

@app.route("/")
#to get all the name from the db's collection
#"127.0.0.1:5000/mycol_1 shows all docs of db's collections on a web page"
@app.route('/mycol_1', methods=['GET'])
def all_mycol_1s():
    mycol_1 = mydb.db.mycol_1
    output = []
    for q in mycol_1.find():
        output.append({"name":q["name"], "img":q["img"], "summary":q["summary"]})

    return jsonify({"result":output})

#"127.0.0.1:5000/mycol_1/<name> shows requird name only from db's collections on a web page"
@app.route('/mycol_1/<name>', methods=['GET'])
def one_mycol_1s(name):
    mycol_1 = mydb.db.mycol_1
    q = mycol_1.find_one({"name":name})
    output = [{"name": q["name"], "img": q["img"], "summary": q["summary"]}] if q else "Movie name not in the db's collections"

    return jsonify({"result":output})

@app.route("/mycol_1", methods=["POST"])
def add_to_mycol_1s():
    mycol_1 = mydb.db.mycol_1; 
    name = request.json["name"]
    img = request.json["img"]
    summary = request.json["summary"]
    mycol_1_id = mycol_1.insert({"name":name,"img":img,"summary":summary})
    mycol_12 = mycol_1.find_one({"_id":mycol_1_id})
    output = [{"name": mycol_12["name"], "img": mycol_12["img"], "summary": mycol_12["summary"]}]

    return jsonify({"result":output})


if (__name__) == '__main__':
    app.run(debug=True)
