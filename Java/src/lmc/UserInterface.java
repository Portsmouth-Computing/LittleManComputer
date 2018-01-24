package lmc;

import javax.swing.*;

public class UserInterface extends JFrame
{
    private int[] memoryRef;
    private Registers registerRef;

    public UserInterface(int[] memory, Registers registers)
    {
        memoryRef   = memory;
        registerRef = registers;
        initUI();

    }

    private void initUI()
    {
        setTitle("Little Man Computer - By Matthew Hopson");
        setSize(1280, 720);
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        setVisible(true);

    }
}
