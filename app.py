from flask import Flask
from flask import Flask, render_template, request
from flask import Flask, flash, request, redirect, url_for
import os
import json
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.static_folder = 'static'
UPLOAD_FOLDER = '/static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set([ 'pdf'])

@app.route("/", methods=[ 'POST','GET'])
def home():
    if request.method == 'POST':
        # if 'pdf's' not in request.files:
        #     print("wrong")
        file_names=[]
        pdf_s = request.files.getlist('pdf')
        for pdf in pdf_s:
            if pdf.filename != '':
                file_names.append(str(pdf.filename)[:-4].lower())
                pdf.save(os.path.join(app.root_path, f'static/{pdf.filename}'))
        isdone=True
        return render_template("index.html",isdone=True,file_names=json.dumps(file_names),len=len(file_names))
    return render_template("index.html")

if __name__ == "main":
    app.run()