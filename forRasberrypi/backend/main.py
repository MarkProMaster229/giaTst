from flask import Flask, request, jsonify
from flask_cors import CORS
from bisnesLogic.bisnes import Analization, Return_data
import uuid

app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'])

@app.route('/server',methods=['POST'])
def main_label():
    user = request.form.get('user')
    about = request.form.get('about')
    image = request.files.get('image')

    originalName = image.filename
    unique_prefix = str(uuid.uuid4())
    originalName = f"{unique_prefix}_{originalName}"

    bisnes_logic = Analization()
    bisnes_logic.initialization(user,about,originalName)
    bisnes_logic.workForSave(image, originalName)

    return jsonify({'status': 'ok'})

@app.route('/getMyImages', methods=['GET'])
def useEff():
    images_and_data = Return_data()
    type = images_and_data.retData()
    return jsonify(type)
      



if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)