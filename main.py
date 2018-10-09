from sentimentClassify import predict_sentiment
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method=="POST":
        text = request.form["text"]
        pred = predict_sentiment(text)
        return render_template('main.html', after_srch=True, pred=pred, text=text)
    return render_template('main.html', after_srch=False)

app.config['TEMPLATES_AUTO_RELOAD']=True
app.run(debug=True)
