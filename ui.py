from tkinter import *


class Window(Frame):
    """Creates window for input of LMC"""
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("LMC")
        self.pack(fill =BOTH, expand = 1)
        self.header_label = Label(self, text = "Little Man Computer")
        self.header_label.grid(row = 0, column = 0, columnspan = 3 )
        
        # Create text box
        self.textarea = Text(self,width = 20, height = 35)
        #self.textarea.pack(expand=NO, fill ="y")
        self.textarea.grid(row = 1, column = 0, columnspan = 3)

        self.execute_button = Button(self, text = "Execute", command = self.run)
        self.execute_button.grid(row = 2, column = 0)
        self.reset_button = Button(self, text = "Reset", command = self.reset)
        self.reset_button.grid(row = 2, column = 1)
        self.burn_it_all = Button(self, text = "Exit", command = self.exit)
        self.burn_it_all.grid(row = 2, column = 2)


        #execute_button = Button(self,text="Test",command = self.run())
        #execute_button.place(x = 10, y = 5)


    def run(self):
        print(self.textarea.get(1.0, END))
        #exit() # repalce this with actual computation of task

    def reset(self):
        self.textarea.delete(1.0, END)
        
    def exit(self):
        exit()

root = Tk()

root.geometry("500x700")
app = Window(master=root)
app.mainloop()
