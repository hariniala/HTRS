from flask import Flask, render_template, request
import main
import urllib.request
#from app import app
from werkzeug.utils import secure_filename
from main import infer
from main import FilePaths
import os
app = Flask(__name__)

@app.route('/', methods=['GET'])

def hello_word():

    return render_template('main.html')

@app.route('/', methods=['POST'])

def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
           
            #flash(r)
            #return render_template('main.html',prediction=r)
            #return redirect('/')




if __name__ == '_main_':
     app.run(port=3000, debug=True)