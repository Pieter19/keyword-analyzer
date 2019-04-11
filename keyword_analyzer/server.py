from flask import Flask

from keyword_analyzer import urls


class FlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        super(FlaskApp, self).__init__(*args, **kwargs)
        for item in urls.layout:
            self.register_blueprint(**item)


app = FlaskApp(__name__)
