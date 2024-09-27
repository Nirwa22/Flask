from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def home():
    return "home"
@app.route("/user_data/<user_id>/<name>")
def user_id(user_id, name):
    user_data = {
            "User_Id": user_id,
            "Name": name
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"]=extra
    return jsonify(user_data),200

@app.route("/post_request",methods=["POST"])
def request():
    data = request.get_json()
    return jsonify(data),201

if __name__ == '__main__':
    app.run(debug=True)