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
public final class LittleManComputer
{
    int[] memory;
    Registers register;
    UserInterface userInterface;

    final Scanner consoleInput;

    public LittleManComputer(String file)
    {
        memory          = new int[100]; //LMC has 100 memory locations
        register        = new Registers();
        userInterface   = new UserInterface(memory, register);
        consoleInput    = new Scanner(System.in);

        new Assembler(memory).assemble(file);
    }

    /**
     * runs the computer
     */
    public void run()
    {
        while(register.instruction != 0) {
            if (!fetchNextInstruction()) {
                break;
            }
            executeInstruction();
            //System.out.printf("Instruction: %d, Address: %d\n", instructionRegister, addressRegister);
        }
    }

    /**
     * Loads the next instruction into the registers
     * @return whether or not it is the end of the instructions
     */
    private boolean fetchNextInstruction()
    {
        int opcode = memory[register.programCounter++];
        String opString = String.valueOf(opcode);

        String instruction = "" + opString.charAt(0);
        if (instruction.equals("0")) {
            return false;
        }
        String address;
        try {
            address = "" + opString.charAt(1) + opString.charAt(2);
        } catch (StringIndexOutOfBoundsException e ) {
            address = "" + opString.charAt(1);
        }

        register.instruction = Integer.parseInt(instruction);
        register.address     = Integer.parseInt(address);
        return true;
    }

    private void add()
    {
        register.accumulator += memory[register.address];
    }

    private void subtract()
    {
        register.accumulator -= memory[register.address];
    }

    private void store()
    {
        memory[register.address] = register.accumulator;
    }

    private void load()
    {
        register.accumulator = memory[register.address];
    }

    private void branch(boolean condition)
    {
        if (condition) {
            register.programCounter = register.address;
        }
    }

    private void input()
    {
        System.out.print("Please enter a value: ");
        register.accumulator = consoleInput.nextInt();
    }

    private  void output()
    {
        System.out.println("Accumulator: " + register.accumulator);
    }


    /**
     * Executes the instruction at the
     * @return whether or not it is the end of the instructions
     */
    private void executeInstruction()
    {
        switch (register.instruction) {
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
                branch(register.accumulator == 0);
                break;
            case 8:
                branch(register.accumulator >= 0);
                break;
            case 9:
                switch (register.address) {
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
