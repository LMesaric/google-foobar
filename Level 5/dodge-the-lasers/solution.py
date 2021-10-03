from decimal import Decimal, getcontext, ROUND_DOWN


def solution(str_n):
    getcontext().prec = 200
    sqrt_2_minus_1 = Decimal('2').sqrt() - 1

    def solution_rec(n):
        if n == 0:
            return 0
        next_n = (sqrt_2_minus_1 * n).to_integral_exact(rounding=ROUND_DOWN)  # floor
        return n * next_n + n * (n + 1) / 2 - next_n * (next_n + 1) / 2 - solution_rec(next_n)

    return str(solution_rec(Decimal(str_n)))


from time import time

t = time()
print(solution("77"))
print(solution("5"))
print(solution("1" + "0" * 100))
print(time() - t)
