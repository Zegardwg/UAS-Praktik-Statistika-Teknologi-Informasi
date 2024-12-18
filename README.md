Berikut adalah versi **ringkas dokumentasi** dengan tambahan cara **download library Python** dan **setup Flask** agar lebih mudah dimengerti.

---

# **Dashboard Data Sekolah**  
Visualisasi data fasilitas sekolah di Indonesia menggunakan **Flask** dan **Python**.
![Demo](static/gif.gif)
---

## **Library yang Digunakan**  

- **Flask**: Framework untuk membangun aplikasi web Python.  
- **Pandas**: Membaca dan mengolah data CSV.  
- **Seaborn** & **Matplotlib**: Membuat visualisasi data.
  
---

## **Fitur Utama**  
1. **Visualisasi Data**: Grafik menggunakan **Seaborn** dan **Matplotlib**.  
2. **Tabel Data**: Menampilkan data CSV dalam bentuk tabel dengan **Pandas**.  
3. **Desain Responsif**: Menggunakan **Bootstrap 5**.  

---

## **Persyaratan**  

Pastikan Anda sudah menginstal:  
- **Python 3.x**  
- **pip** (Python Package Installer)

---

## **Instalasi**  

### **1. Clone Proyek**  

---

### **2. Install Library Python**  

Jalankan perintah di bawah ini untuk menginstal dependensi:

```bash
pip install Flask pandas seaborn matplotlib
```

Atau jika menggunakan **file `requirements.txt`**:  

```bash
pip install -r requirements.txt
```

---

### **3. Struktur Proyek**  

```
project/
│
├── app.py                 # Flask server
├── data/                  # Dataset CSV
│   ├── internet-facility.csv
│   ├── computer-availability.csv
│   └── drinking-water-availability.csv
├── static/                # Gambar visualisasi
├── templates/             # Template HTML
│   └── index.html
├── requirements.txt       # Python dependencies
└── README.md
```

---

### **4. Jalankan Flask Server**  

Jalankan perintah berikut untuk memulai server Flask:

```bash
python app.py
```

Jika server berjalan, akses **dashboard** di browser pada:  
[http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## **Kode Utama (app.py)**  

```python
from flask import Flask, render_template, url_for
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load Data
def load_data():
    internet_df = pd.read_csv('data/internet-facility.csv')
    computer_df = pd.read_csv('data/computer-availability.csv')
    water_df = pd.read_csv('data/drinking-water-availability.csv')
    return internet_df, computer_df, water_df

# Buat Visualisasi
def create_visualizations():
    # Load data
    internet_df, computer_df, water_df = load_data()

    # Set Seaborn Style
    sns.set_theme(style="whitegrid", palette="pastel")
    if not os.path.exists('static'):
        os.makedirs('static')

    # Contoh Visualisasi: Internet Facility
    plt.figure(figsize=(12, 8))
    sns.barplot(data=internet_df, x='State', y='% of Schools with Internet Facility available - All Management', color='skyblue')
    plt.title('Internet Facility in Schools')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/internet_facility.png')

# Route utama Flask
@app.route("/")
def index():
    create_visualizations()
    internet_df, _, _ = load_data()
    internet_table = internet_df.to_html(classes='table table-striped', index=False)
    return render_template("index.html", internet_table=internet_table, img_path=url_for('static', filename='internet_facility.png'))

if __name__ == "__main__":
    app.run(debug=True)
```

---

## **Tampilan Visualisasi**  
Gambar visualisasi akan disimpan di folder **`/static`** dan ditampilkan di halaman utama melalui file **`index.html`**.

---

## **Cara Download dan Menjalankan**  

1. **Pastikan Flask Terinstal:**  
   Jika belum, install Flask menggunakan `pip`:

   ```bash
   pip install flask
   ```

2. **Install Semua Library Tambahan:**  
   ```bash
   pip install pandas seaborn matplotlib
   ```

3. **Jalankan Proyek:**  
   ```bash
   python app.py
   ```

4. **Akses Dashboard:**  
   Buka browser dan akses [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
---

Sekarang, pengguna dapat dengan cepat menginstal Flask, dependensi Python, dan menjalankan server untuk melihat visualisasi data fasilitas sekolah.
