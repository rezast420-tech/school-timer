from flask import Flask, render_template_string
import os

# ایجاد اپلیکیشن Flask
app = Flask(__name__)

# مسیر اصلی
@app.route("/")
def home():
    html_content = """
    <html>
        <head>
            <title>اپلیکیشن Render</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { color: #2c3e50; }
                a { text-decoration: none; color: #2980b9; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>سلام! اپلیکیشن شما روی Render اجرا شد 🎉</h1>
            <p>برای اطلاعات بیشتر <a href="/about">اینجا کلیک کنید</a></p>
        </body>
    </html>
    """
    return render_template_string(html_content)

# مسیر about نمونه
@app.route("/about")
def about():
    html_content = """
    <html>
        <head>
            <title>درباره ما</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                h1 { color: #16a085; }
                a { text-decoration: none; color: #2980b9; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>درباره اپلیکیشن</h1>
            <p>این اپلیکیشن با Flask و روی Render.com اجرا شده است.</p>
            <p><a href="/">بازگشت به صفحه اصلی</a></p>
        </body>
    </html>
    """
    return render_template_string(html_content)

# اجرای اپلیکیشن
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # پورت Render
    app.run(host="0.0.0.0", port=port, debug=True)
