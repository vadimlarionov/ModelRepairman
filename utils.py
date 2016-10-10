# -*- coding: utf-8 -*-


class Utils:

    @staticmethod
    def to_str(object):
        if isinstance(object, str):
            return object
        return '%.10f' % object
