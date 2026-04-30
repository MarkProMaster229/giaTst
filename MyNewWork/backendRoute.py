from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS 
from backendbisnesLogic import GetInfo
app = Flask(__name__)
g = GetInfo()
CORS(app)
@app.route('/fullPeople', methods=['GET'])
def forlabel():
    a = g.full_info()
    print("bit")
    return a



if __name__ == '__main__':
    app.run(debug=True)