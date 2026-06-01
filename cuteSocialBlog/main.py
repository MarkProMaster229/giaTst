from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS
from bisnesLogic.tool import Registration

app = Flask(__name__)
CORS(app)



if __name__ == '__main__':
    app.run(debug=True)