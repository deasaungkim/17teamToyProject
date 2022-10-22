from flask import Flask, render_template, request, jsonify, json

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


# # 회원가입
@app.route('/register', methods=['GET', 'POST'])
def register1():
    if request.method == "GET":
        return render_template('register.html')
    else:
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password_check = request.form['password_check']

    if not (username and email and password and password_check):
        return jsonify({'msg': "빈칸을 채워주세요."})
    elif password != password_check:
        return jsonify({'msg': "비밀번호가 일치하지 않습니다."})
    else:
        doc = {
            "email": email,
            "username": username,
            "password": password,
        }
        db.users.insert_one(doc)

        return jsonify({'result': 'success'})


@app.route("/food", methods=["POST"])
def food_get():
    food_receive = request.form["food_give"]
    food_list = db.foodlist.find_one({'menu': food_receive}, {
        '_id': False})
    return jsonify({'result': food_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
