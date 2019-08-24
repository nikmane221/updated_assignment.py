from flask import Flask,request,jsonify,json
from bson import ObjectId
from flask_pymongo import PyMongo, MongoClient

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydb_1"
mydb = PyMongo(app)

# to get all data from the database

@app.route('/mycol_1', methods=['GET'])
def all_mycol_1s():
    mycol_1 = mydb.db.mycol_1
    output = []
    for q in mycol_1.find():
        output.append({"name":q["name"], "img":q["img"], "summary":q["summary"]})

    return jsonify({"result":output})

# to get specific name from the database

@app.route('/mycol_1/<string:name>', methods=['GET'])
def one_mycol_1s(name):
    mycol_1 = mydb.db.mycol_1
    q = mycol_1.find_one({"name":name})
    output = [{"name": q["name"], "img": q["img"], "summary": q["summary"]}] if q else "Movie name not in the db's collections"

    return jsonify({"result":output})

if (__name__) == '__main__':
    app.run(debug=True)
