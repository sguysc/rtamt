from rtamt.ast.nodes.unary_node import UnaryNode


class Always(UnaryNode):
    """A class for storing STL Always nodes
        Inherits TemporalNode
    """

    def __init__(self, child):
        """Constructor for Always

        Parameters:
            child : stl.Node
            bound : Interval
        """
        name_phrase = 'always'
        super(Always, self).__init__(name_phrase, child)







