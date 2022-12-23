from flask import Blueprint, render_template, request, redirect, Flask
import generator
app = Flask(__name__, template_folder='templates',static_folder='static')  

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/analyze", methods=['POST'])
def analyze():
    character1 = str(request.form['word'])
    num = request.form['accuracy']
    key = int(num)
    

    choice = request.form['choices']
    if choice == "one":
        text = generator.one_tg(key, character1)
    else:
        count = request.form['count']
        word_count = int(count)
        text = generator.two_tg(key, character1, word_count)
    
    return render_template("index.html", text=text)

if __name__=='__main__':
   app.run(debug=True)