from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS
from bisnesLogic.tool import Registration, Autorization


app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])
@app.route('/dataProduct')
def uploud_data():
    data = request.get_json()
    if not data: 
        return jsonify({"error data"})
        