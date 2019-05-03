import random
from simanneal import Annealer
import frequency_generator as f
import keyboardArray as k
import time



freq_map = f.make_freq()
alphabet = "abcdefghijklmnopqrstuvwxzy"
key_distances = k.key_distances(1);

class KeyboardProblem(Annealer):
    """Test annealer with keyboard problem."""
    def __init__(self, state):
        #print("state")
        self.state = state
        super(KeyboardProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two keys in the route."""
        #print("move")
        a = random.randint(0, len(self.state)-1)
        b = random.randint(0, len(self.state)-1)
        self.state[a], self.state[b] = self.state[b], self.state[a]
    def energy(self):
        #print("energy")
        """Calculates the length of the route."""
        e = cost(self.state)
        return e



def generate_random_layout():
    layout = []
    while len(layout) < 26:
        r_int = random.randint(0,25)
        letter = alphabet[r_int]
        if letter not in layout:
            layout.append(letter)
    return layout

#keying times
#frequency pairs

def key_pair_cost(key_a, idx_a, key_b, idx_b):
    frequency = freq_map[1][str(key_a)+key_b]    #freq_map(key_a, key_b)
    keying_time = key_distances[idx_a][idx_b]
    return frequency * keying_time

def cost(layout):
    total_cost = 0;
    for idx_a, key_a in enumerate(layout):
        for idx_b, key_b in enumerate(layout):
            total_cost += key_pair_cost(key_a, idx_a, key_b, idx_b)
    return total_cost


def display_keyboard(layout):
    #10
    #9
    #7
    print(layout[0:10])
    print(layout[10:19])
    print(layout[19:26])

def main():
    init_state = generate_random_layout()

    t_end = time.time() + 60 * 20
    min_e = -1
    min_state = 0
    e_2 = -1
    e_3 = -1
    s_2 = 0
    s_3 = 0
    while time.time() < t_end:
        tsp = KeyboardProblem(init_state)
        tsp.steps = 100000
        # since our state is just a list, slice is the fastest way to copy
        tsp.copy_strategy = "slice"
        state, e = tsp.anneal()
        if (min_e == -1 or e < min_e):
            s_3 = s_2
            s_2 = min_state
            min_state = state
            e_3 = e_2
            e_2 = min_e
            min_e = e

    print("best")
    print(display_keyboard(min_state))
    print(min_e)
    print("second")
    print(display_keyboard(s_2))
    print(e_2)
    print("third")
    print(display_keyboard(s_3))
    print(e_3)
    return state
main()
