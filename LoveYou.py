# Made By PeterHo(PHP135) 

dick = """




███╗░░░███╗░█████╗░██████╗░███████╗  ██████╗░██╗░░░██╗  ██████╗░██╗████████╗░█████╗░██╗░░██╗░█████╗░
████╗░████║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚██╗░██╔╝  ██╔══██╗██║╚══██╔══╝██╔══██╗██║░░██║██╔══██╗
██╔████╔██║███████║██║░░██║█████╗░░  ██████╦╝░╚████╔╝░  ██████╔╝██║░░░██║░░░██║░░██║███████║██║░░██║
██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░  ██╔══██╗░░╚██╔╝░░  ██╔═══╝░██║░░░██║░░░██║░░██║██╔══██║██║░░██║
██║░╚═╝░██║██║░░██║██████╔╝███████╗  ██████╦╝░░░██║░░░  ██║░░░░░██║░░░██║░░░╚█████╔╝██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░╚════╝░







"""








import pygame
import threading
import tkinter as tk
from tkinter import messagebox
import time

class Forsomeone(tk.Tk): # based on Tkinter
    def __init__(self):
        super().__init__() # initialize tkinter
        self.Lyrics = []
        self.rep = 0
        self.main()

    def play_Music(self): # Play music
        self.start_button.destroy()
        pygame.mixer.init()
        pygame.mixer.music.load(r"assets/music.wav")
        pygame.mixer.music.play()
        self.thread = threading.Thread(target=self.Display_Lyrics)
        self.thread.start()

    def End_Kill(self, event): # when press ESC
        self.lyrics_text.config(text="")
        self.reset_state() # need to fix this shit like if someone clicked this button lyrics would be stopped and not continue
        pygame.mixer.music.stop()
        self.top = tk.Toplevel(self)
        self.top.wm_attributes("-topmost", 1)
        self.top.geometry("400x400")
        self.top.wm_resizable(0,0)
        self.top.protocol("WM_DELETE_WINDOW", lambda: None)
        self.top.configure(bg="#824670")
        self.label = tk.Label(self.top, text="Hay không:))", font=("Time New Romans", 30, "bold"), bg="#824670", fg="#CD9FCC")
        self.label.pack()
        self.nhap = tk.Entry(self.top, font=("Time New Romans", 24, "bold"), relief="solid", bg="#824670", fg="#CD9FCC")
        self.nhap.pack(pady=20)
        self.button = tk.Button(self.top, text="Gửi", font=("Time New Romans", 24, "bold"), relief="ridge", bg="#824670", fg="#CD9FCC", command=self.Check)
        self.button.pack(ipadx=20)

    def Check(self): # Check
        entry = self.nhap.get().lower()
        if entry in ["y", "yes", "có", "c", "co", "hay","hay vl", "hay vcl", "hay vãi", "hay vãi hợi", "hay vãi đái","hay vđ","hay vcll"]:
            self.lyrics_text.config(text="Thank You, Love You<3")
            self.lyrics_text.place(x=470, y=390)
            messagebox.showinfo("Foraido", "Cảm Ơn Nha")
            self.top.destroy()
            self.To_Tinh()
        elif entry in ["n", "no", "không", "k", "khong", "không hay", "khong hay", "đ", "đéo", "đell", "dell", "như lồn","như lol", "cặc", "như cặc", "như l", "như c", "dở", "dở vl", "dở vđ", "dở vcl"]:
            messagebox.showinfo("Foraido", "Cái Dái mà không hay ")
            messagebox.showinfo("Foraido", "Coi lại tiếp nhé")
            self.top.destroy()
            self.reset_state()
            self.main()
        elif entry == "":
            messagebox.showinfo("Foraido", "Chưa Nhập gì mà gửi cái lồn")
        else:
            messagebox.showerror("Foraido", "Nhập cái đéo gì v")

    def Display_Lyrics(self): #Display lyrics
        time.sleep(12)
        with open(r"assets/lyrics.txt", "r") as f:
            self.Lyrics = f.read()
        lyrics = self.Lyrics
        length = len(lyrics)
        words_display = 4 # Words display each 0.45 sec
        l = []
        for i in range(0, length, words_display):
            l.append(lyrics[i:i+words_display])
        for x in range(len(l)):
            time.sleep(0.45)
            self.lyrics_text.config(text="".join(l[:x+1]))
            self.update_idletasks()
        time.sleep(3)
        self.lyrics_text.config(text="Nhấn esc đi")
        self.lyrics_text.place(x=610, y=395)

    def Accepted(self):
        messagebox.showinfo("Forsomeone", "Ye T bt mà")
        messagebox.showinfo("LOVEYOU", "LOVEYOUTOO")
        self.lyrics_text.config(text="GOODBYE BAE")
        self.lyrics_text.place(x=580 ,y=395)
        messagebox.showinfo("LOVEYOU", "GOODBYE")
        time.sleep(5)
        self.destroy()

    def To_Tinh(self):
        subwidget = tk.Toplevel()
        subwidget.geometry("400x400")
        subwidget.protocol("WM_DELETE_WINDOW", lambda: None)
        subwidget.wm_resizable(0,0)
        subwidget.configure(background="#824670")
        label = tk.Label(subwidget, text="Làm Ny t nhé", font=("Time New Romans", 30, "bold"), bg="#824670", fg="#CD9FCC")
        label.pack()
        button = tk.Button(subwidget, text="Đồng Ý", width=10, height=5, font=("Time New Romans", 24, "bold"), relief="ridge", bg="#824670", fg="#CD9FCC", activebackground="#824670", activeforeground="#CD9FCC")
        button.configure(command=self.Accepted)
        button.pack(side=tk.RIGHT)
        button2 = tk.Button(subwidget, text="Genau", width=10, height=5, font=("Time New Romans", 24, "bold"), relief="ridge", bg="#824670", fg="#CD9FCC", activebackground="#824670", activeforeground="#CD9FCC")
        button2.configure(command=self.Accepted)
        button2.pack(side=tk.RIGHT)

    def reset_state(self): # reset the list to display nothing if rẻun
        self.Lyrics = []
        self.lyrics_text.config(text="")
        self.update_idletasks()

    def main(self): # Main
        self.lyrics_text = tk.Label(self, text=self.Lyrics, font=("channel", 40, "bold"), bg="#CD9FCC", fg="#fc007e", wraplength=self.winfo_width() - 50)
        self.lyrics_text.place(x=150, y=300)
        self.start_button = tk.Button(self, text="<3", command=self.play_Music, width=20, height=5, relief=tk.FLAT, bg="#CD9FCC", font=("Ebrima", 50, "bold"), activebackground="#CD9FCC", bd="0", highlightthickness=0)
        self.start_button.place(x=360, y=160)
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.bind("<Escape>", self.End_Kill)


        



if __name__ == "__main__":
    print(dick)
    root = Forsomeone()
    image = tk.PhotoImage(file=r"assets/heart.png")
    root.iconphoto(True, image)
    root.bind("<Escape>", root.End_Kill)
    root.title("Foraido")
    root.configure(background="#CD9FCC")
    root.attributes("-fullscreen", True)
    root.mainloop()
