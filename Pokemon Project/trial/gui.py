import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\eldon\Documents\Kuliah\KULIAH SMT 5\PEMLAN\DOSEN\projek\assets")

def on_button_click():
    label_var.set("Hello, " + name_entry.get() + "!")
    text.insert(tk.END, f"\n{name_entry.get()} is awesome!")

# Buat instance dari Tk
app = tk.Tk()
app.title("Contoh Aplikasi Tkinter")

# Buat Label
label_var = tk.StringVar()
label_var.set("Selamat datang di aplikasi Tkinter!")
label = tk.Label(app, textvariable=label_var, font=("Arial", 14))
label.pack(pady=10)

# Buat Frame
frame = ttk.Frame(app)
frame.pack(pady=10)

# Buat Entry (Input teks)
name_label = ttk.Label(frame, text="Masukkan Nama:")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Buat Tombol
button = ttk.Button(app, text="Sapa", command=on_button_click)
button.pack(pady=10)

# Buat Text (Kolom teks)
text = tk.Text(app, height=5, width=40)
text.pack(pady=10)
text.insert(tk.END, "Ini adalah kolom teks.\nIsi dapat ditambahkan di sini.")

# Buat Spinbox
spin_label = ttk.Label(app, text="Pilih Angka:")
spin_label.pack(pady=5)
spinbox_var = tk.IntVar()
spinbox = ttk.Spinbox(app, from_=1, to=10, textvariable=spinbox_var)
spinbox.pack(pady=5)

# Buat Checkbutton
check_var = tk.BooleanVar()
checkbutton = ttk.Checkbutton(app, text="Saya setuju", variable=check_var)
checkbutton.pack(pady=5)

# Buat Radiobutton
radio_var = tk.StringVar()
radiobutton1 = ttk.Radiobutton(app, text="Pilihan 1", variable=radio_var, value="1")
radiobutton2 = ttk.Radiobutton(app, text="Pilihan 2", variable=radio_var, value="2")
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

# Buat Combobox
combo_label = ttk.Label(app, text="Pilih Bahasa:")
combo_label.pack(pady=5)
combo_var = tk.StringVar()
combo_box = ttk.Combobox(app, textvariable=combo_var, values=["Python", "Java", "C++"])
combo_box.pack(pady=5)

# Buat Frame untuk Gambar
canvas_frame = ttk.Frame(app)
canvas_frame.pack(pady=10)

# Load gambar dari file dan ubah ukurannya
image_path = ASSETS_PATH / "battle.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((200, 200), Image.ANTIALIAS)  # Sesuaikan ukuran gambar yang diinginkan
tk_image = ImageTk.PhotoImage(resized_image)

# Tampilkan gambar di dalam Canvas
canvas = tk.Canvas(canvas_frame, width=200, height=200)
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
canvas.pack()

# Jalankan loop utama
app.mainloop()
