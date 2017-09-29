# Little Man Computer
#### Python version of: https://peterhigginson.co.uk/LMC/

| Instruction        | Mnemonic | Machine Code  | Info                                                                                         | Example        |
|--------------------|----------|---------------|----------------------------------------------------------------------------------------------|----------------|
| End                | HLT      | 000           | Ends the program                                                                             | HLT            |
| Add                | ADD      | 1xx           | Adds the value at address xx to the accumulator                                              | ADD 50         |
| Subtract           | SUB      | 2xx           | Subtracts the value at address xx from accumulator                                           | SUB 50         |
| Store              | STA      | 3xx           | Storecontents of accumulator to address xx                                                   | STA 50         |
| Load               | LDA      | 5xx           | Loads contents of address xx to the accumulator                                              | LDA 50         |
| Branch Always      | BRA      | 6xx           | Jumps to the instruction at address xx                                                       | BRA 05         |
| Branch If Zero     | BRZ      | 7xx           |  Jumps to the instruction at address xx, given the value  in the accumulator is 0            | BRZ 05         |
| Branch If Positive | BRP      | 8xx           | Jumps to the instruction at address xx, given the value  in the accumulator is 0, or greater | BRP 05         |
| Input              | INP      | 901           | Prompts user for input, store in accumulator                                                 | INP            |
| Output             | OUT      | 902           | Outputs value currently in accumulator                                                       | OUT            |
| Data               | DAT      | -             | ???                                                                                          | VarName DAT 50 |      