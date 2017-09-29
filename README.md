# Little Man Computer
#### Python version of: LMC by [Peter Higginson](https://peterhigginson.co.uk/LMC/)

Modern computers contain a processor which executes instructions and memory which stores both the instructions and also the data that is to be used. In addition there are various means both to give data to the computer and to receive information from it. Although The Little Man Computer is a simulation of how a computer works. It is a heavily simplified version of a computer from the one that sits on your desk but nonetheless it is an excellent tool to learn how a computer works. from You will recall that a computer has various components including means to input data, output information, carry out calculations and store results.



| Instruction        | Mnemonic | Machine Code  | Info                                                                                         | Example        |
|--------------------|----------|---------------|----------------------------------------------------------------------------------------------|----------------|
| End                | HLT      | 000           | Ends the program                                                                             | HLT            |
| Add                | ADD      | 1xx           | Adds the value at address xx to the accumulator                                              | ADD 50         |
| Subtract           | SUB      | 2xx           | Subtracts the value at address xx from accumulator                                           | SUB 50         |
| Store              | STA      | 3xx           | Storecontents of accumulator to address xx                                                   | STA 50         |
| Load               | LDA      | 5xx           | Loads contents of address xx to the accumulator                                              | LDA 50         |
| Branch Always      | BRA      | 6xx           | Jumps to the instruction at address xx                                                       | BRA 05         |
| Branch If Zero     | BRZ      | 7xx           | Jumps to the instruction at address xx, given the value  in the accumulator is 0             | BRZ 05         |
| Branch If Positive | BRP      | 8xx           | Jumps to the instruction at address xx, given the value  in the accumulator is 0, or greater | BRP 05         |
| Input              | INP      | 901           | Prompts user for input, store in accumulator                                                 | INP            |
| Output             | OUT      | 902           | Outputs value currently in accumulator                                                       | OUT            |
| Data               | DAT      | -             | ???                                                                                          | VarName DAT 50 |

### How to use LMC
1. The 100 memory addresses in the computer memory are numbered 0 to 99 and can each contain a 'machine code' instruction or data.
2. Each assembly language instruction is made up of a 3 letter mnemonic (which represents the operation code), usually followed by the memory address of the data the CPU is to act on (this is called absolute memory addressing).
3. Pressing the Assemble Program button translates the assembly language instructions into 'machine code' and loads them into RAM. it also resets the Program Counter to zero.
4. The Input box allows the user to enter numerical data (-999 to 999) while a program is running and load it into the accumulator.
5. The Output box can output the contents of the accumulator while a program is running.
6. A RAM memory address that is used to store data can be given a meaningful label. Data can also be stored in these named address locations.
7. The results of any ADD or SUBTRACT instructions are stored in the accumulator .
8. The Program Counter stores the memory address of the instruction being carried out. It will automatically increment by 1 after each instruction is completed.
9. If the CPU receives an non-sequential instruction to branch (BRP, BRP or BRZ) then the Program Counter is set to the memory address of that instruction.
10. Branch instructions are set to branch to a labelled memory location.
11. To restart a program, the Program Counter is reset to 0.

[Reference](https://gcsecomputing.org.uk/lmc/)