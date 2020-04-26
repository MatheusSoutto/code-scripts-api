from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://matheus-soutto:Matheus13@hackerrank-jyajn.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/create',  methods=['POST'])
def create():
    if 'file' in request.files:
        file = request.files['file']
        mongo.save_file(file.file_name, file)
    
    return 'Done!'

