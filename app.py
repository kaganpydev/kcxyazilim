from flask import Flask, render_template

app = Flask(__name__)

# ==========================
# ANA SAYFALAR
# ==========================
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


# ==========================
# ALT SAYFALAR (EĞİTİM ATÖLYESİ ALTINDA)
# ==========================
@app.route('/akademi/cocuk-python')
def cocuk_python():
    return render_template("cocuk-python.html")

@app.route('/akademi/yetiskin-python')
def yetiskin_python():
    return render_template("yetiskin-python.html")


if __name__ == "__main__":
    app.run(debug=True)
