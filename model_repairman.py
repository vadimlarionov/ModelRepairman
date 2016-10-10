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
        return self.to / self.tno

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

    # ρ0 - коэффициент загрузки одного специалиста ремонтом компьютеров
    def load_factor_specialist(self, c):
        return self.computers_repair(c) / c

    # n - среднее количество неисправных компьютеров
    def average_broken_computers(self, c):
        return self.n - self.broken_length(c)

    # Tр - время пребывания компьютера в неисправном состоянии (в очереди на ремонт и ремонте)
    def broken_computer_time(self, c):
        l = self.broken_length(c)
        return l * self.tno / (self.n - l)

    # W - cреднее время нахождения компьютера в очереди на ремонт
    def broken_computer_in_queue_time(self, c):
        return self.broken_computer_time(c) - self.to

    # ρe - коэффициент загрузки компьютера
    def load_factor_computer(self, c):
        return self.average_broken_computers(c) / self.n

    # Tц - среднее время цикла для компьютера
    def computer_cycle_time(self, c):
        return self.broken_computer_time(c) + self.tno

    # ρe / ρo
    def ratio(self, c):
        return self.load_factor_computer(c) / self.load_factor_specialist(c)
