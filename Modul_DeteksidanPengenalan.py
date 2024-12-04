from ultralytics import YOLO
import cv2
import numpy as np
from tensorflow import keras
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog, QMessageBox, QFrame, QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap

class ModulDeteksidanPengenalan(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modul Deteksi dan Pengenalan")
        self.setFixedSize(1080, 640)  # Ukuran jendela

        # Load model
        self.yolo_model = YOLO('best.pt')
        self.face_recognition_model = keras.models.load_model('resnet-model-v12-150epcV2-loss(csAll)-48x48.keras')
        # Daftar nama berdasarkan urutan kelas pada model ResNet
        self.names = ['Darryl', 'Dion', 'Dony', 'Edgar', 'Hansen', 'Joseph', 'Mari', 'Mr.Darius', 'Robert', 'Steven', 'Suli', 'Susa', 'William','Yosia']  # Sesuaikan dengan nama yang sebenarnya

        # Atur Tampilan UI
        # Widget utama
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
    
        # Layout utama
        main_layout = QVBoxLayout(self.central_widget)
        # Layout horizontal untuk tombol kembali
        button_layout = QHBoxLayout()
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
        button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        main_layout.addLayout(button_layout)
        
        # Video display area (layar video)
        video_layout = QVBoxLayout()
        self.video_frame = QFrame(self)
        self.video_frame.setFixedSize(620,380)  # Display video (Center)
        video_layout.addWidget(self.video_frame, alignment=Qt.AlignCenter)

        self.canvas_label = QLabel(self.video_frame)
        self.canvas_label.setGeometry(0, 0, 620,370)  # Ukuran layar
        self.canvas_label.setStyleSheet("background-color: black;")

        main_layout.addLayout(video_layout)  # Tambahkan ke layout utama

        # Style tombol tambahan
        button_style = """
            font-size: 10px;
            background-color: #76BA99;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 5px;
        """ 
        # Bagian input dan output
        self.input_frame = QFrame(self)
        input_layout = QVBoxLayout(self.input_frame)
        row_layout = QHBoxLayout() # Label dan Edit box dalam 1 row
        self.total_seats_label = QLabel("Total Tempat Duduk:", self) # Label
        row_layout.addWidget(self.total_seats_label)
        self.total_seats_entry = QLineEdit(self) # Edit box
        row_layout.addWidget(self.total_seats_entry)
        # Tambahkan layout horizontal ke layout utama
        input_layout.addLayout(row_layout)
        # Input button Tempat Duduk
        self.input_button = QPushButton("Input", self) 
        self.input_button.setStyleSheet(button_style)
        self.input_button.clicked.connect(self.show_total_seats)
        input_layout.addWidget(self.input_button)

        # Layout Horizontal untuk jumlah kursi tersisa dan nama terdeteksi
        seats_and_name_layout = QHBoxLayout()
        self.remaining_seats_label = QLabel("Jumlah Tempat Duduk yang tersisa:", self) # Label untuk jumlah kursi tersisa
        seats_and_name_layout.addWidget(self.remaining_seats_label)
        # Label dinamis untuk jumlah kursi tersisa
        self.remaining_seats_value = QLabel("-", self)
        seats_and_name_layout.addWidget(self.remaining_seats_value)

        # Label untuk nama
        self.name_label = QLabel("Nama:", self)
        seats_and_name_layout.addWidget(self.name_label)
        # Label dinamis untuk nama yang terdeteksi
        self.name_value = QLabel("-", self)
        seats_and_name_layout.addWidget(self.name_value)

        # Tambahkan layout baru ke input_layout
        input_layout.addLayout(seats_and_name_layout)

        main_layout.addWidget(self.input_frame)

        # Tombol di bagian bawah
        self.button_frame = QFrame(self)
        button_layout = QHBoxLayout(self.button_frame)
        # Choose File Video
        self.choose_file_button = QPushButton("Choose File Video", self)
        self.choose_file_button.setStyleSheet(button_style)
        self.choose_file_button.clicked.connect(self.choose_file)
        button_layout.addWidget(self.choose_file_button)
        # Camera
        self.start_camera_button = QPushButton("Start Camera", self)
        self.start_camera_button.setStyleSheet(button_style)
        self.start_camera_button.clicked.connect(self.start_camera)
        button_layout.addWidget(self.start_camera_button)
        # Stop Process
        self.stop_camera_button = QPushButton("Stop", self)
        self.stop_camera_button.setStyleSheet(button_style)
        self.stop_camera_button.clicked.connect(self.stop_camera)
        button_layout.addWidget(self.stop_camera_button)

        main_layout.addWidget(self.button_frame)

        # Inisialisasi Awal
        # Video source and flags
        self.video_source = None
        self.is_camera_running = False
        self.cap = None  # Initialize VideoCapture object
        self.timer = QTimer()
        # Initialize total seats
        self.total_seats = 5  # Default value

    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Choose a Video File", "", "Video Files (*.mp4 *.avi *.mov)")
        if filename:
            self.video_source = filename
            self.play_video()

    def play_video(self):
        if self.video_source:
            self.cap = cv2.VideoCapture(self.video_source)  # Store the VideoCapture object
            self.timer.timeout.connect(self.update_video_frame)
            self.timer.start(50)

    def start_camera(self):
        self.video_source = 0  # 0 for the default camera
        self.is_camera_running = True
        self.stop_video()  # Ensure any video is stopped before starting the camera
        self.capture_camera()

    def capture_camera(self):
        if self.is_camera_running:
            self.cap = cv2.VideoCapture(self.video_source)  # Store the VideoCapture object
            self.timer.timeout.connect(self.update_video_frame)
            self.timer.start(50)

    def update_video_frame(self):
        if self.cap is not None:
            ret, frame = self.cap.read()
            if ret:
                # Resize frame to fit GUI
                frame = cv2.resize(frame, (620, 410))

                # Detect objects with YOLOv8
                results = self.yolo_model(frame)
                num_boxes_above_threshold = 0  # Initialize counter for boxes above threshold

                detected_names = []  # Initialize list for detected names

                for result in results:
                    for i, bbox in enumerate(result.boxes.xyxy):
                        bbox = bbox.cpu().numpy()  # Convert to NumPy array
                        x1, y1, x2, y2 = map(int, bbox[:4])  # Get bounding box coordinates
                        cls = int(result.boxes.cls[i])  # Get class ID
                        confidence = result.boxes.conf[i]  # Get confidence score

                        # Check if confidence is above the threshold
                        if cls == 0 and confidence >= 0.4:  # Class ID 0 for 'person'
                            num_boxes_above_threshold += 1  # Increment counter

                            # Draw bounding box around the person
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                            # Crop and preprocess face from the bounding box
                            face_roi = self.crop_face_from_bbox(frame, bbox)
                            detected_name, conf = self.recognize_face(face_roi)

                            # Append detected name to the list
                            detected_names.append(f"{detected_name} (Conf: {conf:.2f})")

                            # Draw the name label above the bounding box
                            label = f"{detected_name} (Conf: {conf:.2f})"
                            cv2.putText(frame, label, (x1 - 60, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)  # Kecilkan font size

                # Output labels
                # Calculate remaining seats
                remaining_seats = max(self.total_seats - num_boxes_above_threshold, 0)

                # Gabungkan dan urutkan nama-nama yang terdeteksi
                # Hanya ambil nama tanpa confidence
                sorted_detected_names = sorted([name.split(' (')[0] for name in detected_names])  # Urutkan nama-nama tanpa conf
                all_detected_names = ", ".join(sorted_detected_names) if sorted_detected_names else "Unknown"

                # Update dynamic labels
                self.remaining_seats_value.setText(str(remaining_seats))
                self.name_value.setText(all_detected_names)

                # Convert frame to QImage for display
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = rgb_image.shape
                bytes_per_line = channel * width
                q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                self.canvas_label.setPixmap(QPixmap.fromImage(q_image))

    def stop_camera(self):
        self.is_camera_running = False
        self.stop_video()

    def stop_video(self):
        if self.cap is not None:
            self.cap.release()  # Release the video source
            self.timer.stop()  # Stop the timer
            self.cap = None  # Reset the cap object
            # Do not clear the canvas_label, keep the last frame visible

    def show_total_seats(self):
        try:
            # Ambil input dari QLineEdit dan ubah menjadi integer
            input_seats = int(self.total_seats_entry.text())
            
            # Validasi agar total seats tidak kurang dari 0
            if input_seats > 0:
                self.total_seats = input_seats
                QMessageBox.information(self, "Info", f"Total Seats berhasil diperbarui: {self.total_seats}")
            else:
                QMessageBox.warning(self, "Peringatan", "Total tempat duduk harus lebih dari 0.")
        
        except ValueError:
            # Jika input bukan angka
            QMessageBox.warning(self, "Peringatan", "Masukkan angka yang valid untuk total tempat duduk.")

    def crop_face_from_bbox(self, frame, bbox):
        x1, y1, x2, y2 = map(int, bbox)
        return frame[y1:y2, x1:x2]

    def preprocess_face(self, face_roi):
        face_roi = cv2.resize(face_roi, (48, 48))  # Adjust size as needed for your model
        face_roi = face_roi.astype('float32') / 255.0
        return np.expand_dims(face_roi, axis=0)

    def recognize_face(self, face_roi):
        # Preprocess the face image for recognition
        preprocessed_face = self.preprocess_face(face_roi)
        
        # Predict the class of the face
        predictions = self.face_recognition_model.predict(preprocessed_face)
        confidence = np.max(predictions)
        
        # Determine threshold for recognition
        if confidence > 0.2:  # Adjust this threshold based on your model's performance
            predicted_class_index = np.argmax(predictions)
            
            # Dapatkan nama dari indeks yang terdeteksi
            detected_name = self.names[predicted_class_index]  # Ganti 'Person {index}' dengan nama dari daftar
            return detected_name, confidence
        else:
            return "Unknown", confidence

    def open_modul_halaman_utama(self):
        # Impor dilakukan di sini untuk menghindari circular import
        from Modul_HalamanUtama import HomePage
        
        self.modul_halaman_utama = HomePage()
        self.modul_halaman_utama.show()
        self.close()  # Close the current window