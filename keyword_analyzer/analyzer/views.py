from flask import render_template, request, jsonify

from keyword_analyzer.analyzer.impl import url_statistics


def index():
    return render_template('index.html')


def get_statistics():
    req = request.json

    return jsonify(url_statistics(req['url']))
