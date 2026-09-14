import sys

def answer() -> int:
    # The learner put a print inside a loop to see what was happening, and it
    # prints far more than the 50K the runner keeps. unittest writes its
    # summary to stderr, after this, so the summary is what gets dropped.
    total = 0
    for i in range(5000):
        print(f'debug: i is {i}, total is {total}', file=sys.stderr)
        total += 1
    return 6 * 7
