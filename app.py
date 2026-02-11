from flask import Flask, render_template, Response, send_from_directory

app = Flask(__name__)


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

@app.route('/egitmenler')
def egitmenler():
    egitmenler = [
        {
            "slug": "kagan-cem-kayaci",
            "ad": "Kağan Cem Kayacı",
            "unvan": "Python Eğitmeni"
        }
    ]
    return render_template("egitmenler.html", egitmenler=egitmenler)


@app.route('/egitmen/<slug>')
def egitmen_detay(slug):
    if slug == "kagan-cem-kayaci":
        egitmen = {
            "ad": "Kağan Cem Kayacı",
            "unvan": "Python Eğitmeni",
            "hakkinda": """
            Python alanında birebir ve grup eğitimleri veren,
            başlangıç ve orta seviye öğrencileri gerçek projelerle
            yazılım dünyasına hazırlayan eğitmendir.
            """,
            "sertifikalar": ["Millî Eğitim Bakanlığı (MEB) onaylı, resmî Python Eğitimi Sertifikası",
    "Yıldız Teknik Üniversitesi tarafından sunulan kapsamlı Python Eğitimi Sertifikası",
    "Boğaziçi Enstitüsü – Uygulamalı ve İleri Düzey Python Eğitimi Sertifikası"]
        }
        return render_template("egitmen_detay.html", egitmen=egitmen)

    return "Eğitmen bulunamadı", 404


@app.route("/kilis-yazilim-python-kursu-egitimi")
def kilis_python_kursu():
    return render_template("kilis_python.html")

from flask import redirect

@app.route("/kilis-python-kursu")
def eski_link():
    return redirect("/kilis-yazilim-python-kursu-egitimi", code=301)

if __name__ == "__main__":
    app.run(debug=True)

