import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    # Default values (used in VS Code)
    a = 2
    b = 3

    # Override defaults if arguments are passed (used in Jenkins)
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

    print(f"Result: {add(a, b)}")
