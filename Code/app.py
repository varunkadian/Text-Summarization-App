from flask import Flask, render_template, request
import nltk
from newspaper import Article
app = Flask(__name__)

def summarize(url):
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()
    authors = article.authors
    date = article.publish_date
    data = article.text
    summary = article.summary
    return summary

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        url_content = summarize(url)
        return render_template("main.html",value=url_content)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)