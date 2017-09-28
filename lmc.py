class LittleManComputer():
    def __init__(self):
        self.memory                 = [] 
        self.progCounter            = 0
        self.instructionRegister    = -1
        self.addressRegister        = 0
        self.accumulator            = 0
        for i in range (100):
            self.memory.append(0)
    

    def loadInstruction(self, op, strAddress, location):
        op = str(op)
        op += strAddress
        self.memory[location] = int(op)
    
    def loadInstructions(self):
        inFile = open("instructions.txt")
        
        instructionPtr = 0
        for line in inFile:
            words = line.split(" ")
            instruction = words[0]
            if (instruction == "LDA"):
                self.loadInstruction(5, words[1], instructionPtr)
            elif(instruction == "STA"):
                self.loadInstruction(3, words[1], instructionPtr)
            elif (instruction == "ADD"):
                self.loadInstruction(1, words[1], instructionPtr)
            elif (instruction == "SUB"):
                self.loadInstruction(2, words[1], instructionPtr)
            elif (instruction == "INP\n"):
                self.loadInstruction(9, "01", instructionPtr)
            elif (instruction == "OUT\n"):
                self.loadInstruction(9, "02", instructionPtr)
            elif (instruction == "HTL\n"): 
                self.loadInstruction(0, "00", instructionPtr)
            instructionPtr += 1
            
        inFile.close()
        
        print ("Instructions:")
        for instruction in self.memory:
            print (instruction)
            if instruction == 0:
                break;
            
    
            
    def run(self):
        def lmcAdd():
            self.accumulator = self.accumulator + self.memory[self.addressRegister]
            
        def lmcLoad():
            self.accumulator = self.memory[addressRegister]
        def lmcStore():
            self.memory[self.addressRegister] = self.accumulator
            
        def lmcInput():
            self.accumulator = int(input("Enter input: "))
            
        def lmcOutput():
            print (self.accumulator)
    
        print ("\n RUNNING \n")
        while self.instructionRegister != 0:
            #split instructions into instruction and address
            #bus would move to address, take into cpu registers
            instr   = str(self.memory[self.progCounter])
            if int(instr) == 0:
                break
            
            opcode  = instr[0]
            address = instr[1] + instr[2]
            self.progCounter += 1
            
            #push to registers
            self.instructionRegister = int(opcode)
            self.addressRegister     = int(address)
            
           #print ("instruction: ", self.instructionRegister, " add ", self.addressRegister)
            
            #interpret
            if (self.instructionRegister == 1):
                lmcAdd()
            if (self.instructionRegister == 3):
                lmcStore()
            if (self.instructionRegister == 5):
                lmcLoad()
            if (self.instructionRegister == 9):
                if (self.addressRegister == 1):
                    lmcInput()
                elif (self.addressRegister == 2):
                    lmcOutput()
            
    
    

def main():
    print ("\n\nLITTLE MAN COMPUTER\n\n")
    #init the memory
    lmc = LittleManComputer()
        
    #load the instructions
    lmc.loadInstructions();
    
    #run the program
    lmc.run()
    
    
    
    

    
    
if __name__ == "__main__":
    main()