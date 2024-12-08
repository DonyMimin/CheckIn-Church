# CheckIn-Church
## Instalasi
- Jalankan apps .exe CheckIn-Church (dapat didownload dari link gdrive [Apps CheckIn-Church](https://drive.google.com/drive/folders/1Pw5jhF1Z_wOf98aa74XPHRbxdnM5nJDJ?usp=sharing)) yang berlokasi pada:
```
Final_app_exe -> dist -> main -> CheckIn-Church.exe
```
- Jalankan apps .exe CheckIn-Church dengan ``Run as Administrator``

## Clone Repository to run source code
- Clone repository:
```
git clone https://github.com/DonyMimin/DonyMimin-Deteksi-Tempat-Duduk-dan-Pengenalan-Wajah-Yolov8-dan-ResNet50.git
```
- Install all requiremnets library:
```
pip install -r requirements.txt
```
- Run main.py

## Regenerate .exe
- Untuk regenerate .exe baru, clone repository dengan command:
```
  https://github.com/DonyMimin/DonyMimin-Deteksi-Tempat-Duduk-dan-Pengenalan-Wajah-Yolov8-dan-ResNet50
```
- run build command pada Command Prompt pada directory repository yang telah di clone sebelumnya dengan perintah:
```
pyinstaller main.spec
```
- Jika proses build sudah selesai, maka dapat dibuka kembali aplikasi .exe apps CheckIn-Church yang ada pada directory clone repostitory dengan path:
```
Current directory clone -> dist -> main -> CheckIn-Church.exe
```
- Kemudian memasukkan bobot model yang telah ada ``Pada model folder`` pada directory file yang sama dengan aplikasi .exe
- Dapat melihat proses dari train sebelumnya ``Pada train folder`` baik pada model YOLOv8 dan ResNet50 dalam mendapatkan bobot model

Link gDrive:
 [Apps CheckIn-Church](https://drive.google.com/drive/folders/1Pw5jhF1Z_wOf98aa74XPHRbxdnM5nJDJ?usp=sharing)

Panduan Program:
- Dapat dilihat di Manual Book yang dilampirkan `` [Manual Book Program](https://drive.google.com/file/d/1BeJnEGddO0uCph2tlhgFmFX-RStjCSUj/view?usp=sharing)``
