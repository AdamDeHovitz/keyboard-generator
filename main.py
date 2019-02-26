import random
from simanneal import Annealer


alphabet = "abcdefghijklmnopqrstuvwxzy"

class KeyboardProblem(Annealer):
    """Test annealer with keyboard problem."""
    def __init__(self, state):
        self.state = generate_random_layout()
        super(KeyboardProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two keys in the route."""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]
    def energy(self):
        """Calculates the length of the route."""
        e = cost(self.state)
        return e



def generate_random_layout():
    layout = []
    while len(layout) < 26:
        r_int = random.randint(0,26)
        letter = alphabet[r_int]
        if letter not in layout:
            layout.append(letter)
    return layout

#keying times
#frequency pairs

def key_pair_cost(key_a, idx_a, key_b, idx_b):
    frequency = freq_map(key_a, key_b)
    keying_time = key_map(idx_a, idx_b)
    return frequency * keying_time

def cost(layout):
    total_cost = 0;
    for idx_a, key_a in enumerate(layout):
        for idx_b, key_b in enumerate(layout):
            total_cost += key_pair_cost(key_a, idx_a, key_b, idx_b)
    return total_cost

def main():
    layout = generate_random_layout()
    initial_cost = cost(layout)
    # T = .9
    # instable = False
    # while (T > minimum_temperature):
    #     while instable
    #         qwert


main()