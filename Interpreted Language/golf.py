import sys
fileName = "reversestring.txt"
lines = []
try:
    # fileName = sys.argv[1]
    file = open(fileName, 'r')
    lines = file.read().split("\n")

    file.close()
except Exception as error:
    print(f"Error opening file:\n{error}")
    sys.exit(0)

stack = []
pc = 0


def error(str):
    print("\n" + str + f"at  line {pc}")
    sys.exit(0)


def pop(index=-1):
    if len(stack) < 1:
        error("Error: stack underflow")
    return stack.pop(index)


while 0 <= pc < len(lines):
    parts = lines[pc].split(" ")
    instruction = parts[0]
    if instruction == "Mulligan":
        stack.append(0)
    elif instruction == "Tee-Off":
        top = pop()
        stack.append(top)
        stack.append(top)
    elif instruction == "Swing":
        top = pop()
        stack.append(top + 1)
    elif instruction == "Relief":
        a = pop()
        b = pop()
        stack.append(b - a)
    elif instruction == "Putt":
        try:
            stack.append(ord(input(" "[0])))
        except IndexError:
            stack.append(0)
    elif instruction == "Chip":
        print(chr(pop()))
    elif instruction == "Flop":
        print(int(pop()))
    elif instruction == "Punch":
        top = pop()
        if len(parts) < 2:
            error("Error: Expected argument for Punch instruction")
        try:
            line = int(parts[1]) - 1
            if top != 0:
                pc = line - 1
        except:
            error("Error: Invalid instruction argument for Punch")
    elif instruction == "Drive":
        characters = input()
        for character in characters:
            stack.append(ord(character))


    elif instruction == "Provisional":
        top = pop()
        if len(parts) < 2:
            error("Error: Expected argument for Provisional instruction")
        try:
            top += int(parts[1])
            stack.append(top)
        except:
            error("Error: Invalid instruction argument for Provisional")

    elif instruction == "Hook":
        top = pop()
        stack.insert(0, top)
    elif instruction == "Slice":
        bottom = pop(0)
        stack.append(bottom)
    elif instruction == "Lightning":
        break

    pc += 1
