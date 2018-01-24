package lmc;

import java.io.Console;
import java.util.Scanner;
import java.util.logging.ConsoleHandler;

/**
 * The LittleManComputer itself
 * @author      Matthew Hopson
 * @version     1.0
 * @since       1.0
 */
public class LittleManComputer
{
    int[] memory;

    int programCounter;
    int instructionRegister;
    int addressRegister;
    int accumulator;

    Scanner consoleInput;

    public LittleManComputer(String file)
    {
        consoleInput    = new Scanner(System.in);
        memory          = new int[100]; //LMC has 100 memory locations
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
            executeInstruction();
            System.out.printf("Instruction: %d, Address: %d\n", instructionRegister, addressRegister);
        }

        for (int i  = 0; i < 100; i++) {
            System.out.printf("Memory %d: %d\n", i, memory[i]);
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

    private void add()
    {
        accumulator += memory[addressRegister];
    }

    private void subtract()
    {
        accumulator -= memory[addressRegister];
    }

    private void store()
    {
        memory[addressRegister] = accumulator;
    }

    private void load()
    {
        accumulator = memory[addressRegister];
    }

    private void branch(boolean condition)
    {
        if (condition) {
            //TODO
        }
    }

    private void input()
    {
        System.out.print("Please enter a value: ");
        accumulator = consoleInput.nextInt();
    }

    private  void output()
    {
        System.out.println("Accumulator: " + accumulator);
    }


    /**
     * Executes the instruction at the
     * @return whether or not it is the end of the instructions
     */
    private void executeInstruction()
    {
        switch (instructionRegister) {
            case 1:
                add();
                break;
            case 2:
                subtract();
                break;
            case 3:
                store();
                break;
            case 4:
                System.out.println("Unknown command");
                break;
            case 5:
                load();
                break;
            case 6:
                branch(true);
                break;
            case 7:
                branch(accumulator == 0);
                break;
            case 8:
                branch(accumulator > 0);
                break;
            case 9:
                switch (addressRegister) {
                    case 1:
                        input();
                        break;
                    case 2:
                        output();
                        break;
                }
                break;
        }
    }
}
