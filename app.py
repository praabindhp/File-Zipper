from flask import Flask
import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file:
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('File(s) Successfully Uploaded')
		return redirect('/')

if __name__=='__main__':
    app.run(debug=True)