from flask import Flask

from models.pages import Page
from utils import import_data

app = Flask(__name__)


@app.route('/')
def home_page():
    if a := import_data():
        return Page(a).home()
    return 'File not found'


@app.route('/candidates/<int:uid>')
def candidates_page(uid):
    if a := import_data():
        return Page(a).candidates(uid)
    return 'File not found'


@app.route('/skills/<skill>')
def skills_page(skill):
    if a := import_data():
        return Page(a).skills(skill)
    return 'File not found'


if __name__ == '__main__':
    app.run()
