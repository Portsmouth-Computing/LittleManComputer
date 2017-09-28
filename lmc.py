class LittleManComputer():
    """LMC""" 
    def __init__(self):
        self.memory                 = [] 
        self.progCounter            = 0
        self.instructionRegister    = -1
        self.addressRegister        = 0
        self.accumulator            = 0
        for i in range (100):
            self.memory.append(0)
    
    def load_instructions(self):
        """Loads Instructions Into Memory"""
        def load_instruction(op, strAddress, location):
            op = str(op)
            op += strAddress
            self.memory[location] = int(op)
        
        in_file = open("instructions.txt")
        instruction_ptr = 0
        for line in in_file:
            words = line.split(" ")
            instruction = words[0]
            if instruction == "LDA":
                load_instruction(5, words[1], instruction_ptr)
            elif instruction == "STA":
                load_instruction(3, words[1], instruction_ptr)
            elif instruction == "ADD":
                load_instruction(1, words[1], instruction_ptr)
            elif instruction == "SUB":
                load_instruction(2, words[1], instruction_ptr)
            elif instruction == "INP\n":
                load_instruction(9, "01", instruction_ptr)
            elif instruction == "OUT\n":
                load_instruction(9, "02", instruction_ptr)
            elif instruction == "HTL\n":
                load_instruction(0, "00", instruction_ptr)
            elif instruction == "BRA": 
                load_instruction(6, words[1], instruction_ptr)
            elif instruction == "BRZ": 
                load_instruction(7, words[1], instruction_ptr)
            elif instruction == "BRP": 
                load_instruction(8, words[1], instruction_ptr)

            instruction_ptr += 1
        in_file.close()
    
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
            print ("Inst: ", self.instructionRegister)
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
            
def main():
    print ("\n\nLITTLE MAN COMPUTER\n\n")
    #init the memory
    lmc = LittleManComputer()
        
    #load the instructions
    lmc.load_instructions()
    
    #run the program
    lmc.run()
    
if __name__ == "__main__":
    main()
