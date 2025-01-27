def hanoi(n: int, source: str, target: str, auxiliary: str, state: dict) -> None:
    """
    Solves the Tower of Hanoi problem and logs the sequence of steps.

    :param n: The number of disks.
    :param source: The source rod.
    :param target: The target rod.
    :param auxiliary: The auxiliary rod.
    :param state: The current state of the rods.
    """
    if n == 1:
        print(f"Move disk from {source} to {target}: {state[source][-1]}")
        state[target].append(state[source].pop())
        print(f"Intermediate state: {state}")
    else:
        hanoi(n - 1, source, auxiliary, target, state)
        print(f"Move disk from {source} to {target}: {state[source][-1]}")
        state[target].append(state[source].pop())
        print(f"Intermediate state: {state}")
        hanoi(n - 1, auxiliary, target, source, state)


def main() -> None:
    """
    Main function to initialize the Tower of Hanoi problem and start the solution.
    """
    try:
        n: int = int(input("Enter the number of disks: "))
        state = {"A": list(range(n, 0, -1)), "B": [], "C": []}
        print(f"Initial state: {state}")
        hanoi(n, "A", "C", "B", state)
        print(f"Final state: {state}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of disks.")


if __name__ == "__main__":
    main()
