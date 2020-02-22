from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def scatterwords_index():
    return render_template('index.html', template_folder='slick')

if __name__ == "main":
    app.run(debug=True)