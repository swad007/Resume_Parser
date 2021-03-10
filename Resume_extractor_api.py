# 23-02-21
# Swadhin Das

#---------------------------------------Imports---------------------------------------------------------------------------

import flask, request, jsonify

import spacy
import spacy.cli

import nltk

from resume_parser import resumeparse

#---------------------------------- App -----------------------------------------------------------------------------------

app = flask(__name__)

@app.route('/extract_resume', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return "Hello"

    content = request.json()
    data = resumeparse.read_file('/content/Anubhab_Cover letter.pdf')

    result =data

    return jsonify( {'solution_text': result } )
