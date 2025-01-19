# PRODIGY_CS_02

# Image Encryptor/Decryptor

A simple GUI-based application to encrypt and decrypt images using  image pixels and a user-provided key. This tool uses Python's `Pillow` and `NumPy` libraries for image manipulation and `Tkinter` for the graphical user interface.

### Features

- **Encryption**: Encrypts an image using a key (0-255) and saves the result as `encrypted_image.png`.
- **Decryption**: Decrypts the encrypted image using the same key and saves the result as `decrypted_image.png`.
- **Simple GUI**: User-friendly interface with options to browse files and input encryption keys.
- **Validation**: Ensures that the encryption key is a valid integer within the range of 0-255.
- Note : Ensure that the selected image file is accessible from the project directory or provide the correct path during encryption.

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `Pillow`
  - `NumPy`

Install the dependencies using pip:

```bash
pip install pillow numpy
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MAvinash24/PRODIGY_CS_02.git
```

2. Navigate to project directory:
```bash
cd PRODIGY_CS_02
```

3. Run the tool:
```bash
python pixel_manipulation.py
```

### Screenshot of GUI
![Image Pixel Manipulation GUI](https://github.com/user-attachments/assets/8eae7e7f-81b9-4349-a851-18b4b64c0f53)
