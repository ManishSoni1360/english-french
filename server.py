from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translateToFrench', methods=['POST'])
def translate_text():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Text is Missing'}), 400

    text = data['text']
    translation = translator.translate(text, dest='fr').text
    translation = translation.replace('comment allez-vous', 'comment ça va')
    return jsonify({'translation': translation})

