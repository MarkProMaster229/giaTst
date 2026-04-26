from myBdConnect.endine import SessionLocal, Base
from myBdConnect.models import Users, Original_os, Comment, Likes
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])

@app.route('/forMainLabel')
def forRegistration():
    #probably frontent have - label witch name usersName