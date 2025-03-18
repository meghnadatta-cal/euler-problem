from mpmath import mp, mpf, sqrt, log10, floor
import math
 
# Set decimal precision high enough (200 decimal places should be safe)
mp.dps = 200
 
# Precompute high‐precision square roots for 1..2011
MAX_VAL = 2011
sqrt_vals = [None] * (MAX_VAL+1)
for i in range(1, MAX_VAL+1):
    sqrt_vals[i] = sqrt(mpf(i))
 
def N_pq(p, q):
    """
    For given integers p and q (with p < q and √q–√p < 1),
    return the minimal integer n such that (√q–√p)^(2n) < 10^(–2011).
    This is computed as:
         n = floor(2011/( -2*log10(√q–√p) )) + 1.
    """
    delta = sqrt_vals[q] - sqrt_vals[p]  # positive, < 1
    # Compute -log10(delta)
    L = -log10(delta)
    # Compute quotient = 2011/(2*L)
    # (Because we require 2n > 2011/(L) so n > 2011/(2L).)
    quotient = mpf(2011) / (2 * L)
    n_val = int(floor(quotient)) + 1
    return n_val
 
def main():
    total_sum = 0
    count_pairs = 0
    # Loop over p from 1 to MAX_VAL.
    for p in range(1, MAX_VAL+1):
        sp = sqrt_vals[p]
        # For the property (√q – √p) < 1, we need q < (√p+1)².
        T = (sp + 1)**2
        # Determine the maximum q allowed by the (√p+1)² condition.
        # If p is a perfect square, T is an integer and we require q <= T-1.
        if int(sqrt(mpf(p)))**2 == p:
            q_bound = int(T) - 1
        else:
            q_bound = int(floor(T))
        # Also, we have the condition p+q ≤ MAX_VAL.
        q_bound = min(q_bound, MAX_VAL - p)
        # q runs from p+1 to q_bound (inclusive), if any.
        for q in range(p+1, q_bound+1):
            # Only consider pairs where (√q–√p) < 1 holds (it should by our q_bound)
            if (sqrt_vals[q] - sp) >= 1:
                continue
            n_val = N_pq(p, q)
            total_sum += n_val
            count_pairs += 1
    print("Sum of all N(p,q) =", total_sum)
    print("Total valid pairs =", count_pairs)
 
if __name__ == '__main__':
    main()