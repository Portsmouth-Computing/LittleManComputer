package lmc;

public class LittleManComputer
{
    int[] memory;

    public LittleManComputer(String file)
    {
        memory = new int[100]; //LMC has 100 memory locations

        Assembler assembler = new Assembler(memory);
        assembler.assemble(file);
        for (int i = 0; i < 20; i++) {
            System.out.println(memory[i]);
        }
    }
}
