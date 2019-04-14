from flask import Blueprint

from keyword_analyzer.analyzer import urls

analyzer_blueprint = Blueprint('analyzer', __name__)

for item in urls.layout:
    analyzer_blueprint.add_url_rule(**item)
