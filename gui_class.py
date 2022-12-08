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
        
        # Asosiy oyna sozlamalari.

        ## Asosiy oyna orqa fon rangini belgilash.
        self.asosiy_oyna.configure(bg=soz.asosiy_oyna_orqa_fon_rangi)

    def tab_control(self):
        """____"""
        
        # 1-notebook.
        self.tab_control = ttk.Notebook(self.asosiy_oyna)  # Create Tab Control.
        
        # 1-tab.
        self.tab1 = ttk.Frame(self.tab_control)  # Create a tab.
        self.tab_control.add(self.tab1, text="Tab 1")  # Add the tab.
        
        # 2-tab.
        self.tab2 = ttk.Frame(self.tab_control)  # Create a tab.
        self.tab_control.add(self.tab2, text="Tab 2")  # Add the tab.
        
        self.tab_control.pack(expand=1, fill="both")
    
    def mighty(self):
        """"____"""
        
        # 1-mighty.
        self.mg = ttk.LabelFrame(self.tab1, text=" Mighty Python ")
        self.mg.grid(column=0, row=0, padx=10, pady=10)
    
    def widjetlar(self):
        """_______"""

        # 1-widjet turi: Label.

        ## 1-label.
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="white", background="black")
        self.lb = ttk.Label(self.mg, width=12, text="1-label", style="BW.TLabel")
        self.lb.grid(column=0, row=0, padx=4, pady=4)

        # 2-widjet turi: Button.
        
        ## 1-button.
        self.bt = ttk.Button(self.mg, text="OK", command=self.bt_funk)
        self.bt.grid(column=2, row=0, padx=4, pady=4)
        
        # 3-widjet turi: Entry.

        ## 1-entry.
        self.et_str = tk.StringVar()
        self.et = ttk.Entry(self.mg, width=12, textvariable=self.et_str)
        self.et.grid(column=1, row=0)
        
        ### 1-entry-ga focus-ni o'ratish.
        self.et.focus()

        # 4-widjet turi: Combobox.

        ## 1-combobox.
        self.cb_str = tk.StringVar()
        self.cb = ttk.Combobox(self.mg, width=12, textvariable=self.cb_str)
        self.cb["values"] = (1996, 1997, 1998, 1999, 2000)
        self.cb.grid(column=0, row=1)
        self.cb.current(0)

        ## 2-combobox.
        self.cb1_str = tk.StringVar()
        self.cb1 = ttk.Combobox(self.mg, width=12, textvariable=self.cb1_str, state="readonly")
        self.cb1["values"] = (1996, 1997, 1998, 1999, 2000)
        self.cb1.grid(column=1, row=1)
        self.cb1.current(0)

        # 5-widjet turi: Checkbutton.

        ## 1-checkbutton.
        self.ch_var = tk.IntVar()
        self.ch = tk.Checkbutton(self.mg, text="Nofaol", variable=self.ch_var, state=soz.NOFAOL)
        self.ch.select()
        self.ch.grid(column=0, row=3, sticky=soz.CHAP)

        ## 2-checkbutton.
        self.ch1_var = tk.IntVar()
        self.ch1 = tk.Checkbutton(self.mg, text="Belgilanmagan", variable=self.ch1_var)
        self.ch1.deselect()
        self.ch1.grid(column=1, row=3, sticky=soz.CHAP)

        ## 3-checkbutton.
        self.ch2_var = tk.IntVar()
        self.ch2 = tk.Checkbutton(self.mg, text="Faol", variable=self.ch2_var)
        self.ch2.select()
        self.ch2.grid(column=2, row=3, sticky=soz.ONG)

        # 6-widjet turi: Radiobutton.

        ## 1-radiobutton.
        self.rb_var = tk.IntVar()
        self.rb = tk.Radiobutton(self.mg, text="Ko'k", variable=self.rb_var, value=1, command=self.rb_funk)
        self.rb.grid(column=0, row=5, sticky=soz.CHAP, columnspan=3)

        ## 2-radiobutton.
        self.rb2 = tk.Radiobutton(self.mg, text="Oltin", variable=self.rb_var, value=2, command=self.rb_funk)
        self.rb2.grid(column=1, row=5, sticky=soz.CHAP, columnspan=3)

        ## 3-radiobutton.
        self.rb3 = tk.Radiobutton(self.mg, text="Qizil", variable=self.rb_var, value=3, command=self.rb_funk)
        self.rb3.grid(column=2, row=5, sticky=soz.CHAP, columnspan=3)

        # 7-widjet turi: ScrolledText.

        ## 1-scrolledtext.
        self.a = tk.WORD
        self.st = scrolledtext.ScrolledText(self.mg, width=30, height=3, wrap=self.a)
        self.st.grid(column=0, columnspan=3)
        
    # widjetlar bilan bo'g'lanadigan funksiyalar.

    ## 1, 2, 3 -radiobutton bilan bog'landigan funksiya.
    def rb_funk(self):
        x = self.rb_var.get()
        if x == 1:
            self.asosiy_oyna.configure(bg=soz.KOK)
        elif x == 2:
            self.asosiy_oyna.configure(bg=soz.OLTIN)
        elif x == 3:
            self.asosiy_oyna.configure(bg=soz.QIZIL)

    ## 1-button bilan bog'lanadigan funksiya.
    def bt_funk(self):
        pass

    def _yangi_hujjat(self):
        self.yangi_hujjat_oynasi = tk.Tk()
        self.yangi_hujjat_oynasi.title("Yangi hujjat")
        self.yangi_hujjat_oynasi.geometry("600x600")
        self.yangi_hujjat_oynasi.resizable(False, False)
        ## 1-scrolledtext.
        self.a = tk.WORD
        self.st1 = scrolledtext.ScrolledText(self.yangi_hujjat_oynasi, width=70, height=34, wrap=self.a)
        self.st1.grid(column=0, columnspan=3, padx=20, pady=20)
        
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

        

        
