from flask import Flask, render_template, url_for
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Fungsi untuk membaca dataset dari folder data
def load_data():
    internet_df = pd.read_csv('data/internet-facility.csv')
    computer_df = pd.read_csv('data/computer-availability.csv')
    water_df = pd.read_csv('data/drinking-water-availability.csv')
    return internet_df, computer_df, water_df

# Fungsi untuk membuat visualisasi dan menyimpan gambar di folder static
def create_visualizations():
    # Load data
    internet_df, computer_df, water_df = load_data()

    # Set style untuk Seaborn
    sns.set_theme(style="whitegrid", palette="pastel")

    # Pastikan folder static ada
    if not os.path.exists('static'):
        os.makedirs('static')

    # Visualisasi Internet Facility
    if 'State' in internet_df.columns and '% of Schools with Internet Facility available - All Management' in internet_df.columns:
        # Bar Plot
        plt.figure(figsize=(12, 8))
        sns.barplot(data=internet_df, x='State', y='% of Schools with Internet Facility available - All Management', color='skyblue')
        plt.title('% Sekolah dengan Fasilitas Internet - Bar Plot', fontsize=14)
        plt.xlabel('Provinsi', fontsize=12)
        plt.ylabel('Persentase', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.savefig('static/internet_facility_bar.png')

        # Line Plot
        plt.figure(figsize=(12, 8))
        sns.lineplot(data=internet_df, x='State', y='% of Schools with Internet Facility available - All Management', marker='o', color='blue')
        plt.title('% Sekolah dengan Fasilitas Internet - Line Plot', fontsize=14)
        plt.xlabel('Provinsi', fontsize=12)
        plt.ylabel('Persentase', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.savefig('static/internet_facility_line.png')

    # Visualisasi Computer Facility
    if 'State' in computer_df.columns and '% of Schools with Computer Facility - All Management' in computer_df.columns:
        # Bar Plot
        plt.figure(figsize=(12, 8))
        sns.barplot(data=computer_df, x='State', y='% of Schools with Computer Facility - All Management', color='orange')
        plt.title('% Sekolah dengan Fasilitas Komputer - Bar Plot', fontsize=14)
        plt.xlabel('Provinsi', fontsize=12)
        plt.ylabel('Persentase', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.savefig('static/computer_facility_bar.png')

        # Histogram
        plt.figure(figsize=(12, 8))
        sns.histplot(data=computer_df, x='% of Schools with Computer Facility - All Management', bins=10, kde=True, color='orange')
        plt.title('% Sekolah dengan Fasilitas Komputer - Histogram', fontsize=14)
        plt.xlabel('Persentase', fontsize=12)
        plt.ylabel('Frekuensi', fontsize=12)
        plt.tight_layout()
        plt.savefig('static/computer_facility_hist.png')

    # Visualisasi Drinking Water Availability
    if 'State' in water_df.columns and '% of Schools having Drinking Water Facility within School Premises' in water_df.columns:
        # Scatter Plot
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=water_df, x='State', y='% of Schools having Drinking Water Facility within School Premises', color='green', s=100)
        plt.title('% Sekolah dengan Fasilitas Air Minum - Scatter Plot', fontsize=14)
        plt.xlabel('Provinsi', fontsize=12)
        plt.ylabel('Persentase', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.savefig('static/drinking_water_scatter.png')

        # Line Plot
        plt.figure(figsize=(12, 8))
        sns.lineplot(data=water_df, x='State', y='% of Schools having Drinking Water Facility within School Premises', marker='o', color='green')
        plt.title('% Sekolah dengan Fasilitas Air Minum - Line Plot', fontsize=14)
        plt.xlabel('Provinsi', fontsize=12)
        plt.ylabel('Persentase', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.savefig('static/drinking_water_line.png')

    plt.close('all')

# Route utama untuk menampilkan data dan visualisasi
@app.route("/")
def index():
    # Load data
    internet_df, computer_df, water_df = load_data()

    # Buat visualisasi
    create_visualizations()

    # Konversi DataFrame ke tabel HTML
    internet_table = internet_df.to_html(classes='table table-striped', index=False)
    computer_table = computer_df.to_html(classes='table table-striped', index=False)
    water_table = water_df.to_html(classes='table table-striped', index=False)

    # Render template dan kirim data ke HTML
    return render_template("index.html",
                           internet_table=internet_table,
                           computer_table=computer_table,
                           water_table=water_table,
                           internet_bar=url_for('static', filename='internet_facility_bar.png'),
                           internet_line=url_for('static', filename='internet_facility_line.png'),
                           computer_bar=url_for('static', filename='computer_facility_bar.png'),
                           computer_hist=url_for('static', filename='computer_facility_hist.png'),
                           water_scatter=url_for('static', filename='drinking_water_scatter.png'),
                           water_line=url_for('static', filename='drinking_water_line.png'))

if __name__ == "__main__":
    app.run(debug=True)
