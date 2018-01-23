package lmc;

public class LittleManComputer
{
    int[] memory;

    int programCounter;
    int instructionRegister;
    int addressRegister;
    int accumulator;

    public LittleManComputer(String file)
    {
        memory = new int[100]; //LMC has 100 memory locations
        programCounter = 0;
        instructionRegister = -1;
        addressRegister = 0;
        accumulator = 0;

        Assembler assembler = new Assembler(memory);
        assembler.assemble(file);
    }

    /**
     * runs the computer
     */
    public void run()
    {
        while(instructionRegister != 0) {
            if (!fetchNextInstruction()) {
                break;
            }
            System.out.printf("Instruction: %d, Address: %d\n", instructionRegister, addressRegister);
        }
    }

    /**
     * Loads the next instruction into the registers
     * @return whether or not it is the end of the instructions
     */
    private boolean fetchNextInstruction()
    {
        int opcode = memory[programCounter++];
        String opString = String.valueOf(opcode);

        String instruction = "" + opString.charAt(0);
        if (instruction.equals("0")) {
            return false;
        }
        String address     = "" + opString.charAt(1) + opString.charAt(2);

        instructionRegister = Integer.parseInt(instruction);
        addressRegister     = Integer.parseInt(address);
        return true;
    }
}
