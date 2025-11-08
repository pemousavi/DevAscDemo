import sys

#!/usr/bin/env python3
"""
Tower of Hanoi - recursive solution
Saves moves to console and prints total move count.
"""


def hanoi(n: int, src: str, dst: str, aux: str):
    """Yield moves as tuples (disk, from, to)."""
    if n <= 0:
        return
    if n == 1:
        yield (1, src, dst)
    else:
        yield from hanoi(n - 1, src, aux, dst)
        yield (n, src, dst)
        yield from hanoi(n - 1, aux, dst, src)

def main():
    # Allow optional command-line argument
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Usage: TowerOfHanoi.py [number_of_disks]")
            return
    else:
        try:
            n = int(input("Enter number of plates (positive integer): ").strip())
        except Exception:
            print("Invalid input.")
            return

    if n <= 0:
        print("Number of plates must be a positive integer.")
        return

    move_count = 0
    for disk, frm, to in hanoi(n, "A", "C", "B"):
        move_count += 1
        print(f"Move {move_count}: move disk {disk} from {frm} -> {to}")

    print(f"Total moves: {move_count} (expected {2**n - 1})")

if __name__ == "__main__":
    main()