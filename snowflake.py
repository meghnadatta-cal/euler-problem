import math
 
n = int(1e7)

ans = 0
 
for t in range(1, n - 2):

    v = 7 * t + 17

    A = math.gcd(v, (2 * pow(4, t, v) - pow(3, t, v)) % v + v)

    B = math.gcd(v, ((3 * t - 17) * pow(4, t, v) + (2 * t + 17) * pow(3, t, v)) % v + v)

    ans += math.gcd(A, B) * 6
 
print(f"ans = {ans}")

 