# -*- coding: utf-8 -*-


class Utils:

    @staticmethod
    def to_str(obj):
        if isinstance(obj, str):
            return obj
        return '%.5f' % obj
