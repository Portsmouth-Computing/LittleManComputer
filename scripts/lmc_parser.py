def remove_empty(arr):
    arr = filter(None, arr)

class LMCParser:
    '''Class to parse LMC instructions and assemble into machine code'''
    def __init__(self):
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
                            "DAT": 4}
        self.labels = dict()

    def get_labels(self, command_list):
        '''parse commands and extract the labels'''
        instruction_ptr = 0
        for line in command_list:
            words = line.split(" ")
            remove_empty(words)
            if not words[0] in self.commands:
                self.labels[words[0]] = instruction_ptr #insert label
            instruction_ptr += 1

    def load_instruction(self, memory, op_code, ref_address, mem_location):
        '''loads up a single instruction'''
        memory_address = 0
        try:
            memory_address = int(ref_address)
        except ValueError:
            memory_address = self.labels[ref_address]
        memory[mem_location] = int(str(op_code) + str(memory_address))

    def parse_line(self, line, memory_location, memory):
        '''Parse a single line of instructions eg `BEGIN STA 50`'''
        remove_empty(line)
        instruction = line[0]
        if instruction == "INP":
            self.load_instruction(memory, 9, "01", memory_location)
        elif instruction == "OUT":
            self.load_instruction(memory, 9, "02", memory_location) #INP, OUT, and HLT are special cases, as they do not have an address to manip
        elif instruction == "HLT":
            self.load_instruction(memory, 0, "00", memory_location)
        else:
            if instruction in self.commands:
                self.load_instruction(memory, self.commands[instruction], line[1], memory_location)
            else:
                if (line[1] == "DAT"): #Dat, takes the form of NAME DAT INITAL VALUE
                    if(len(line) == 2):
                        memory[memory_location] = 0 #a value is optional, so default to 0
                    else: 
                        memory[memory_location] = int(line[2])    
                else: #this means it is a label, so pop that out and reparse the line
                    line.pop(0)
                    self.parse_line(line, memory_location, memory)

    def assemble(self, command_list, memory):
        '''Take the list of commands and converts it into Op code in memory'''
        self.get_labels(command_list)

        instruction_ptr = 0
        for line in command_list:
            commands = line.split(" ")
            self.parse_line(commands, instruction_ptr, memory)
            instruction_ptr += 1
