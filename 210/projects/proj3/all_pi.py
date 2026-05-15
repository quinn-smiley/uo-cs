import math
import random

import arch
import wallis
import mc

def all_pi(err_tol: float) -> list[int]:
    # Arch
    num_sides = 1
    while abs(arch.pi_arch(num_sides) - math.pi) > err_tol:
        num_sides += 1
    diff_arch = abs(arch.pi_arch(num_sides) - math.pi)
    print("Archimedes: num_sides =", num_sides, " (Differs by", diff_arch, ")")

    # Wallis
    num_pairs = 1
    while abs(wallis.pi_wallis(num_pairs) - math.pi) > err_tol:
        num_pairs += 1
    diff_wallis = abs(wallis.pi_wallis(num_pairs) - math.pi)
    print("Wallis: num_pairs =", num_pairs, "(Differs by", diff_wallis, ")")

    # MC
    num_darts = 1
    while abs(mc.pi_mc(num_darts) - math.pi) > err_tol:
        num_darts += 1
    diff_mc = abs(mc.pi_mc(num_darts) - math.pi)

    print("Monte Carlo: num_darts =", num_darts, "(Differs by", diff_mc, ")")

    print([num_sides, num_pairs, num_darts])

all_pi(0.1)
