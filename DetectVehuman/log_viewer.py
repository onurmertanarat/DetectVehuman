import tkinter as tk
from tkinter import scrolledtext, messagebox
import os

class LogViewer:
    def __init__(self, root, log_file="logs/system_log.txt"):
        self.root = root
        self.log_file = log_file
        self.root.title("Araç Algılama ve Kapı Durumu")
        self.root.geometry('600x500')

        self.log_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.log_text.pack(expand=True, fill='both')

        self.gate_status_label = tk.Label(self.root, text="Kapı Durumu: Bilinmiyor", font=("Arial", 14))
        self.gate_status_label.pack(pady=20)

        self.update_log()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_log(self):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r") as f:
                    log_data = f.readlines()

                self.log_text.config(state=tk.NORMAL)
                self.log_text.delete(1.0, tk.END)
                for line in log_data:
                    self.log_text.insert(tk.END, line)
                self.log_text.config(state=tk.DISABLED)

                self.log_text.yview(tk.END)
            except Exception as e:
                messagebox.showerror("Hata", f"Log dosyası okunurken bir hata oluştu: {e}")
        else:
            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete(1.0, tk.END)
            self.log_text.insert(tk.END, "Henüz kayıt yok.")
            self.log_text.config(state=tk.DISABLED)

        self.root.after(2000, self.update_log)

    def update_gate_status(self, status):
        self.gate_status_label.config(text=f"Kapı Durumu: {status}")

    def on_closing(self):
        if messagebox.askokcancel("Çıkış", "Programdan çıkmak istediğinize emin misiniz?"):
            self.root.destroy()
