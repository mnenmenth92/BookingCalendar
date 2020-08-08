from flask_restful import Resource
from flask import render_template, make_response

# main page
class MainPage(Resource):

    # return index.html
    def get(self):
        return make_response(render_template('build/index.html', 200))