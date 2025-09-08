from flask import Flask, render_template
import os

app = Flask(__name__)

# صفحه اصلی با تایمر
@app.route("/")
def home():
    return render_template("index.html")

# صفحه درباره
@app.route("/about")
def about():
    return render_template("about.html")

# صفحه تایمر تعاملی
@app.route("/timer")
def timer():
    return render_template("timer.html")

# اجرای محلی برای تست
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
