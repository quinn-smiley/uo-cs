"""Monty Hall Problem
Quinn Smiley, 2026-05-05, CS 211"""

import random


def simulate(n_doors, trials, do_switch): # Asked Cursor for the best way to structure this function
    """
    Simulate the Monty Hall problem with n_doors (n_doors >= 3).

    Returns the number of wins out of `trials` trials.
    - do_switch = False  -> contestant stays with first pick
    - do_switch = True   -> contestant switches to the other unopened door
    """
    if n_doors < 3:
        raise ValueError("n_doors must be >= 3")
    if trials < 1:
        raise ValueError("trials must be >= 1")

    wins = 0

    for _ in range(trials):
        prize_door = random.randrange(n_doors)

        first_pick = random.randrange(n_doors)

        host_doors = []
        for d in range(n_doors):
            if d != first_pick and d != prize_door:
                host_doors.append(d)

        opened_by_host = set(random.sample(host_doors, n_doors - 2))

        closed_doors = []
        for d in range(n_doors):
            if d not in opened_by_host:
                closed_doors.append(d)

        if do_switch:
            if closed_doors[0] == first_pick:
                final_pick = closed_doors[1]
            else:
                final_pick = closed_doors[0]
        else:
            final_pick = first_pick

        if final_pick == prize_door:
            wins += 1

    return wins


def main(): # Asked Cursor the most effective way to test 
    def show_results(n_doors, trials):
        stay_wins = simulate(n_doors, trials, False)
        switch_wins = simulate(n_doors, trials, True)

        stay_rate = stay_wins / trials
        switch_rate = switch_wins / trials

        print("n =", n_doors, "trials =", trials)
        print(
            "  stay:   wins =",
            stay_wins,
            "rate =",
            round(stay_rate, 4),
            "expected ~",
            round(1 / n_doors, 4),
        )
        print(
            "  switch: wins =",
            switch_wins,
            "rate =",
            round(switch_rate, 4),
            "expected ~",
            round((n_doors - 1) / n_doors, 4),
        )
        print()

    n_text = input("Enter number of doors n (>=3): ").strip()
    n_doors = int(n_text)

    trials_text = input("Enter number of trials (e.g., 50000): ").strip()
    trials = int(trials_text)

    show_results(n_doors, trials)


if __name__ == "__main__":
    main()
