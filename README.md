#Assembler_Simulator

This repository holds the project for Computer Architecture course. This project is a code to understand the working of memory of a 
assembly code in a CISC Architecture model of machine. Opcode for various instructions were given and we had to plot graphs for the memory locations
after every instruction.

The Project is divided into 2 parts Assembler and Simulotor

1.Assembler
	This part of the project converts the assembly code into the machine code acccording to the given architecture. It also handles the error test cases and asserts 
	error accoriding to the type of error in the assebly code. The machine code is the code that is interpreted by the system to perform the operations accordingly.

2.Simulator
	This part of the project reads the machine code which is the binary code and interprets the operationn and allocate memory accordingly and performs the operation
	and outputs the final value of the memory adresses and the value stored in them after the instructions have been executed.
	
There is also the bonus part of the project which is to plot the graph of how the memory changes while the operations are being simulated in the machine.

INSTRUCTIONS FOR RUN FILE: All the run files need to be granted permission/privelidge for execution.
Eg. for Linux-systems, go to the folder of each run file using bash/terminal and write "chmod +x run" {without quotes}.

To run the results for your assembler, go to Automated Testing folder and open bash/terminal.
Assuming you have granted required permisions to the run file, type "./run --no-sim" {without quotes}.

To run the results for your simulator, go to Automated Testing folder and open bash/terminal.
Assuming you have granted required permisions to the run file, type "./run --no-asm" {without quotes}.

To run the results for both,, the assembler and the simulator, go to Automated Testing folder and open bash/terminal.
Assuming you have granted required permisions to the run file, type "./run" or "./run --verbose" [for verbose output] {without quotes}.

_________________________________________________________________________________________________________________________________________________________________________
