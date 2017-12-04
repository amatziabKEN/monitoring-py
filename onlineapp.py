import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/roles')
def getserversroles():
    req = requests.get('http://badger.kenshoo.com/server/roles')
    list = req.json()
    return render_template("shopping.html", food=list)
    return

@app.route('/servers')
def getservers():
    req = requests.get('http://badger.kenshoo.com/servers')
    list = req.json()
    return render_template("shopping.html", food=list)
    return


if __name__ == "__main__":
    app.run(debug=True)



