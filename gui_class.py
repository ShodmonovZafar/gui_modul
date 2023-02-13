import tkinter as tk
import gui_funksiyalari as funk
from gui_sozlamalari import Sozlamalar
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg


soz = Sozlamalar()

class Gui():
    """____"""
    
    widjet_turlari = ["Button", "Canvas", "Checkbutton", "Entry", "Frame",
                      "Label", "Listbox", "Menubutton", "Menu", "Message",
                      "Radiobutton", "Scale", "Scrollbar", "Text", "Toplevel",
                      "Spinbox", "PanedWindow", "LabelFrame", "tkMessageBox"]

    def __init__(self):
        """_____"""
        
        # Asosiy oynani yaratish.
        self.asosiy_oyna = tk.Tk()

        # Asosiy oynaga nom berish.
        self.asosiy_oyna.title(soz.asosiy_oyna_nomi)

        # Asosiy oyna o'lchamini boshqarish.

        ## Asosiy oyna o'lchamini belgilash.
        self.asosiy_oyna.geometry("{0}x{1}".format(soz.asosiy_oyna_kengligi, soz.asosiy_oyna_balandligi))

        ## Asosiy oyna o'lchamini o'zgarmaydigan yoki o'zgaradigan qilish.
        self.asosiy_oyna.resizable(False, False)

    def notebook(self):
        """____"""
        
        # 1-notebook.
        self.notebook1 = ttk.Notebook(self.asosiy_oyna)
        
        # 1-frame.
        self.frame1 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.frame1, text="frame1")
        
        # 2-frame.
        self.frame2 = ttk.Frame(self.notebook1)
        self.notebook1.add(self.frame2, text="frame2")
        
        self.notebook1.pack(expand=1, fill="both")
    
    def label_frame(self):
        """"____"""
        
        # 1-label_frame.
        self.label_frame1 = ttk.LabelFrame(self.frame1, text="label_frame1")
        self.label_frame1.grid(column=0, row=0, padx=10, pady=10)
    
    def widjetlar(self):
        """
        Widjet turlari
            |--> Button
            |--> Canvas
            |--> Checkbutton
            |--> Entry
            |--> Frame
            |--> Label
            |--> Listbox
            ...
        """

        # 1-widjet turi: Label.

        ## 1-label.
        self.label1 = ttk.Label(self.label_frame1, width=12, text="1-label")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        # 2-widjet turi: Button.
        
        ## 1-button.
        self.button1 = ttk.Button(self.label_frame1, text="OK", command=self.button1_funk)
        self.button1.grid(column=2, row=0, padx=4, pady=4)
        
        # 3-widjet turi: Entry.

        ## 1-entry.
        self.entry1_str = tk.StringVar()
        self.entry1 = ttk.Entry(self.label_frame1, width=12, textvariable=self.entry1_str)
        self.entry1.grid(column=1, row=0)
        
        ### 1-entry-ga focus-ni o'ratish.
        self.entry1.focus()

        # 4-widjet turi: Combobox.

        ## 1-combobox.
        self.combobox1_str = tk.StringVar()
        self.combobox1 = ttk.Combobox(self.label_frame1, width=12, textvariable=self.combobox1_str)
        self.combobox1["values"] = (1996, 1997, 1998, 1999, 2000)
        self.combobox1.grid(column=0, row=1)
        self.combobox1.current(0)

        ## 2-combobox.
        self.combobox2_str = tk.StringVar()
        self.combobox2 = ttk.Combobox(self.label_frame1, width=12, textvariable=self.combobox2_str, state="readonly")
        self.combobox2["values"] = (1996, 1997, 1998, 1999, 2000)
        self.combobox2.grid(column=1, row=1)
        self.combobox2.current(0)

        # 5-widjet turi: Checkbutton.

        ## 1-checkbutton.
        self.checkbutton1_var = tk.IntVar()
        self.checkbutton1 = tk.Checkbutton(self.label_frame1, text="Nofaol", variable=self.checkbutton1_var, state=soz.NOFAOL)
        self.checkbutton1.select()
        self.checkbutton1.grid(column=0, row=3, sticky=soz.CHAP)

        ## 2-checkbutton.
        self.checkbutton2_var = tk.IntVar()
        self.checkbutton2 = tk.Checkbutton(self.label_frame1, text="Belgilanmagan", variable=self.checkbutton2_var)
        self.checkbutton2.deselect()
        self.checkbutton2.grid(column=1, row=3, sticky=soz.CHAP)

        ## 3-checkbutton.
        self.checkbutton3_var = tk.IntVar()
        self.checkbutton3 = tk.Checkbutton(self.label_frame1, text="Faol", variable=self.checkbutton3_var)
        self.checkbutton3.select()
        self.checkbutton3.grid(column=2, row=3, sticky=soz.ONG)

        # 6-widjet turi: Radiobutton.

        ## 1-radiobutton.
        self.radiobutton1_var = tk.IntVar()
        self.radiobutton1 = tk.Radiobutton(self.label_frame1, text="Ko'k", variable=self.radiobutton1_var, value=1, command=self.radiobutton1_funk)
        self.radiobutton1.grid(column=0, row=5, sticky=soz.CHAP, columnspan=3)

        ## 2-radiobutton.
        self.radiobutton2 = tk.Radiobutton(self.label_frame1, text="Oltin", variable=self.radiobutton1_var, value=2, command=self.radiobutton1_funk)
        self.radiobutton2.grid(column=1, row=5, sticky=soz.CHAP, columnspan=3)

        ## 3-radiobutton.
        self.radiobutton3 = tk.Radiobutton(self.label_frame1, text="Qizil", variable=self.radiobutton1_var, value=3, command=self.radiobutton1_funk)
        self.radiobutton3.grid(column=2, row=5, sticky=soz.CHAP, columnspan=3)

        # 7-widjet turi: ScrolledText.

        ## 1-scrolledtext.
        self.a = tk.WORD
        self.scrolledtext1 = scrolledtext.ScrolledText(self.label_frame1, width=30, height=3, wrap=self.a)
        self.scrolledtext1.grid(column=0, columnspan=3)

    def css(self):
        self.asosiy_oyna.configure(bg="#ccaa00", padx=4, pady=4)

        # self.frame2_style = ttk.Style()
        # self.frame2_style.configure("BW.TFrame", foreground="white", background="#215462")

        # # 1-label.
        # self.label1_style = ttk.Style()
        # self.label1_style.configure("BW.TLabel", foreground="white", background="black")
        # self.label1.configure(style="BW.TLabel")
        # self.frame1.configure(style="BW.TFrame")


    # widjetlar bilan bo'g'lanadigan funksiyalar.

    ## 1, 2, 3 -radiobutton bilan bog'landigan funksiya.
    def radiobutton1_funk(self):
        x = self.radiobutton1_var.get()
        if x == 1:
            self.asosiy_oyna.configure(bg=soz.KOK)
        elif x == 2:
            self.asosiy_oyna.configure(bg=soz.OLTIN)
        elif x == 3:
            self.asosiy_oyna.configure(bg=soz.QIZIL)

    ## 1-button bilan bog'lanadigan funksiya.
    def button1_funk(self):
        pass
        
    def _yangi_hujjat(self):
        self.yangi_hujjat_oynasi = tk.Tk()
        self.yangi_hujjat_oynasi.title("Yangi hujjat")
        self.yangi_hujjat_oynasi.geometry("600x600")
        self.yangi_hujjat_oynasi.resizable(False, False)
        ## 1-scrolledtext.
        self.a = tk.WORD
        self.scrolledtext2 = scrolledtext.ScrolledText(self.yangi_hujjat_oynasi, width=70, height=34, wrap=self.a)
        self.scrolledtext2.grid(column=0, columnspan=3, padx=20, pady=20)
        
        self.yangi_hujjat_oynasi.mainloop()
    
    def _chiqish(self):
        self.asosiy_oyna.quit()
        self.asosiy_oyna.destroy()
        exit()
    
    def _msgBox(self):
        # msg.showinfo("Python Message Info Box", "A Python GUI created using tkinter:\n The year in 2022.")
        # msg.showwarning("Python Message Warning Box", "A Python GUI created using tkinter:\nWarning: There might be a bug in this code.")
        # msg.showerror("Python Message Error Box", "A Python GUI created using tkinter:\nError: Houston ~ we DO have a serius PROBLEM!")
        answer = msg.askyesnocancel("Python Message Multi Choice Box", "Are you sure you really wish to do this?")
        print(answer)
    
    def menyu_qatori(self):
        """____"""
        
        # Menyu qatori-ni yaratish.
        self.menyu_qatori = Menu(self.asosiy_oyna)
        self.asosiy_oyna.config(menu=self.menyu_qatori)
        
        # Menyu yaratish va Menyu elementlarini qo'shish.
        self.hujjat_menyu = Menu(self.menyu_qatori, tearoff=0)  # hujjat menyusini yaratish.
        self.hujjat_menyu.add_command(label="Yangi", command=self._yangi_hujjat)  # Hujjat menyusiga element qo'shish.
        self.hujjat_menyu.add_separator()
        self.hujjat_menyu.add_command(label="Chiqish", command=self._chiqish)  # Hujjat menyusiga element qo'shish.
        self.menyu_qatori.add_cascade(label="Hujjat", menu=self.hujjat_menyu)
        
        self.yordam_menyu = Menu(self.menyu_qatori, tearoff=0)
        self.menyu_qatori.add_cascade(label="Yordam", menu=self.yordam_menyu)
        self.yordam_menyu.add_command(label="Haqida", command=self._msgBox)

    def mainloop(self):
        self.asosiy_oyna.mainloop()

        

        
