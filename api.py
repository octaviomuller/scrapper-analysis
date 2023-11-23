from flask import Flask, jsonify, request
from association import associate_keywords_with_colors_and_font
from keyword_extractor import keyword_extractor

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    data = request.json['text']
    keywords = keyword_extractor(data)
    result = associate_keywords_with_colors_and_font(keywords, similarity_threshold=0.01)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
