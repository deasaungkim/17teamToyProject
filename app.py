from flask import Flask, render_template,request,jsonify,json
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:sparta@cluster0.scjlryq.mongodb.net/Cluster0@?retryWrites=true&w=majority")
db = client.dbsparta
@app.route('/')
def home():
    return render_template('toy.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/join')
def join():
    return render_template('join.html')

# @app.route("/homework", methods=["POST"])
# def homework_post():
#     food_receive = request.form["food_give"]
#
#     doc = {
#         'name': name_receive,
#
#     }
#
#     db.foodlist.insert_one(doc)
#     return jsonify({'msg':'응원을 남겨주셔서 감사합니다!'})

@app.route("/food", methods=["POST"])
def food_get():
    food_receive = request.form["food_give"]
    food_list = db.foodlist.find_one({'menu':food_receive},{
        '_id':False})
    return jsonify({'result':food_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

