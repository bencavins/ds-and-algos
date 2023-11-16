import random

class Door:
    def __init__(self, prize):
        self.prize = prize

def gen_doors():
    doors = [Door('goat'), Door('goat'), Door('$$$')]
    random.shuffle(doors)
    return doors

def do_one_sim(switch=False):
    doors = gen_doors()
    pick = doors[0]
    if doors[1].prize == 'goat':
        other = doors[2]
    else:
        other = doors[1]
    
    if switch:
        pick = other
    
    return pick.prize == '$$$'

def run_sim(N=100000):
    print(f'Testing {N} stays...')
    wins = 0
    for _ in range(N):
        if do_one_sim():
            wins += 1
    print(f'Win %: {wins/N}')
    print(f'Lose %: {(N-wins)/N}')

    print()

    print(f'Testing {N} switches...')
    wins = 0
    N = 10000
    for _ in range(N):
        if do_one_sim(switch=True):
            wins += 1
    print(f'Win %: {wins/N}')
    print(f'Lose %: {(N-wins)/N}')

if __name__ == '__main__':
    run_sim()