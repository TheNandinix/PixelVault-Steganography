import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from core.encryption import hide_data
from core.decryption import show_data

ctk.set_appearance_mode("Dark") # Requirement: Usability [cite: 74]

class PixelVaultApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PixelVault - Secure Steganography")
        self.geometry("600x500")
        
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
        
        self.enc = self.tabview.add("Encrypt")
        self.dec = self.tabview.add("Decrypt")
        
        self.setup_enc()
        self.setup_dec()

    def setup_enc(self):
        ctk.CTkButton(self.enc, text="Select Image", command=self.sel_enc).pack(pady=10)
        self.lbl_enc = ctk.CTkLabel(self.enc, text="No File")
        self.lbl_enc.pack()
        self.msg = ctk.CTkTextbox(self.enc, height=100); self.msg.pack(pady=10)
        self.pass_enc = ctk.CTkEntry(self.enc, placeholder_text="Password (Optional)"); self.pass_enc.pack()
        ctk.CTkButton(self.enc, text="Encrypt", fg_color="green", command=self.run_enc).pack(pady=10)
        self.enc_path = ""

    def setup_dec(self):
        ctk.CTkButton(self.dec, text="Select Image", command=self.sel_dec).pack(pady=10)
        self.lbl_dec = ctk.CTkLabel(self.dec, text="No File")
        self.lbl_dec.pack()
        self.pass_dec = ctk.CTkEntry(self.dec, placeholder_text="Password"); self.pass_dec.pack()
        ctk.CTkButton(self.dec, text="Decrypt", fg_color="orange", command=self.run_dec).pack(pady=10)
        self.res = ctk.CTkTextbox(self.dec, height=100); self.res.pack(pady=10)
        self.dec_path = ""

    def sel_enc(self):
        p = filedialog.askopenfilename(filetypes=[("PNG", "*.png")])
        if p: self.enc_path=p; self.lbl_enc.configure(text=os.path.basename(p))

    def sel_dec(self):
        p = filedialog.askopenfilename(filetypes=[("PNG", "*.png")])
        if p: self.dec_path=p; self.lbl_dec.configure(text=os.path.basename(p))

    def run_enc(self):
        if not self.enc_path: return
        save = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if save:
            ok, txt = hide_data(self.enc_path, self.msg.get("0.0", "end").strip(), save, self.pass_enc.get())
            messagebox.showinfo("Result", txt)

    def run_dec(self):
        if not self.dec_path: return
        ok, txt = show_data(self.dec_path, self.pass_dec.get())
        self.res.delete("0.0", "end"); self.res.insert("0.0", txt)