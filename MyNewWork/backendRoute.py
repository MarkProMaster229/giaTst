from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS 

app = Flask(__name__)
@app.route('/fullPeople', methods=['GET'])
def forlabel():
    print("bit")



if __name__ == '__main__':
    app.run(debug=True)