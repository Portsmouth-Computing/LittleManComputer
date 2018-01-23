package lmc;

import java.util.HashMap;
import java.util.Map;

public class Assembler {
    private int[] memory;
    private HashMap<String, Integer> commands;

    public Assembler(int[] memory) {
        this.memory = memory;
        commands = createCommandList();
    }

    private HashMap<String, Integer> createCommandList()
    {
        HashMap<String, Integer> commands = new HashMap<>();
        commands.put("HLT", 0);
        commands.put("ADD", 1);
        commands.put("SUB", 2);
        commands.put("STA", 4);
        commands.put("LDA", 5);
        commands.put("BRA", 6);
        commands.put("BRZ", 7);
        commands.put("BRP", 8);
        commands.put("INP", 9);
        commands.put("OUT", 9);
        commands.put("DAT", 4);

        return commands;
    }

    private void loadInstruction(int memoryLocation, int opcode, String address)
    {
        String opcodeString = String.valueOf(opcode);
        opcodeString += address;
        memory[memoryLocation] = Integer.parseInt(opcodeString);
    }

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
