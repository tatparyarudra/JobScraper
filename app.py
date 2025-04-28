from flask import Flask, render_template, request
from scraper import scrape_remoteok

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []
    if request.method == "POST":
        keyword = request.form.get("keyword")
        jobs = scrape_remoteok(keyword)
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
