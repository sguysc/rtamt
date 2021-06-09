import sys

from rtamt.ast.nodes.binary_node import BinaryNode


class Disjunction(BinaryNode):
    """A class for storing STL Or nodes
        Inherits TemporalNode
    """
    def __init__(self, child1, child2):
        """Constructor for Or node

        Parameters:
            child1 : stl.Node
            child2 : stl.Node
        """
        name_phrase = 'or'
        super(Disjunction, self).__init__(name_phrase, child1, child2)
