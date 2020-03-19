from rtamt.operation.abstract_operation import AbstractOperation
from rtamt.operation.stl_ct.since_operation import SinceOperation
from rtamt.operation.stl_ct.once_bounded_operation import OnceBoundedOperation
from rtamt.operation.stl_ct.historically_bounded_operation import HistoricallyBoundedOperation
from rtamt.operation.stl_ct.and_operation import AndOperation

class SinceBoundedOperation(AbstractOperation):
    def __init__(self, begin, end):
        self.left = []
        self.right = []
        self.begin = begin
        self.end = end

    def update(self, *args, **kargs):
        out = []
        left_list = args[0]
        right_list = args[1]
        self.left = self.left + left_list
        self.right = self.right + right_list

        since = SinceOperation()
        hist = HistoricallyBoundedOperation(0, self.begin)
        once = OnceBoundedOperation(self.begin, self.end)
        andop = AndOperation()

        out1 = once.update(right_list)
        out2 = since.update(left_list, right_list)
        out3 = hist.update(out2)
        out = andop.update(out1, out3)

        return out

    def offline(self, *args, **kargs):
        out = []
        left_list = args[0]
        right_list = args[1]
        self.left = self.left + left_list
        self.right = self.right + right_list

        since = SinceOperation()
        hist = HistoricallyBoundedOperation(0, self.begin)
        once = OnceBoundedOperation(self.begin, self.end)
        andop = AndOperation()

        out1 = once.offline(right_list)
        out2 = since.offline(left_list, right_list)
        out3 = hist.offline(out2)
        out = andop.offline(out1, out3)

        return out
