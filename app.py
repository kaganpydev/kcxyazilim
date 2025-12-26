from flask import Flask, render_template, send_from_directory, request, redirect
import os

app = Flask(__name__)


@app.before_request
def force_https():
    if request.headers.get("X-Forwarded-Proto") == "http":
        return redirect(request.url.replace("http://", "https://"), code=301)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/yazilim')
def yazilim():
    return render_template("yazilim.html")

@app.route('/akademi')
def akademi():
    return render_template("akademi.html")

@app.route('/hakkimizda')
def hakkimizda():
    return render_template("hakkimizda.html")

@app.route('/akademi/cocuk-python')
def cocuk_python():
    return render_template("cocuk-python.html")

@app.route('/akademi/yetiskin-python')
def yetiskin_python():
    return render_template("yetiskin-python.html")


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.root_path, 'sitemap.xml', mimetype='application/xml')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt', mimetype='text/plain')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

if __name__ == "__main__":
    app.run()





