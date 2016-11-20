# 9)Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


lines = []
while True:
    line= input()
    if line:
        lines.append(line.upper())
    else:
        break
print("\n".join(lines))
