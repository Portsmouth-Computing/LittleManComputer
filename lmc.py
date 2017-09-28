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
    
    def loadInstructions(self):
        """Loads Instructions Into Memory"""
        def loadInstruction(op, strAddress, location):
            op = str(op)
            op += strAddress
            self.memory[location] = int(op)
        
        in_file = open("instructions.txt")
        instruction_ptr = 0
        for line in in_file:
            words = line.split(" ")
            instruction = words[0]
            if instruction == "LDA":
                loadInstruction(5, words[1], instruction_ptr)
            elif instruction == "STA":
                loadInstruction(3, words[1], instruction_ptr)
            elif instruction == "ADD":
                loadInstruction(1, words[1], instruction_ptr)
            elif instruction == "SUB":
                loadInstruction(2, words[1], instruction_ptr)
            elif instruction == "INP\n":
                loadInstruction(9, "01", instruction_ptr)
            elif instruction == "OUT\n":
                loadInstruction(9, "02", instruction_ptr)
            elif instruction == "HTL\n":
                loadInstruction(0, "00", instruction_ptr)
            elif instruction == "BRA": 
                loadInstruction(6, words[1], instruction_ptr)
            elif instruction == "BRZ": 
                loadInstruction(7, words[1], instruction_ptr)
            elif instruction == "BRP": 
                loadInstruction(8, words[1], instruction_ptr)

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
            print("Output:", self.accumulator)

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

            opcode = instr[0]

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
                lmcBranchAlways()
            elif self.instructionRegister == 8:
                lmcBranchAlways()
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
    lmc.loadInstructions()
    
    #run the program
    lmc.run()
    
if __name__ == "__main__":
    main()
