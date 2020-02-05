from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploaded_files'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file_data():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_name = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return f'File {f.filename} was successfully uploaded'

if __name__ == '__main__':
    app.run(debug=True)