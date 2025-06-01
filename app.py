from flask import Flask, render_template, request
from recommendation import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    movie = ""
    if request.method == "POST":
        movie = request.form["movie"]
        recommendations = get_recommendations(movie)
    return render_template("index.html", movie=movie, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
