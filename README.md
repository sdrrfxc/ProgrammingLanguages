# Interpreted Language

## Key Features:

Stack Based

Variables

- These should be able to store some value

Control structures:

- if
- else
- for
- while

## Instructions
| Mulligan  | Push 0 onto the stack |
| --- | --- |
| Tee-Off | Duplicate top stack value |
| Swing | Add one to top stack value |
| Relief | Pops A and then B from the stack and pushes B - A to the stack |
| Putt | Take one character of input and push it’s ascii code to the stack |
| Chip | Pop the top value of the stack and print it as an ascii character |
| Flop | Pop the top value of the stack and print it as an integer |
| Punch n | Pops the top of the stack, if it is non-zero this instruction jumps to the nth line |
| Provisional n | Pops the top of the stack and adds the n value and pushes to the top |
| Hook | Pop the top of the stack and push it to the bottom |
| Slice | Remove the bottom value of the stack and push it to the top |
| Drive | Take string of input and push ascii characters of each character to the stack |
| Lightning | Terminate program execution |
