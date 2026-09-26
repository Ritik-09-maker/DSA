class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)

        for i in factors[::-1]:
            if i * i != n:
                factors.append(n // i)

        factors.sort()

        if k <= len(factors):
            return factors[k - 1]

        return -1