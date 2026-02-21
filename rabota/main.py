from datetime import datetime
from itertools import zip_longest
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from backend import Material_data

import sys

app = Flask(__name__)

material_data = Material_data("127.0.0.1","examen","postgres","Admin123","5433")

@app.route('/', methods=['GET', 'POST'])
def root():
    print(material_data.get_edinica_izmerenia("1"))
    return render_template("MasterPage.html")




if __name__ == '__main__':
    app.run(debug=True)


