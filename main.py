from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os
import deepspeech
import mp3_wav
app = Flask(__name__)
app.secret_key = 'my-secret-key'
app.config['UPLOAD_FOLDER'] = "GIVE PATH TO FOLDER"

@app.route("/")
def home():
    return render_template('index.html')
 
@app.route('/output',methods=['POST','GET'])
def ouput():
    if request.method=='POST':
        file = request.files["audio"]
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if filename.split('.')[1]=="mp3":
            filename = mp3_wav.preprocess_file(filename)
            
        text = deepspeech.generate("static/img/"+filename)
        return render_template('output.html',text=text)
    else:
        return "Something wrong happened"

#to automatically detecting changes and debugging
if __name__ == "__main__":
    app.debug=True
    app.run(host="192.168.43.204",port=8000)

#app.run(debug=True)
