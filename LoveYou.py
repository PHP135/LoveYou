import pygame
import threading
import tkinter as tk
from tkinter import messagebox
import time

class Forchianh(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Lyrics = []
        self.rep = 0
        self.main()

    def play_Music(self):
        self.start_button.destroy()
        pygame.mixer.init()
        pygame.mixer.music.load(r"assets/forchanh.wav")
        pygame.mixer.music.play()
        self.thread = threading.Thread(target=self.Display_Lyrics)
        self.thread.start()

    def End_Kill(self, event):
        pygame.mixer.music.stop()
        top = tk.Toplevel(self)
        top.geometry("400x400")
        top.protocol("WM_DELETE_WINDOW", lambda: None)
        top.configure(bg="#824670")
        self.label = tk.Label(top, text="Hay không:))(y/n)", font=("Time New Romans", 30, "bold"), bg="#824670", fg="#CD9FCC")
        self.label.pack()
        self.nhap = tk.Entry(top, font=("Time New Romans", 24, "bold"), relief="solid", bg="#824670", fg="#CD9FCC")
        self.nhap.pack(pady=20)
        self.button = tk.Button(top, text="Gửi", font=("Time New Romans", 24, "bold"), relief="ridge", bg="#824670", fg="#CD9FCC", command=self.Check)
        self.button.pack(ipadx=20)

    def Check(self):
        entry = self.nhap.get().lower()
        if entry in ["y", "yes", "có", "c", "co", "hay"]:
            messagebox.showinfo("Forchanh", "Cảm Ơn Nha")
            self.To_Tinh()
        elif entry in ["n", "no", "không", "k", "khong", "không hay", "khong hay"]:
            messagebox.showinfo("Forchanh", "Cái Dái")
            messagebox.showinfo("Forchanh", "Coi lại tiếp nhé")
            self.reset_state()
            self.main()
        else:
            messagebox.showerror("ForChanh", "Có Hoặc là không thôi ku")
            self.reset_state()
            self.main()

    def To_Tinh(self):
        top = tk.Toplevel()
        top.geometry("400x400")
        top.protocol("WM_DELETE_WINDOW", lambda: None)
        label = tk.Label(top, text="Làm Ny t nhé", font=("Time New Romans", 18, "bold"), padx=10)
        label.pack()
        button = tk.Button(top, text="Có", width=25, height=10)
        button.pack(side=tk.RIGHT)
        button2 = tk.Button(top, text="Genau", width=25, height=10)
        button2.pack(side=tk.RIGHT)

    def Display_Lyrics(self):
        time.sleep(12)
        with open(r"assets/lyrics.txt", "r") as f:
            self.Lyrics = f.read()
        lyrics = self.Lyrics
        length = len(lyrics)
        words_display = 4
        l = []
        for i in range(0, length, words_display):
            l.append(lyrics[i:i+words_display])
        for x in range(len(l)):
            time.sleep(0.45)
            self.lyrics_text.config(text="".join(l[:x+1]))
            self.update_idletasks()
        time.sleep(2)
        self.lyrics_text.config(text="Nhấn esc đi")
        self.lyrics_text.place(x=620, y=390)
        time.sleep(3)
        self.lyrics_text.config(text="")

    def reset_state(self):
        self.Lyrics = []
        self.lyrics_text.config(text="")
        self.update_idletasks()

    def main(self):
        self.lyrics_text = tk.Label(self, text=self.Lyrics, font=("channel", 40, "bold"), bg="#CD9FCC", fg="#fc007e", wraplength=self.winfo_width() - 50)
        self.lyrics_text.place(x=150, y=300)
        self.start_button = tk.Button(self, text="<3", command=self.play_Music, width=20, height=5, relief=tk.FLAT, bg="#CD9FCC", font=("Ebrima", 50, "bold"), activebackground="#CD9FCC", bd="0", highlightthickness=0)
        self.start_button.place(x=360, y=160)
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.bind("<Escape>", self.End_Kill)
        



if __name__ == "__main__":
    root = Forchianh()
    image = tk.PhotoImage(file=r"assets/heart.png")
    root.iconphoto(True, image)
    root.bind("<Escape>", root.End_Kill)
    root.title("ForChanh")
    root.configure(background="#CD9FCC")
    root.attributes("-fullscreen", True)
    root.mainloop()
