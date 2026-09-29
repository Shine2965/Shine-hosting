from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    data_user = None
    jenis_bangun = request.form.get("jenis_bangun")

    if request.method == "POST":
        # Mengambil data profil singkat
        nama = request.form.get("nama")
        alamat = request.form.get("alamat")
        data_user = f"Halo, {nama}, alamat kamu di {alamat}..."

        # Menghitung Luas Segitiga
        if jenis_bangun == "segitiga":
            try:
                alas = float(request.form.get("alas", 0))
                tinggi = float(request.form.get("tinggi", 0))
                luas = 0.5 * alas * tinggi
                hasil = f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah: {luas} cm²"
            except ValueError:
                hasil = "Masukkan angka yang valid untuk alas dan tinggi!"

        # Menghitung Luas Persegi
        elif jenis_bangun == "persegi":
            try:
                sisi = float(request.form.get("sisi", 0))
                luas = sisi * sisi
                hasil = f"Luas persegi dengan sisi {sisi} cm adalah: {luas} cm²"
            except ValueError:
                hasil = "Masukkan angka yang valid untuk sisi!"

    return render_template("index.html", hasil=hasil, data_user=data_user, jenis_bangun=jenis_bangun)

# Diperlukan untuk Vercel serverless function
app.debug = True
