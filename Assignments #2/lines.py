import sys
import os

def main():
    
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Get the file name and check extension
    file = sys.argv[1]
    if not file.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if file exists
    if not os.path.exists(file):
        sys.exit("File does not exist")

    try:
        # Count lines, excluding comments and blank lines
        count = 0
        with open(file) as x:
            for line in x:
                line = line.lstrip()
                if line and not line.startswith("#"):
                    count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")

main()
