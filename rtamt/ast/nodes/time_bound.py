class TimeBound(object):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def strTimeBound(self):
        return '[' + str(self.begin) + ',' + str(self.end) + ']'

    @property
    def begin(self):
        return self.__begin

    @begin.setter
    def begin(self, begin):
        self.__begin = begin

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end
