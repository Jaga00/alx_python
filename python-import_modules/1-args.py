#  program that prints the number of and the list of its arguments.

import sys

def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print(f"{num_arguments} {'argument' if num_arguments == 1 else 'arguments'}:", end=" ")

    if num_arguments == 0:
        print("")
    else:
        print()

        for index, arg in enumerate(arguments, 1):
            print(f"{index}: {arg}")

if __name__ == "__main__":
    main()