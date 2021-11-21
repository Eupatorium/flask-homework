from flask import Flask, jsonify, request
app = Flask(__name__)

names = [
    {
        'id': 1,
        'Name':'Raju',
        'Contact': '9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': 'Rahul',
        'Contact': '9876543222', 
        'done': False
    }
]


@app.route("/")
def Welcom():
    return "Welcome"

@app.route("/add-data",methods = ["POST"])

def add_task():
    
    if not request.json:
        return jsonify({
            "status": "error", 
            "message": "please provide sufficient data"
        },400) 

    contact = {
        'id':names [-1]['id']+1,
        'Name':request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }

    names.append(contact)

    return jsonify({
            "status": "success", 
            "message": "contact added"
        })

@app.route("/get-data")

def get_task():
    return jsonify({"data":names})

if __name__ == '__main__':
    app.run()