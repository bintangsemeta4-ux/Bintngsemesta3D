# Bintang Semesta 3D — Android WebView project

Paket ini adalah **proyek sumber Android untuk membangun APK**, bukan file APK yang sudah dikompilasi.

## Cara termudah menghasilkan APK
1. Buat repositori GitHub baru.
2. Ekstrak ZIP ini, lalu unggah seluruh isi folder proyek ke repositori (termasuk folder `.github/workflows`).
3. Buka tab **Actions** di repositori GitHub.
4. Jalankan workflow **Build Bintang Semesta APK** (atau push ke branch `main`).
5. Setelah workflow selesai, buka hasil run → bagian **Artifacts** → unduh `BintangSemesta3D-debug-apk.zip`.
6. Ekstrak ZIP artifact dan pasang `app-debug.apk` di Android. Jika diminta, izinkan pemasangan dari sumber tersebut.

## Catatan
- Aplikasi memakai WebView untuk menampilkan editor yang sudah ada.
- Three.js dimuat dari CDN, jadi koneksi internet dibutuhkan untuk tampilan 3D.
- Ini APK debug untuk uji coba, bukan rilis Play Store.
- Periksa semua ukuran dan estimasi secara mandiri; ini prototipe konsep, bukan gambar kerja konstruksi.
