
package lmc;
import java.util.HashMap;

/**
 * Converts a string of commands into bytecode in memory
 * @author      Matthew Hopson
 * @version     1.0
 * @since       1.0
 */
public class Assembler {
    private int[] memory;
    private HashMap<String, Integer> commands;

    public Assembler(int[] memory) {
        this.memory = memory;
        commands = createCommandList();
    }

    /**
     * Creates a hash map of instructions in the LMC with their corresponding opcodes
     * @return hash map of commands in the LMC
     */
    private HashMap<String, Integer> createCommandList()
    {
        HashMap<String, Integer> commands = new HashMap<>();
        commands.put("HLT", 0);
        commands.put("ADD", 1);
        commands.put("SUB", 2);
        commands.put("STA", 3);
        commands.put("LDA", 5);
        commands.put("BRA", 6);
        commands.put("BRZ", 7);
        commands.put("BRP", 8);
        commands.put("INP", 9);
        commands.put("OUT", 9);
        commands.put("DAT", 4);

        return commands;
    }

    /**
     * Loads a single instruction into memory
     * @param memoryLocation    the location in memory to load the instruction into
     * @param opcode            the opcode of the instruction
     * @param address           the memory address to load the instruction into
     */
    private void loadInstruction(int memoryLocation, int opcode, String address)
    {
        String opcodeString = String.valueOf(opcode);
        opcodeString += address;
        memory[memoryLocation] = Integer.parseInt(opcodeString);
    }

    /**
     * Parses a line of the inputted  and puts it into memory
     * @param instructionPointer the memory location to load the line into
     */
    private void parseLine(int instructionPointer, String[] commandList)
    {
        String opcodeString = commandList[0];
        switch (opcodeString) {
            case "INP":
                loadInstruction(instructionPointer, 9, "01");
                break;
            case "OUT":
                loadInstruction(instructionPointer, 9, "02");
                break;
            case "HLT":
                loadInstruction(instructionPointer, 0, "00");
                break;
            default:
                if (commands.containsKey(opcodeString)) {
                    int opcode = commands.get(opcodeString);
                    try {
                        String address = commandList[1];
                        loadInstruction(instructionPointer, opcode, address);
                    }
                    catch (ArrayIndexOutOfBoundsException e) {
                        System.out.println(commandList[0]);
                    }
                }
                else {
                    if (opcodeString.equals("DAT")) {

                    }
                    else { //is a label

                    }
                }
        }
    }

    /**
     * Converts text file into a list of opcodes in "memory"
     * @param file the name of the file to assemble
     */
    public void assemble(String file)
    {
        String data = Util.readFile(file);
        String[] commandList = data.split("[\\r\\n]+");

        short instructionPointer = 0;
        for (String line : commandList) {
            String[] commands = line.split("\\s+");
            parseLine(instructionPointer, commands);
            instructionPointer++;
        }
    }
}