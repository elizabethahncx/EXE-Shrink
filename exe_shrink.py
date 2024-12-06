import sys
import os
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QPushButton, QLabel,
    QLineEdit, QProgressBar, QVBoxLayout, QHBoxLayout, QWidget, QTextEdit, QRadioButton, QButtonGroup
)
from PyQt5.QtCore import Qt

class EXEShrink(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EXE Shrink - Compress Your Executables!")
        self.setGeometry(100, 100, 500, 400)
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()

        # Input file section
        file_layout = QHBoxLayout()
        self.file_label = QLabel("Select Executable File:")
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Browse for .exe file...")
        self.file_browse_btn = QPushButton("Browse")
        self.file_browse_btn.clicked.connect(self.browse_file)
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(self.file_browse_btn)

        # Compression level
        compression_layout = QHBoxLayout()
        self.compression_label = QLabel("Select Compression Level:")
        self.low_radio = QRadioButton("Low")
        self.medium_radio = QRadioButton("Medium")
        self.high_radio = QRadioButton("High")
        self.medium_radio.setChecked(True)
        compression_group = QButtonGroup(self)
        compression_group.addButton(self.low_radio)
        compression_group.addButton(self.medium_radio)
        compression_group.addButton(self.high_radio)
        compression_layout.addWidget(self.compression_label)
        compression_layout.addWidget(self.low_radio)
        compression_layout.addWidget(self.medium_radio)
        compression_layout.addWidget(self.high_radio)

        # Output folder section
        output_layout = QHBoxLayout()
        self.output_label = QLabel("Save Compressed File To:")
        self.output_input = QLineEdit()
        self.output_input.setPlaceholderText("Choose output folder...")
        self.output_browse_btn = QPushButton("Browse")
        self.output_browse_btn.clicked.connect(self.browse_output_folder)
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_input)
        output_layout.addWidget(self.output_browse_btn)

        # Action buttons
        action_layout = QHBoxLayout()
        self.compress_btn = QPushButton("Compress")
        self.compress_btn.clicked.connect(self.compress_file)
        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset_fields)
        action_layout.addWidget(self.compress_btn)
        action_layout.addWidget(self.reset_btn)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        # Log area
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)

        # Adding to main layout
        main_layout.addLayout(file_layout)
        main_layout.addLayout(compression_layout)
        main_layout.addLayout(output_layout)
        main_layout.addLayout(action_layout)
        main_layout.addWidget(self.progress_bar)
        main_layout.addWidget(self.log_area)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Executable File", "", "Executable Files (*.exe)")
        if file_path:
            self.file_input.setText(file_path)

    def browse_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.output_input.setText(folder_path)

    def compress_file(self):
        exe_path = self.file_input.text()
        output_folder = self.output_input.text()
        if not exe_path or not output_folder:
            self.log_area.append("Please select both an executable file and output folder.")
            return

        compression_level = "medium"
        if self.low_radio.isChecked():
            compression_level = "low"
        elif self.high_radio.isChecked():
            compression_level = "high"

        self.log_area.append(f"Starting compression for {exe_path} at {compression_level} level...")
        self.progress_bar.setValue(50)

        # Simulating compression using UPX
        try:
            output_file = os.path.join(output_folder, os.path.basename(exe_path))
            subprocess.run(["upx", f"--{compression_level}", "-o", output_file, exe_path], check=True)
            self.progress_bar.setValue(100)
            self.log_area.append(f"Compression successful! Saved to {output_file}")
        except Exception as e:
            self.log_area.append(f"Error during compression: {e}")

    def reset_fields(self):
        self.file_input.clear()
        self.output_input.clear()
        self.medium_radio.setChecked(True)
        self.progress_bar.setValue(0)
        self.log_area.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EXEShrink()
    window.show()
    sys.exit(app.exec_())
