from flask import Flask,jsonify,request

app=Flask(__name__)
contacts=[{

    "id":1,
    "contact":"8655939882",
    "name":"Dad",
    "done":False 
},
{

    "id":2,
    "contact":"7689963421",
    "name":"Mom",
    "done":False 
}
]
@app.route("/app-data",methods=["POST"])

def add_contact():
    if not request.json:
        return jsonify({"status":"error","message":"please provide the data."},400)
    contact=[{

        "id":contacts[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json["contact",""],
        "done":False
    }]
    contact.append(contacts)
    return jsonify({"status":"succesful","message":"sucessfully added a new task"})

@app.route("/get-data")

def get_task():
    return jsonify({
       "data":contacts,
    })

if __name__=="__main__":
    app.run(debug=True)
