# -*- coding: utf-8 -*-


class Utils:

    @staticmethod
    def to_str(obj):
        if isinstance(obj, str):
            return obj
        return '%.5f' % obj

    @staticmethod
    def to_int_list(line):
        return [int(x) for x in line.split(',')]
