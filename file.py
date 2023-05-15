import sys
# Task 2
# Design Recipe
# 1) read a file, for each line print the total of the line, account for many errors that could happen
# 2) no input or outputs only the info from the file given
# 3) template of function
#   - open the file name for read
#   - go through each line
#   - strip and split the line in order to access each value
#   - if the length of the line is not two then print an error
#   - make a try statement to make the values into floats
#   - except an error if there is one
# 4) test case:
# 5)

if len(sys.argv) < 2:
    print("Error: Not a File name")
    sys.exit(1)
try:
    fil = sys.argv[1]
    with open(fil) as file:
        for line in file:
            values = line.strip().split()
            if len(values) != 2:
                print(f"Error: line format - {line.strip()}")
                continue
            try:
                a = float(values[0])
                b = float(values[1])
                print(a + b)
            except ValueError:
                print(f"Error: cant be turned float - {line.strip()}")
except FileNotFoundError:
    print("Error: File not found")
    sys.exit(1)
except IOError as e:
    print(f"Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
