# -*- coding: utf-8 -*-

from math import factorial, pow


class ModelRepairman:

    def __init__(self, n, tno, to):
        """
        :param n: Количество компьютеров
        :param tno: Среднее время наработки на отказ одного компьютера
        :param to: Среднее время ремонта одного компьютера
        """
        self.n = n
        self.tno = tno
        self.to = to

    def psi(self):
        return (1 / self.tno) / (1 / self.to)

    # P0
    def probability_initial_state(self, c):
        p0 = 0
        psi = self.psi()
        n_factorial = factorial(self.n)
        for k in range(c+1):
            p0 += (n_factorial * pow(psi, k)) / (factorial(k) * factorial(self.n - k))

        for k in range(c+1, self.n+1):
            p0 += (n_factorial * pow(psi, k)) / (pow(c, k - c) * factorial(c) * factorial(self.n - k))

        return pow(p0, -1)

    # Pk
    def probability_kth_state(self, c, k):
        return factorial(self.n) * pow(self.psi(), k) * self.probability_initial_state(c) / \
               (pow(c, k - c) * factorial(c) * factorial(self.n - k))

    # Q
    def queue_length(self, c):
        q = 0
        for k in range(c, self.n+1):
            q += (k - c) * self.probability_kth_state(c, k)
        return q

    # L
    def broken_length(self, c):
        l = 0
        for k in range(1, self.n+1):
            l += k * self.probability_kth_state(c, k)
        return l

    # U
    def computers_repair(self, c):
        return self.broken_length(c) - self.queue_length(c)















