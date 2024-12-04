import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from Modul_TentangSistem import ModulTentangSistem
from Modul_Bantuan import ModulBantuan
from Modul_DeteksidanPengenalan import ModulDeteksidanPengenalan

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.setFixedSize(1080, 640)
        self.initUI()

    def initUI(self):
        # Set layout utama
        layout = QVBoxLayout()

        # Spacer di atas untuk mendorong konten ke tengah
        top_spacer = QSpacerItem(20, 80, QSizePolicy.Minimum)
        layout.addItem(top_spacer)

       # Label Judul
        title_label = QLabel("Deteksi Tempat Duduk dan Pengenalan Wajah")
        title_label.setStyleSheet("font-size: 32px; font-weight: bold;")  # Make the text bold
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Spacer di bawah judul
        layout.addSpacing(40)

        # Frame untuk button "Modul Deteksi dan Pengenalan" agar bisa dirata tengah
        button1_frame = QHBoxLayout()
        # Tombol Modul Deteksi dan Pengenalan
        button1 = QPushButton("Modul Deteksi dan Pengenalan")
        self.set_button_style(button1)  # Set ukuran tombol
        button1.clicked.connect(self.open_modul_deteksi_dan_pengenalan)
        button1_frame.addWidget(button1, alignment=Qt.AlignCenter)  # Tambahkan tombol ke frame dan rata tengah
        layout.addLayout(button1_frame)  # Tambahkan frame ke layout utama

        # Spacer ke bawah 
        layout.addSpacing(40)

        # Frame untuk menempatkan dua tombol secara horizontal
        button_frame = QHBoxLayout()
        # Tombol Modul Tentang Sistem
        button2 = QPushButton("Modul Tentang Sistem")
        self.set_button_style(button2)  # Set ukuran tombol
        button2.clicked.connect(self.open_modul_tentang_sistem)
        button_frame.addWidget(button2)

        # Spacer di antara button2 dan button3
        button_spacer = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        button_frame.addItem(button_spacer)  # Add spacer to create space

        # Tombol Modul Bantuan
        button3 = QPushButton("Modul Bantuan")
        self.set_button_style(button3)  # Set ukuran tombol
        button3.clicked.connect(self.open_modul_bantuan)
        button_frame.addWidget(button3)

        # Tambahkan frame ke layout utama dan rata tengah
        button_frame_container = QWidget()
        button_frame_container.setLayout(button_frame)
        layout.addWidget(button_frame_container, alignment=Qt.AlignCenter)

        # Spacer di bawah untuk mendorong konten ke tengah
        bottom_spacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(bottom_spacer)

        # Atur layout utama ke widget pusat
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # style button
    def set_button_style(self, button):
        button.setStyleSheet("""
            font-size: 22px; 
            padding: 20px; 
            background-color: #76BA99; 
            color: white; 
            font-weight: bold;
            border-radius: 15px;  /* Atur sudut tombol agar sedikit bulat */
        """)
        button.setFixedSize(QSize(400, 120))  # Set ukuran tombol yang sama untuk semua tombol

    def open_modul_tentang_sistem(self):
        # Membuka halaman Modul Tentang Sistem
        self.modul_tentang_sistem_window = ModulTentangSistem()  # Buat instance baru dari ModulTentangSistem
        self.modul_tentang_sistem_window.show()  # Tampilkan jendela baru
        self.close()  # Tutup HomePage saat modul lain dibuka

    def open_modul_bantuan(self):
        # Membuka halaman Modul Bantuan
        self.modul_bantuan_window = ModulBantuan()  # Buat instance baru dari ModulBantuan
        self.modul_bantuan_window.show()  # Tampilkan jendela baru
        self.close()  # Tutup HomePage saat modul lain dibuka
    
    def open_modul_deteksi_dan_pengenalan(self):
        # Membuka halaman Modul Deteksi dan Pengenalan
        self.modul_deteksi_dan_pengenalan_window = ModulDeteksidanPengenalan()  # Buat instance baru dari ModulDeteksidanPengenalan
        self.modul_deteksi_dan_pengenalan_window.show()  # Tampilkan jendela baru
        self.close()  # Tutup HomePage saat modul lain dibuka


# Jalankan aplikasi
def start_app():
    app = QApplication(sys.argv)
    home_window = HomePage()
    home_window.show()
    sys.exit(app.exec_())
