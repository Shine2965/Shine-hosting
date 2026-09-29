from flask import Flask, request, render_template_string

app = Flask(__name__)

# Menyisipkan HTML langsung sebagai string di dalam kode Python
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Program Multi-Hitung Web</title>
    <style>
        body { font-family: 'Courier New', Courier, monospace; background: #121212; color: #00ff00; padding: 20px; max-width: 600px; margin: 0 auto; }
        .box { border: 1px solid #00ff00; padding: 20px; border-radius: 5px; background: #1a1a1a; margin-bottom: 20px; }
        input, select, button { background: #222; color: #00ff00; border: 1px solid #00ff00; padding: 8px; margin: 5px 0; width: 100%; box-sizing: border-box; }
        button { cursor: pointer; font-weight: bold; }
        button:hover { background: #00ff00; color: #000; }
        .hidden { display: none; }
        .animasi-teks { border-right: 2px solid #00ff00; white-space: nowrap; overflow: hidden; animation: typing 2s steps(40, end), blink .75s step-end infinite; }
        @keyframes typing { from { width: 0 } to { width: 100% } }
        @keyframes blink { from, to { border-color: transparent } 50% { border-color: #00ff00 } }
    </style>
</head>
<body>

    <div class="box">
        <h2>=== SELAMAT DATANG DI PROGRAM MULTI-HITUNG WEB 🗿 ===</h2>
        
        <form method="POST">
            <label>Nama Anda:</label>
            <input type="text" name="nama" required value="{{ nama }}">
            
            <label>Tester :D :</label>
            <input type="text" name="alamat" required value="{{ alamat }}">

            <label>Pilih Bangun Datar:</label>
            <select name="jenis_bangun" id="jenis_bangun" onchange="toggleForm()">
                <option value="segitiga" {% if jenis_bangun == 'segitiga' %}selected{% endif %}>Hitung Luas Segitiga (▲)</option>
                <option value="persegi" {% if jenis_bangun == 'persegi' %}selected{% endif %}>Hitung Luas Persegi (■)</option>
            </select>

            <!-- Form Segitiga -->
            <div id="form-segitiga">
                <p style="text-align:center;">▲<br>/ \<br>/___\</p>
                <label>Masukkan panjang alas (cm):</label>
                <input type="number" step="any" name="alas" value="{{ alas }}">
                <label>Masukkan tinggi segitiga (cm):</label>
                <input type="number" step="any" name="tinggi" value="{{ tinggi }}">
            </div>

            <!-- Form Persegi -->
            <div id="form-persegi" class="hidden">
                <p style="text-align:center;">+---+<br>| &nbsp; |<br>+---+</p>
                <label>Masukkan panjang sisi (cm):</label>
                <input type="number" step="any" name="sisi" value="{{ sisi }}">
            </div>

            <button type="submit">HITUNG SEKARANG</button>
        </form>
    </div>

    {% if hasil %}
    <div class="box">
        <h3 class="animasi-teks">{{ data_user }}</h3>
        <p>{{ hasil }}</p>
        <p>Terima kasih telah menggunakan program ini! 🗿</p>
    </div>
    {% endif %}

    <script>
        function toggleForm() {
            var pilihan = document.getElementById("jenis_bangun").value;
            if (pilihan === "segitiga") {
                document.getElementById("form-segitiga").classList.remove("hidden");
                document.getElementById("form-persegi").classList.add("hidden");
            } else {
                document.getElementById("form-segitiga").classList.add("hidden");
                document.getElementById("form-persegi").classList.remove("hidden");
            }
        }
        window.onload = toggleForm;
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    data_user = ""
    jenis_bangun = "segitiga"
    nama = ""
    alamat = ""
    alas = ""
    tinggi = ""
    sisi = ""

    if request.method == "POST":
        nama = request.form.get("nama", "")
        alamat = request.form.get("alamat", "")
        jenis_bangun = request.form.get("jenis_bangun", "segitiga")
        data_user = f"Halo, {nama}, alamat kamu di {alamat}..."

        if jenis_bangun == "segitiga":
            try:
                alas = request.form.get("alas", "")
                tinggi = request.form.get("tinggi", "")
                luas = 0.5 * float(alas) * float(tinggi)
                hasil = f"Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah: {luas} cm²"
            except ValueError:
                hasil = "Masukkan angka yang valid untuk alas dan tinggi!"

        elif jenis_bangun == "persegi":
            try:
                sisi = request.form.get("sisi", "")
                luas = float(sisi) * float(sisi)
                hasil = f"Luas persegi dengan sisi {sisi} cm adalah: {luas} cm²"
            except ValueError:
                hasil = "Masukkan angka yang valid untuk sisi!"

    return render_template_string(
        HTML_TEMPLATE, 
        hasil=hasil, data_user=data_user, jenis_bangun=jenis_bangun,
        nama=nama, alamat=alamat, alas=alas, tinggi=tinggi, sisi=sisi
    )

# Diperlukan untuk Vercel serverless function
app.debug = True
