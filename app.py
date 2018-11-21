# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
import yaml
from flask import Flask
from flask import jsonify, render_template
app = Flask(__name__)

# NOTE: replace with your own api credentials
with open('api_keys.yaml', 'r') as f:
    api = yaml.load(f)

language = 'en'
# word_id = 'Apprehension'

@app.route('/get_word/<word_id>')
def words(word_id):
    # return 'Hello, World!'
    url = api['url'] + language + '/' + word_id.lower()
    r = requests.get(url, headers = {'app_id': api['id'], 'app_key': api['key']})

    # print("code {}\n".format(r.status_code))
    # print("text \n" + r.text)
    # print("json \n" + json.dumps(r.json()))
    return jsonify(r.json())


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hw')
def hello_world():
    return 'hello world!'
