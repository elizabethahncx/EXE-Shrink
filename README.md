# EXE Shrink - Compress Your Executables!

**EXE Shrink** is a simple yet powerful GUI tool designed to compress Windows executable files (.exe) to reduce their size without compromising functionality. It uses the UPX (Ultimate Packer for Executables) tool in the backend, making it easy to handle large executables for efficient distribution and storage.

---

## Features
- **File Selection**: Easily select the `.exe` file you want to compress using a file browser.
- **Compression Levels**: Choose from Low, Medium, or High compression options.
- **Custom Output**: Specify the directory to save your compressed file.
- **Progress Tracking**: Monitor the compression process with a progress bar.
- **Log Output**: View detailed logs about the compression process, including size reduction and time taken.
- **Reset Functionality**: Clear inputs and reset settings to defaults with one click.
- **Dark/Light Theme**: Choose your preferred appearance.

---

## Requirements
- Python 3.7 or higher
- PyQt5 (`pip install pyqt5`)
- UPX (Ultimate Packer for Executables): [Download UPX](https://upx.github.io/)

---

## Installation
1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/yourusername/exe-shrink.git
   cd exe-shrink
