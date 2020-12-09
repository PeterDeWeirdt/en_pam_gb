from flask import Flask, request, jsonify
from sgrna_modeler import models as sg
from sgrna_modeler import enzymes as en

app = Flask(__name__)

model = sg.SklearnSgrnaModel()
model_weights = sg.get_enpam_gb()
model.load_model(model_weights, en.cas12a, 'enPAM_GB')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict_seqs(data)
    output = {'prediction': list(prediction)}
    return jsonify(results=output)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
