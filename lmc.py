from tkinter import *
import random , time

class Command():
    def __init__(self):
        self.label      = " "
        self.command    = " "
        self.address    = " "

class Window(Frame):

    """LMC""" 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        #Frame.configure(self, bg = 'black')
        Frame.grid_columnconfigure(self, 3, minsize=20)#Add a spacer
        Frame.grid_columnconfigure(self, 5, minsize=20)

        self.master = master
      
        self.memory                 = [] 
        self.progCounter            = 0
        self.instructionRegister    = -1
        self.addressRegister        = 0
        self.accumulator            = 0
        self.labels                 = dict()
        for i in range (100):
            self.memory.append(0)
    
        self.init_window()
        self.update_memory()
        self.update_counters()

        self.commands = {   "HTL": 0, 
                            "ADD": 1,
                            "SUB": 2,
                            "STA": 3,
                            "LDA": 5,
                            "BRA": 6,
                            "BRZ": 7,
                            "BRP": 8,
                            "INP": 9,
                            "OUT": 9,
                            "DAT": 4} #temp

    def load_instructions(self):
        """Loads Instructions Into Memory"""
        
        instructionList = self.textarea.get(1.0, END)
        instructionList.upper()
        instructionList = instructionList.split("\n")
        
        instructionList.pop(len(instructionList) - 1)
        #first pass, find labels
        instruction_ptr = 0
        for line in instructionList:
            words = line.split(" ")
            if not words[0] in self.commands:
                self.labels[words[0]] = instruction_ptr
                print ("Found: ", words[0])
            instruction_ptr += 1

        #second pass, actually set up the memory
        def load_instruction(op, strAddress, location): #int, str, int
            '''Loads up a single instruction'''
            memAddress = 0
            try:
                memAddress = int(strAddress)
            except ValueError:
                memAddress = self.labels[strAddress]
            self.memory[location] = int(str(op) + str(memAddress))

        def parse(words, memLocation):
            instruction = words[0]
            if instruction == "ADD":
                load_instruction(1, words[1], memLocation)
            elif instruction == "SUB":
                load_instruction(2, words[1], memLocation)
            elif instruction == "STA":
                load_instruction(3, words[1], memLocation)
            elif instruction == "LDA":
                load_instruction(5, words[1], memLocation)
            elif instruction == "BRA": 
                load_instruction(6, words[1], memLocation)
            elif instruction == "BRZ": 
                load_instruction(7, words[1], memLocation)
            elif instruction == "BRP": 
                load_instruction(8, words[1], memLocation)
            elif instruction == "INP":
                load_instruction(9, "01", memLocation)
            elif instruction == "OUT":
                load_instruction(9, "02", memLocation)
            elif instruction == "HLT":
                load_instruction(0, "00", memLocation)
            else:
                self.labels[instruction] = memLocation
                if (words[1] == "DAT"): #Dat, takes the form of NAME DAT INITAL VALUE
                    if(len(words) == 2):
                        self.memory[memLocation] = 0
                    else: 
                        self.memory[memLocation] = int(words[2])    
                else:
                    words.pop(0)
                    parse(words, memLocation)

        instruction_ptr = 0
        for line in instructionList:
            words = line.split(" ")
            parse(words, instruction_ptr)
            instruction_ptr += 1
            
        #update the GUI
        self.update_memory()

    def run(self):
        """Execute the code"""
        def lmcAdd():
            self.accumulator += self.memory[self.addressRegister]
            
        def lmcSub():
            self.accumulator -= self.memory[self.addressRegister]

        def lmcLoad():
            self.accumulator = self.memory[self.addressRegister]

        def lmcStore():
            self.memory[self.addressRegister] = self.accumulator
            
        def lmcInput():
            self.accumulator = int(input("Enter input: "))
            
        def lmcOutput():
            print ("Output:", self.accumulator)

        def lmcBranchAlways():
            self.progCounter = self.addressRegister

        def lmcBranchIfZero():
            if self.accumulator == 0:
                lmcBranchAlways()

        def lmcBranchIfZeroOrPositive():
            if self.accumulator >= 0:
                lmcBranchAlways()

        print ("\n RUNNING \n")
        while self.instructionRegister != 0:
            #split instructions into instruction and address
            #bus would move to address, take into cpu registers
            instr   = str(self.memory[self.progCounter])
            if int(instr) == 0:
                break
            opcode  = instr[0]

            if len(instr) == 3:
                address = instr[1] + instr[2]
            else:
                address = instr[1]

            self.progCounter += 1
            
            #push to registers
            self.instructionRegister = int(opcode)
            self.addressRegister     = int(address)

            print ("Inst: ", self.instructionRegister)
            
            #interpret
            if self.instructionRegister == 1:
                lmcAdd()
            elif self.instructionRegister == 2:
                lmcSub()
            elif self.instructionRegister == 3:
                lmcStore()
            elif self.instructionRegister == 5:
                lmcLoad()
            elif self.instructionRegister == 6:
                lmcBranchAlways()
            elif self.instructionRegister == 7:
                lmcBranchIfZero()
            elif self.instructionRegister == 8:
                lmcBranchIfZeroOrPositive()
            elif self.instructionRegister == 9:
                if self.addressRegister == 1:
                    lmcInput()
                elif self.addressRegister == 2:
                    lmcOutput()
            else:
                print ("UNRECOGNISED SYMBOL: ", self.instructionRegister)
            
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
        self.randmem = Button(self, text = "randmem", command = self.update_random_mem)
        self.randmem.grid(row = 23, column = 2)
        self.assemble = Button(self, text = "Load", command = self.load_instructions)
        self.assemble.grid(row = 23, column = 0)


    def update_counters(self):
        self.accumulator_label = Label(self,text="Accumulator")
        self.accumulator_label.grid(row = 1, column = 4)
        self.accumulator_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.accumulator_value.grid(row = 2, column = 4)

        self.prog_label = Label(self, text="Progress")
        self.prog_label.grid(row=4, column=4)
        self.prog_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.prog_value.grid(row = 5, column = 4)
        
        self.address_label = Label(self, text="Current Address")
        self.address_label.grid(row = 7, column = 4)
        self.address_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.address_value.grid(row = 8, column = 4)

        self.instruction_label = Label(self, text = "Instruction Register")
        self.instruction_label.grid(row = 10, column = 4)
        self.instruction_value = Label(self, text = "<<<Insert Value here>>>", bg = 'grey')
        self.instruction_value.grid(row = 11, column = 4)
        
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
        
    def exit(self):
        exit()

    def update_random_mem(self):
        for x in range(0,100):
            self.memory[x] = random.randint(0,999)
        self.update_memory()

def main():
    print ("\n\nLITTLE MAN COMPUTER\n\n")

    #Creates UI and starts
    root = Tk()
    root.geometry("1100x650")
    app = Window(master=root)
    #app.update_memory()
    app.mainloop()
    
if __name__ == "__main__":
    main()
