from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

class ModulBantuan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modul Bantuan")
        self.setFixedSize(1080, 640)
        self.initUI()

    def initUI(self):
        # Layout utama vertikal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(40, 20, 30, 20)  # Padding kiri, atas, kanan, bawah

        # Spacer di atas untuk mendorong konten ke bawah
        top_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum)
        main_layout.addItem(top_spacer)

        # Label judul
        title_label = QLabel("Bantuan")
        title_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title_label)

        # Tambahkan spasi setelah judul
        main_layout.addSpacing(20)

        # Label untuk informasi aplikasi
        info_aplikasi_label = QLabel("Petunjuk penggunaan Aplikasi :")
        info_aplikasi_label.setStyleSheet("font-size: 28px;")
        main_layout.addWidget(info_aplikasi_label)

        # Tambahkan spasi
        main_layout.addSpacing(15)

        title_label = QLabel(
            "1. Pada halaman pertama aplikasi klik tombol 'Deteksi dan Pengenalan' untuk ke halaman Modul \nDeteksi dan Pengenalan.\n"
            "2. Deteksi dan pengenalan dapat dimulai dengan menginput file video atau real-time.\n"
            "3. Input jumlah kursi untuk mendapatkan jumlah dari kursi yang tersisa dengan mengetik jumlah\nkursi yang diinginkan kemudian klik tombol 'Input'.\n"
            "4. Klik tombol 'Stop' untuk memberhentikan video atau kamera yang sedang berjalan.")
        title_label.setStyleSheet("font-size: 22px;")
        title_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(title_label)

        # Tambahkan spasi
        main_layout.addSpacing(15)

        title_label = QLabel("Untuk Informasi dari Aplikasi dan Pengembang dapat dilihat Pada Modul Tentang Sistem")
        title_label.setStyleSheet("font-size: 22px;")
        title_label.setAlignment(Qt.AlignLeft)
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