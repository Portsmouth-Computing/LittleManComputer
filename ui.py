from tkinter import *


class Window(Frame):
    """Creates window for input of LMC"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #Frame.configure(self, bg = 'black')
        Frame.grid_columnconfigure(self,3,minsize = 20) # Add a spacer
        self.master = master
        self.init_window()
        self.accumulator = 0

    def init_window(self):
        """ craetes window and all the options"""
        self.master.title("LMC")
        self.pack(fill=BOTH, expand=1)
        self.header_label = Label(self, text = "Little Man Computer")
        self.header_label.grid(row = 0, column = 0, columnspan = 3 )
        
        # Create text box
        self.textarea = Text(self,width = 20, height = 35)
        #self.textarea.pack(expand=NO, fill ="y")
        self.textarea.grid(row = 1, column = 0, columnspan = 3, rowspan = 20)

        self.execute_button = Button(self, text = "Execute", command = self.run)
        self.execute_button.grid(row = 22, column = 0)
        self.reset_button = Button(self, text = "Reset", command = self.reset)
        self.reset_button.grid(row = 22, column = 1)
        self.burn_it_all = Button(self, text = "Exit", command = self.exit)
        self.burn_it_all.grid(row = 22, column = 2)

        self.accumulator_label = Label(self,text="Accumulator", bg = 'grey')
        self.accumulator_label.grid(row = 1, column = 4)
        self.accumulator_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.accumulator_value.grid(row = 2, column = 4)

        self.prog_label = Label(self,text="Progress")
        self.prog_label.grid(row = 4, column = 4)
        self.prog_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.prog_value.grid(row = 5, column = 4)
        
        self.address_label = Label(self,text="Current Address")
        self.address_label.gird(row = 7, column = 4)
        self.address_value.Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.address_value.grid(row = 8, column = 4)

        self.instruction_label = Label(self, text = "Instruction Register")
        self.instruction_label.grid(row = 10, column = 4)
        self.instruction_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.instruction_value.grid(row = 11, column = 4)


        

    def run(self):
        """Execute the computation"""
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
