from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/getReposts", methods = ["GET"])
def getReposts():
    return "100 Reposts"

@app.route("/getLikes", methods = ["GET"])
def getLikes():
    return "200 Likes"

@app.route("/getBookmarks", methods = ["GET"])
def getBookmarks():
    return "300 Bookmarks"    


if __name__ == "__main__":
    app.run(debug=True)




#Practice from video
#@app.route("/get-user/<user_id>")
#def get_user(user_id):
#    user_data = {
#        "user_id": user_id,
#        "name": "John Doe",
#        "email": "john.doe@example.com"
#    }

#    extra = request.args.get("extra")
#    if extra:
#        user_data["extra"] = extra
#
#    return jsonify(user_data), 200


#@app.route("/create-user",methods=["POST"])
#def create_user():
#    data = request.get_json()
#
#    return jsonify(data), 201
