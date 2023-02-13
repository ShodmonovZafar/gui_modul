import gui_class

def gui_main_funksiyasi():
    
    
    my_gui = gui_class.Gui()
    
    my_gui.menyu_qatori()
    my_gui.notebook()
    my_gui.label_frame()
    my_gui.widjetlar()
    #my_gui.css()
    
    
    my_gui.mainloop()

if __name__ == "__main__":
    gui_main_funksiyasi()
