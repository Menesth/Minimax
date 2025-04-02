import random

def find_random_move(validmoves):
    return validmoves[random.randint(0, len(validmoves) - 1)]