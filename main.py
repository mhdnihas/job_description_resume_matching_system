from flask import Flask, request, render_template
import os
import PyPDF2

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='uploads/'

def extract_text_pdf(file_path):
    text=""
    with open(file_path,'rb') as file:
        reader=PyPDF2.PdfReader(file)
        for page in reader.pages:
            text+=page.extract_text()
    return text

def extract_text(file_path):
    if file_path.endwith('.pdf'):
        return extract_text_pdf(file_path)
    else:
        return ""





@app.route("/")
def matchresume():
    return render_template('matchresume.html')


@app.route("/matcher",methods=['GET','POST'])
def matcher():
    if request.method=='POST':
        job_description=request.form.get('job-description')
        resume_files=request.form.getlist('resumes')
        resumes=[]
        for resume_file in resume_files:
            filename=os.path.join(app.config['UPLOAD_FOLDER'],resume_file.filename)
            resume_file.save(filename)
            resumes.append(extract_text(filename))





if __name__ == '__main__':
    app.run(debug=True)
