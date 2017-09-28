memory = [] 

def loadInstruction(op, strAddress, location):
    op = str(op)
    op += strAddress
    memory[location] = int(op)

def loadInstructions():
    inFile = open("instructions.txt")
    
    instructionPtr = 0
    for line in inFile:
        words = line.split(" ")
        instruction = words[0]
        if (instruction == "LDA"):
            loadInstruction(5, words[1], instructionPtr)
        elif(instruction == "STA"):
            loadInstruction(3, words[1], instructionPtr)
        elif (instruction == "ADD"):
            loadInstruction(1, words[1], instructionPtr)
        elif (instruction == "SUB"):
            loadInstruction(2, words[1], instructionPtr)
        elif (instruction == "INP\n"):
            loadInstruction(9, "01", instructionPtr)
        elif (instruction == "OUT\n"):
            loadInstruction(9, "02", instructionPtr)
        elif (instruction == "HTL\n"): 
            loadInstruction(0, "00", instructionPtr)
        instructionPtr += 1
        
    inFile.close()
    
    for instruction in memory:
        print (instruction)
        if instruction == 0:
            break;
        

        
def run():
    progCounter = 0
    instructionRegister = -1
    addressRegister = 0
    accumulator = 0

    print ("\n RUNNING \n")
    while instructionRegister != 0:
    
        instruction = memory[progCounter]
        
        instructionRegister = str(instruction)[0]
        
        
        instrStr = str(instruction)
        print (instruction)
        progCounter += 1
        
    
    

def main():
    #init the memory
    for i in range (99):
        memory.append(0)
        
    #load the instructions
    loadInstructions();
    
    #run the program
    run()
    
    
    
    

    
    
if __name__ == "__main__":
    main()