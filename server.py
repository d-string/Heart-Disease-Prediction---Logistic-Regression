import os
import sys
import random
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route("/heart", methods=["GET", "POST"])
def klasifikasi():

    post = request.get_json()

    var_independent = [0] * 13
    var_independent[0] = post["age"]
    var_independent[1] = post["sex"]
    var_independent[2] = post["cp"]
    var_independent[3] = post["trestbps"]
    var_independent[4] = post["chol"]
    var_independent[5] = post["fbs"]
    var_independent[6] = post["restecg"]
    var_independent[7] = post["thalach"]
    var_independent[8] = post["exang"]
    var_independent[9] = post["oldpeak"]
    var_independent[10] = post["slope"]
    var_independent[11] = post["ca"]
    var_independent[12] = post["thal"]
    var_independent = ",".join(var_independent)

    os.system("python -W ignore heart_analysis.py " + var_independent)
    f = open("klasifikasi_result.txt", "r")
    l = f.readline()
    f.close()
    return jsonify(
        result="Anda Tidak Terkena Penyakit Jantung"
        if l == "0"
        else "Anda Terkena Penyakit Jantung"
    )


# Application1
if __name__ == "__main__":
    app.run(debug=True)
