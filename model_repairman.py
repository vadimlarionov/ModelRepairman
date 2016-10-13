# -*- coding: utf-8 -*-

from math import factorial, pow


class ModelRepairman:
    def __init__(self, n, tno, to, c, zi, z):
        """
        :param n: Количество компьютеров
        :param tno: Среднее время наработки на отказ одного компьютера
        :param to: Среднее время ремонта одного компьютера
        :param zi: Заработная плата специалиста за 1 час
        :param z: Финансовые потери организации от неисправного компьютера за 1 час
        """
        self.n = n
        self.tno = tno
        self.to = to
        self.c = c
        self.zi = zi
        self.z = z

        self.__psi_value = None
        self.__p0 = None
        self.__q = None
        self.__l = None
        self.__u = None

    def psi(self):
        if self.__psi_value is None:
            self.__psi_value = self.to / self.tno
        return self.__psi_value

    # P0
    def probability_initial_state(self):
        if self.__p0 is not None:
            return self.__p0

        p0 = 0
        psi = self.psi()
        c = self.c
        n_factorial = factorial(self.n)
        for k in range(c + 1):
            p0 += (n_factorial * pow(psi, k)) / (factorial(k) * factorial(self.n - k))

        for k in range(c + 1, self.n + 1):
            p0 += (n_factorial * pow(psi, k)) / (pow(c, k - c) * factorial(c) * factorial(self.n - k))

        self.__p0 = pow(p0, -1)
        return self.__p0

    # Pk
    def probability_kth_state(self, k):
        c = self.c
        return factorial(self.n) * pow(self.psi(), k) * self.probability_initial_state() / \
               (pow(c, k - c) * factorial(c) * factorial(self.n - k))

    # Q
    def queue_length(self):
        if self.__q is not None:
            return self.__q
        q = 0
        for k in range(self.c, self.n + 1):
            q += (k - self.c) * self.probability_kth_state(k)
        self.__q = q
        return self.__q

    # L
    def broken_length(self):
        if self.__l is not None:
            return self.__l
        l = 0
        for k in range(1, self.n + 1):
            l += k * self.probability_kth_state(k)
        self.__l = l
        return self.__l

    # U
    def computers_repair(self):
        if self.__u is not None:
            return self.__u
        self.__u = self.broken_length() - self.queue_length()
        return self.__u

    # ρ0 - коэффициент загрузки одного специалиста ремонтом компьютеров
    def load_factor_specialist(self):
        return self.computers_repair() / self.c

    # n - среднее количество неисправных компьютеров
    def average_broken_computers(self):
        return self.n - self.broken_length()

    # Tр - время пребывания компьютера в неисправном состоянии (в очереди на ремонт и ремонте)
    def broken_computer_time(self):
        l = self.broken_length()
        return l * self.tno / (self.n - l)

    # W - среднее время нахождения компьютера в очереди на ремонт
    def broken_computer_in_queue_time(self):
        return self.broken_computer_time() - self.to

    # ρe - коэффициент загрузки компьютера
    def load_factor_computer(self):
        return self.average_broken_computers() / self.n

    # Tц - среднее время цикла для компьютера
    def computer_cycle_time(self):
        return self.broken_computer_time() + self.tno

    # ρe / ρo
    def ratio(self):
        return self.load_factor_computer() / self.load_factor_specialist()

    # Yi
    def calculate_y(self):
        y = self.c * self.zi + self.broken_length() * self.z
        return '%.2f' % y
