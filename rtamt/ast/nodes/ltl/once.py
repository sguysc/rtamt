import sys

from rtamt.ast.nodes.unary_node import UnaryNode


class Once(UnaryNode):
    """A class for storing STL Once nodes
                Inherits TemporalNode
    """
    def __init__(self, child):
        """Constructor for Once node

        Parameters:
            child : stl.Node
            bound : Interval
        """
        name_phrase = 'once'
        super(Once, self).__init__(name_phrase, child)
