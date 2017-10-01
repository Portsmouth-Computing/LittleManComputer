from tkinter import *
from lmc_parser import LMCParser


class Window(Frame):
    """LMC"""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #Frame.configure(self, bg = 'black')
        Frame.grid_columnconfigure(self, 3, minsize=20)#Add a spacer
        self.master = master
        self.reset_everything()

        self.init_window()
        self.update_memory()
        self.update_counters()

    def load_instructions(self):
        """Loads Instructions Into Memory"""
        self.reset_everything()

        instructionList = self.textarea.get(1.0, END)
        instructionList.upper()
        instructionList = instructionList.split("\n") #split the string into individual instructions
        instructionList.pop(len(instructionList) - 1) #get rid of the final char, which is random space for some reason
        asmler = LMCParser()
        asmler.assemble(instructionList, self.memory)
        #update the GUI
        self.update_memory()

    def run(self):
        '''Execute the code'''
        def lmcAdd():
            self.accumulator += self.memory[self.address_register]

        def lmcSub():
            self.accumulator -= self.memory[self.address_register]

        def lmcLoad():
            self.accumulator = self.memory[self.address_register]

        def lmcStore():
            self.memory[self.address_register] = self.accumulator

        def lmcOutput(self):
            self.update_output()


        def lmcInput(self):
            print ("Please input into the input box")
            self.var = IntVar()
            self.inputarea = Text(self, height = 1, width = 5)
            self.inputbutton = Button(self, text = "Confirm",command=lambda: self.var.set(1))
            self.inputarea.grid(row = 16, column = 4)
            self.inputbutton.grid(row = 16, column = 5)

            self.inputbutton.wait_variable(self.var)
            #print("Processing", self.var)
            self.tempvar = self.inputarea.get(1.0,END)
            self.accumulator = int(self.tempvar)
            self.inputarea.delete(1.0, END)
            self.update_counters()
            self.update_memory()

        def lmcBranchAlways():
            self.program_counter = self.address_register

        def lmcBranchIfZero():
            if self.accumulator == 0:
                lmcBranchAlways()

        def lmcBranchIfZeroOrPositive():
            if self.accumulator >= 0:
                lmcBranchAlways()

        while self.instruction_register != 0:
            #split instructions into instruction and address
            #bus would move to address, take into cpu registers
            instr   = str(self.memory[self.program_counter])
            if int(instr) == 0:
                break
            opcode  = instr[0]

            if len(instr) == 3:
                address = instr[1] + instr[2]
            else:
                address = instr[1]

            self.program_counter += 1

            #push to registers
            self.instruction_register = int(opcode)
            self.address_register     = int(address)

            #interpret
            if self.instruction_register == 1:
                lmcAdd()
            elif self.instruction_register == 2:
                lmcSub()
            elif self.instruction_register == 3:
                lmcStore()
            elif self.instruction_register == 5:
                lmcLoad()
            elif self.instruction_register == 6:
                lmcBranchAlways()
            elif self.instruction_register == 7:
                lmcBranchIfZero()
            elif self.instruction_register == 8:
                lmcBranchIfZeroOrPositive()
            elif self.instruction_register == 9:
                if self.address_register == 1:
                    lmcInput(self)
                elif self.address_register == 2:
                    lmcOutput(self)
            else:
                print ("UNRECOGNISED SYMBOL: ", self.instruction_register)

    def init_window(self):
        """ Creates window and all the options"""
        self.master.title("LMC")
        self.pack(fill=BOTH, expand=1)
        self.header_label = Label(self, text="Little Man Computer")
        self.header_label.grid(row = 0, column = 0, columnspan = 3)
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
        self.assemble = Button(self, text = "Load", command = self.load_instructions)
        self.assemble.grid(row = 23, column = 0)

    def update_counters(self):       
        self.accvar = IntVar()
        self.accvar.set(self.accumulator)
        self.accumulator_label = Label(self,text="Accumulator")
        self.accumulator_label.grid(row = 1, column = 4)
        self.accumulator_value = Label(self, textvariable = self.accvar, bg = 'grey')
        self.accumulator_value.grid(row = 2, column = 4)

        self.progvar = IntVar()
        self.progvar.set(self.program_counter)
        self.prog_label = Label(self, text="Progress")
        self.prog_label.grid(row=4, column=4)
        self.prog_value = Label(self, textvariable = self.progvar, bg = 'grey')
        self.prog_value.grid(row = 5, column = 4)

        self.addressvar = IntVar()
        self.addressvar.set(self.address_register)
        self.address_label = Label(self, text="Current Address")
        self.address_label.grid(row = 7, column = 4)
        self.address_value = Label(self, textvariable = self.addressvar, bg = 'grey')
        self.address_value.grid(row = 8, column = 4)

        self.instruction_value = IntVar()
        self.instruction_value.set(self.instruction_register)
        self.instruction_label = Label(self, text = "Instruction Register")
        self.instruction_label.grid(row = 10, column = 4)
        self.instruction_value = Label(self, textvariable = self.instruction_value, bg = 'grey')
        self.instruction_value.grid(row = 11, column = 4)

    def update_output(self):
        self.output_value = IntVar()
        self.output_value.set(self.accumulator)
        self.output_label = Label(self, text = "Output")
        self.output_label.grid(row = 13, column = 4)
        self.output_value = Label(self, textvariable = self.output_value, bg = 'grey')
        self.output_value.grid(row = 14, column = 4)

    def update_memory(self):
        for x in range(0,10):
            for y in range(0,20):
                var = StringVar()
                value_var = StringVar()
                if y % 2 == 0:
                    loc_var = int((y / 2) * 10 + x)
                    var.set("Address " + str(loc_var))
                    self.memory_label = Label(self, textvariable = var)
                    self.memory_label.grid(row = 1 +(y), column = 6+(x),ipadx = 5, ipady = 2 )
                else:
                    value_var.set(self.memory[loc_var])
                    self.memory_value = Label(self, textvariable = value_var, bg = 'grey')
                    self.memory_value.grid(row = 1 +(y), column = 6+(x))

    def reset(self):
        self.textarea.delete(1.0, END)
        self.reset_everything()

    def reset_everything(self):
        self.memory                 = []
        self.program_counter        = 0
        self.instruction_register   = -1
        self.address_register       = 0
        self.accumulator            = 0
        for i in range (100):
            self.memory.append(0)

    def exit(self):
        exit()

def main():
    #Creates UI and starts
    root = Tk()
    root.geometry("1100x650")
    app = Window(master=root)
    #app.update_memory()
    app.mainloop()

if __name__ == "__main__":
    main()
