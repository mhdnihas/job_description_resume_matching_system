from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def matchresume():
    return render_template('matchresume.html')

if __name__ == '__main__':
    app.run(debug=True)
