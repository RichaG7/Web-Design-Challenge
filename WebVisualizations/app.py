from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
    data = pd.read_csv('cities.csv')
    return render_template("data.html",table=data.to_html())

if __name__ == "__main__":
    app.run(debug=True)