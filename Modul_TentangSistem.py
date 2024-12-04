from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class ModulTentangSistem(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modul Tentang Sistem")
        self.setFixedSize(1080, 640)
        self.initUI()

    def initUI(self):
        # Layout utama vertikal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 20, 30, 20)  # Padding kiri, atas, kanan, bawah

        # Spacer di atas untuk mendorong konten ke bawah
        top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum)
        main_layout.addItem(top_spacer)

        # Label judul
        title_label = QLabel("Tentang Sistem")
        title_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Tambahkan spasi setelah judul
        main_layout.addSpacing(35)

        title_label = QLabel("Aplikasi mengenai deteksi tempat duduk dan pengenalan wajah di tempat ibadah Gereja.\nAplikasi ini berfungsi untuk menghitung jumlah tempat duduk yang tersisa \ndan mengenali dari wajah yang terdeteksi\nmelalui sudut pandang rekaman kamera.")
        title_label.setStyleSheet("font-size: 22px;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Tambahkan spasi
        main_layout.addSpacing(20)

        title_label = QLabel("Dibuat oleh Dony\nPembimbing CHAIRISNI LUBIS, Dra., M.Kom.")
        title_label.setStyleSheet("font-size: 22px;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Tambahkan spasi
        main_layout.addSpacing(20)

        title_label = QLabel("Program Studi Teknik Informatika\nUniversitas Tarumanagara\n©2024")
        title_label.setStyleSheet("font-size: 22px;")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Spacer untuk mendorong konten ke atas
        main_layout.addStretch()

        # Layout horizontal untuk tombol kembali
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Spacer untuk mendorong tombol ke kanan

        # Tombol kembali
        back_button = QPushButton("Kembali")
        back_button.setStyleSheet("""
            font-size: 15px;
            background-color: #76BA99; 
            color: white; 
            font-weight: bold;
            border-radius: 15px;  /* Atur sudut tombol agar sedikit bulat */
        """)
        back_button.setFixedSize(100, 40)  # Set ukuran tombol
        back_button.clicked.connect(self.open_modul_halaman_utama)  # Tombol kembali ke halaman utama
        button_layout.addWidget(back_button, alignment=Qt.AlignRight)

        # Tambahkan layout tombol ke layout utama
        main_layout.addLayout(button_layout)

        # Atur layout ke widget utama
        self.setLayout(main_layout)

    def open_modul_halaman_utama(self):
        # Impor dilakukan di sini untuk menghindari circular import
        from Modul_HalamanUtama import HomePage
        
        # Membuka halaman utama
        self.modul_halaman_utama_window = HomePage()
        self.modul_halaman_utama_window.show()
        self.close()
