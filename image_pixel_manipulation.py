import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

def encrypt_image(image_path, output_path, key):
    try:
        with Image.open(image_path) as img:
            img = img.convert('RGB')

            img_array = np.array(img)

            encrypted_array = img_array + key

            encrypted_array = np.clip(encrypted_array, 0, 255)

            encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir) and output_dir != '':
                os.makedirs(output_dir)

            encrypted_image.save(output_path)
            return True, f"Encrypted image saved to {output_path}"

    except Exception as e:
        return False, f"Error during encryption: {e}"

def decrypt_image(image_path, output_path, key):
    try:
        with Image.open(image_path) as img:
            img = img.convert('RGB')
            img_array = np.array(img)

            decrypted_array = img_array - key

            decrypted_array = np.clip(decrypted_array, 0, 255)

            decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir) and output_dir != '':
                os.makedirs(output_dir)

            decrypted_image.save(output_path)
            return True, f"Decrypted image saved to {output_path}"

    except Exception as e:
        return False, f"Error during decryption: {e}"

def browse_file(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def encrypt_action():
    image_path = image_entry.get()
    if not os.path.exists(image_path):
        messagebox.showerror("Error", "Selected image file does not exist.")
        return

    try:
        key = int(key_entry.get())
        if key < 0 or key >= 256:
            messagebox.showerror("Error", "Please enter a key in the range of 0-255.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid key. Please enter an integer.")
        return

    output_path = "encrypted_image.png"
    success, message = encrypt_image(image_path, output_path, key)
    if success:
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", message)

def decrypt_action():
    image_path = "encrypted_image.png"
    if not os.path.exists(image_path):
        messagebox.showerror("Error", "Encrypted image file not found. Please encrypt an image first.")
        return

    try:
        key = int(key_entry.get())
        if key < 0 or key >= 256:
            messagebox.showerror("Error", "Please enter a key in the range of 0-255.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid key. Please enter an integer.")
        return

    output_path = "decrypted_image.png"
    success, message = decrypt_image(image_path, output_path, key)
    if success:
        messagebox.showinfo("Success", message)
    else:
        messagebox.showerror("Error", message)

# Create GUI
def main():
    root = tk.Tk()
    root.title("Image Encryptor/Decryptor")
    root.geometry("500x300")
    root.resizable(False, False)

    font_settings = ("Helvetica", 12)

    tk.Label(root, text="Image Encryptor/Decryptor", font=("Helvetica", 16, "bold"), pady=10).pack()

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text="Select Image File:", font=font_settings).grid(row=0, column=0, sticky="w", pady=5)
    global image_entry
    image_entry = tk.Entry(frame, width=40, font=font_settings)
    image_entry.grid(row=0, column=1, padx=5, pady=5)

    browse_button = tk.Button(frame, text="Browse", font=font_settings, command=lambda: browse_file(image_entry))
    browse_button.grid(row=0, column=2, padx=5, pady=5)

    tk.Label(frame, text="Enter Encryption Key (0-255):", font=font_settings).grid(row=1, column=0, sticky="w", pady=5)
    global key_entry
    key_entry = tk.Entry(frame, width=40, font=font_settings)
    key_entry.grid(row=1, column=1, padx=5, pady=5)

    encrypt_button = tk.Button(frame, text="Encrypt", font=font_settings, command=encrypt_action, width=10)
    encrypt_button.grid(row=2, column=0, pady=20)

    decrypt_button = tk.Button(frame, text="Decrypt", font=font_settings, command=decrypt_action, width=10)
    decrypt_button.grid(row=2, column=1, pady=20)

    exit_button = tk.Button(frame, text="Exit", font=font_settings, command=root.destroy, width=10)
    exit_button.grid(row=2, column=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
