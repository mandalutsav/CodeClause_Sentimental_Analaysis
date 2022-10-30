from flask import Flask, render_template

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
app=Flask(__name__)
run_with_ngrok(main)

@app.route('/',methods=["GET", "POST"])
def main():
    if request.method =="POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score=sid.polarity_scores(inp)
        if score["neg"] !=0:
            return render_template('home.html', message="Negative😞😞")
        else:
            return render_template('home.html', message="Positive😀😀")
            
    return render_template('home.html')