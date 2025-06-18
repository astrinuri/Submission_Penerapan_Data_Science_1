# Proyek Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di seluruh negeri. Walaupun telah berkembang pesat, perusahaan menghadapi tantangan signifikan dalam mengelola karyawan, terutama tingginya **attrition rate** atau tingkat keluar karyawan. Dengan angka attrition yang melebihi **10%**, perusahaan mulai merasakan dampak negatif seperti:
- **Biaya Rekrutmen Tinggi**: Berdasarkan karakteristik perusahaan yang memiliki lebih dari 1.000 karyawan, biaya yang dikeluarkan untuk proses rekrutmen dan pelatihan karyawan baru meningkat seiring tingginya angka pergantian karyawan. Hal ini mencakup biaya iklan lowongan kerja, seleksi, onboarding, dan pelatihan.
- **Penurunan Produktivitas**: Tingginya pergantian karyawan menyebabkan hilangnya pengalaman dan keterampilan yang dibutuhkan untuk mencapai target bisnis. Data dalam dataset seperti **YearsAtCompany** dan **YearsWithCurrManager** dapat membantu mengukur kontribusi pengalaman terhadap produktivitas.
- **Penurunan Kepuasan Karyawan**: Indikator kepuasan seperti **Job Satisfaction**, **Work-Life Balance**, dan **Environment Satisfaction** dalam dataset menunjukkan pentingnya mengidentifikasi ketidakpuasan lebih awal untuk mencegah gelombang keluar karyawan.

Manajemen HR di Jaya Jaya Maju menyadari pentingnya memahami faktor-faktor penyebab attrition agar dapat menyusun strategi yang tepat untuk **meningkatkan retensi karyawan** dan **mengurangi attrition rate** secara signifikan.

### Permasalahan Bisnis
Permasalahan bisnis yang akan diselesaikan melalui proyek ini adalah:
1. **Mengidentifikasi faktor-faktor utama yang mempengaruhi attrition rate** di perusahaan, baik dari segi demografis, kepuasan kerja, maupun metrik finansial.
2. **Mengukur tingkat kepuasan karyawan** berdasarkan parameter seperti **Job Satisfaction**, **Work-Life Balance**, dan **Environment Satisfaction**.
3. **Menentukan pola perilaku karyawan yang cenderung keluar**, seperti pengaruh jarak rumah ke kantor, lembur berlebihan (OverTime), dan pendapatan karyawan.
4. **Menyediakan alat bantu berupa business dashboard** yang memudahkan manajemen HR memantau dan menganalisis faktor-faktor penyebab attrition secara berkala.

Dengan menyelesaikan permasalahan ini, perusahaan diharapkan dapat:
- Mengurangi **attrition rate** dengan mengambil langkah pencegahan yang tepat.
- Menyusun program retensi yang lebih efektif.
- Meningkatkan kepuasan kerja dan produktivitas karyawan.

### Cakupan Proyek
Proyek ini mencakup:
1. **Eksplorasi dan Pemahaman Data**: Analisis dataset `employee_data.csv` untuk memahami karakteristik karyawan dan distribusi attrition.
2. **Data Preparation**: Membersihkan dan memproses data agar siap digunakan untuk analisis lebih lanjut.
3. **Analisis Faktor Penyebab Attrition**:
   - Analisis korelasi antara variabel seperti pendapatan, lembur, tingkat kepuasan, dan jarak rumah.
   - Visualisasi tren dan pola attrition di berbagai departemen, level pekerjaan, dan usia karyawan.
4. **Pembuatan Business Dashboard**: Visualisasi data dalam bentuk dashboard yang mudah dipahami untuk memantau faktor penyebab attrition.
5. **Kesimpulan dan Rekomendasi**: Menarik kesimpulan dari hasil analisis dan memberikan rekomendasi praktis untuk mengurangi attrition.

### Persiapan
**Sumber data**: Dataset yang digunakan dalam proyek ini adalah [Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) sesuai dengan instruksi dari submission proyek ini.
**Setup environment**:
Proyek ini membutuhkan lingkungan sederhana untuk menjalankan analisis data dan dashboard. Berikut langkah-langkah untuk mempersiapkan environment:
1. Menjalankan `notebook.ipynb`
   - Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file `requirements.txt` untuk melihat dependensi yang dibutuhkan).
   - Jalankan seluruh isi file `notebook.ipynb` menggunakan Google Colab/Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.
2. **Menjalankan Dashboard**:
   Untuk melihat isi dashboard secara langsung, dapat diakses pada tableau public berikut : https://public.tableau.com/views/Book1_17502283530910/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
3. **Menjalankan Aplikasi Streamlit Secara Lokal**
Untuk menjalankan aplikasi ini secara lokal, ikuti langkah-langkah berikut:

a. **Clone repositori ini** (jika belum):

   ```bash
   git clone https://github.com/astrinuri/Submission_Penerapan_Data_Science_1.git
   ```
b. Install semua dependencies
c. Pastikan file model rf_model.joblib ada di direktori yang sama dengan app.py
d. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```




---

## 📊 Business Dashboard

Hasil dari analisis dan model prediktif dapat divisualisasikan dalam bentuk dashboard untuk membantu tim HR memantau dan memahami attrition secara real-time. Berikut adalah elemen-elemen yang ditampilkan dalam dashboard **Jaya Jaya Maju Employees Dashboard**:

### 1. Distribusi Gender
Visualisasi pie chart yang menunjukkan jumlah karyawan berdasarkan jenis kelamin. Mayoritas karyawan adalah laki-laki (sekitar 59%), dan sisanya perempuan.

### 2. Status Pernikahan (Marital Status)
Pie chart ini menampilkan komposisi status pernikahan karyawan (Married, Single, Divorced). Diketahui bahwa karyawan yang sudah menikah merupakan kelompok terbesar.

### 3. Attrition (Tingkat Pengunduran Diri)
Bar chart yang memperlihatkan jumlah karyawan yang tetap bekerja (No Attrition) jauh lebih besar dibandingkan yang resign (Yes Attrition).

### 4. Work-Life Balance vs Attrition
Bubble chart digunakan untuk menggambarkan hubungan antara work-life balance dan attrition. Mayoritas karyawan memiliki work-life balance yang "High", namun attrition lebih tinggi pada kategori "Medium" dan "Low".

### 5. Attrition Berdasarkan Status Pernikahan
Visualisasi ini menunjukkan bahwa karyawan single paling banyak mengalami attrition

### 6. Attrition Berdasarkan Job Role
Bar chart horizontal menggambarkan attrition berdasarkan jenis pekerjaan. Jabatan seperti **Sales Executive** dan **Research Scientist** menjadi kontributor utama terhadap attrition, baik dari sisi jumlah maupun proporsi.

---

🔗 **Lihat langsung di Tableau Public**:  
https://public.tableau.com/views/Book1_17502283530910/Dashboard1?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

# **Conclusion**
Proyek ini bertujuan untuk memahami faktor-faktor yang memengaruhi tingkat **attrition** (keluar) karyawan di perusahaan **Jaya Jaya Maju** dan membangun model prediktif untuk mengidentifikasi karyawan dengan risiko keluar tinggi. Berikut adalah temuan utama dan insight yang diperoleh:

#### **1. Faktor-Faktor Penyebab Attrition**
Berdasarkan analisis data dan model prediktif, berikut adalah faktor utama yang memengaruhi attrition:
1. **OverTime**:
   - Karyawan yang sering lembur (**OverTime = Yes**) memiliki risiko keluar yang jauh lebih tinggi dibandingkan yang tidak lembur.
   - Fitur ini adalah prediktor terkuat dalam model prediktif.
2. **MonthlyIncome**:
   - Pendapatan bulanan yang lebih rendah meningkatkan risiko keluar karyawan.
   - Fitur ini mencerminkan pentingnya kepuasan finansial dalam retensi karyawan.
3. **YearsAtCompany dan TotalWorkingYears**:
   - Masa kerja pendek baik di perusahaan maupun secara total adalah indikator risiko tinggi.
4. **Fitur Pendukung Lain**:
   - Fitur seperti **DistanceFromHome** dan **Age** memiliki kontribusi kecil, tetapi tetap relevan dalam memahami pola attrition.

#### **2. Model Prediktif Terbaik**
Model terbaik yang digunakan dalam proyek ini adalah **Random Forest**, dengan metrik performa sebagai berikut:
- **Accuracy**: 84.91%
- **Precision**: 83.44%
- **Recall**: 84.91%
- **F1-Score**: 83.89%
Model ini menunjukkan performa superior dibandingkan model lainnya seperti Logistic Regression, Random Forest, dan SVM.

#### **3. Feature Importance**
Dari analisis feature importance menggunakan model Random Forest :
- **TotalWorkingYears** adalah fitur dengan kontribusi terbesar terhadap prediksi.
- **YearsAtCompany** dan **Age** juga memiliki peran penting.

---

### **Jawaban terhadap Pertanyaan Bisnis**
1. **Apa faktor utama yang memengaruhi attrition?**
   - Faktor utama adalah **OverTime**, **MonthlyIncome**, dan **YearsAtCompany**.
2. **Bagaimana tingkat kepuasan karyawan memengaruhi attrition?**
   - Fitur seperti **JobSatisfaction** tidak signifikan dalam model prediktif, tetapi tetap relevan secara deskriptif.
3. **Apa pola perilaku karyawan dengan risiko keluar tinggi?**
   - Karyawan yang lembur berlebihan, memiliki pendapatan rendah, dan masa kerja pendek cenderung memiliki risiko tinggi.
4. **Apakah kita memiliki alat bantu untuk memantau attrition?**
   - Model prediktif dan visualisasi hasil dapat digunakan untuk membangun dashboard interaktif untuk monitoring risiko.

---

### **Karakteristik Umum Karyawan yang Melakukan Attrition**
Berdasarkan analisis data, berikut adalah karakteristik umum karyawan yang melakukan attrition:
1. **Demografis**:
  - **Usia**: Rata-rata usia karyawan yang keluar adalah 30-an tahun.
  - **Jenis Kelamin**: Mayoritas adalah pria (Male).
  - **Status Pernikahan**: Sebagian besar karyawan yang keluar adalah Single, diikuti oleh Married.
2. **Pekerjaan dan Departemen**:
  - **Peran Kerja**: Posisi yang paling sering melakukan attrition adalah Laboratory Technician.
  - **Departemen**: Departemen **Research & Development** memiliki tingkat attrition tertinggi.
3. **Faktor Finansial dan Beban Kerja**:
  - **Pendapatan**: Rata-rata pendapatan bulanan karyawan yang keluar adalah 4,872.
  - **Lembur (OverTime)**: Sebagian besar karyawan yang keluar bekerja lembur secara signifikan.
4. **Kepuasan dan Keseimbangan**:
  - **Kepuasan Kerja**: Rata-rata tingkat kepuasan kerja adalah **2.5** (Medium).
  - **Keseimbangan Kerja-Hidup**: Rata-rata berada di tingkat **2.67** (Moderate).
5. **Masa Kerja**:
  - **Masa Kerja di Perusahaan**: Rata-rata masa kerja adalah **5 tahun**, dengan beberapa karyawan memiliki masa kerja sangat panjang hingga 40 tahun.

---

### **Rekomendasi Action Items untuk Perusahaan**
1. **Kurangi Lembur Berlebihan**:
   - Berikan program kerja fleksibel untuk meningkatkan keseimbangan kerja-hidup.
2. **Kaji Skala Gaji**:
   - Sesuaikan gaji karyawan agar kompetitif di pasar dan berikan insentif tambahan.
3. **Perkuat Retensi Karyawan Baru**:
   - Implementasikan program onboarding dan mentoring untuk karyawan dengan masa kerja pendek.
4. Mengidentifikasi karyawan dengan YearsAtCompany dan TotalWorkingYears yang pendek, lalu memberikan perhatian khusus terhadap pengembangan karier dan kepuasan mereka.
5. Menciptakan lingkungan kerja yang lebih inklusif dan mendukung bagi karyawan dari berbagai kelompok usia.
6. **Gunakan Model Prediktif**:
   - Integrasikan model Random Forest untuk memonitor risiko secara real-time melalui dashboard HR.

