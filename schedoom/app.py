from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    data = {
            
            "cronList": [
                {
                    "date": "10 0 * * *",
                    "command": "curl www.google.com"
                },
                {

                    "date": "10 20 * * *",
                    "command": "cd /home/ssd && ping www.google.com"

                }
            ]
        }

    
    return jsonify(data)  


if __name__ == '__main__':
    app.run()