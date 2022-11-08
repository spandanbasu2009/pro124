from flask import Flask,jsonify,request
app = Flask(__name__)
contacts = [
    {
        "ID":1,
        "Contact":"1029384756",
        "Name":"Spandan",
        "Done":False
    },
    {
        "ID":2,
        "Contact":"0192837465",
        "Name":"Spandy",
        "Done":False
    }
]

@app.route('/post-data',methods = ["POST"])
def post_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        })
    contact = {
        "ID":contacts[-1]["ID"]+1,
        "Contact":request.json["Contact"],
        "Name":request.json.get("Name",""),
        "Done":False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

app.route('/get-data')
def get_task():
    return jsonify({
        "data":contacts
    })

if (__name__ == "__main__"):
    app.run(debug = True)