from rtamt.ast.nodes.unary_node import UnaryNode


class Rise(UnaryNode):
    """A class for storing STL Neg nodes
        Inherits Node
    """
    def __init__(self, child):
        """Constructor for Neg node

            Parameters:
                child : stl.Node
        """
        name_phrase = 'rise'
        super(Rise, self).__init__(name_phrase, child)
