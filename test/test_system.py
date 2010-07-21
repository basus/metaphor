import unittest
from metaphor.core import system
from metaphor.core import parser

class TestBuilder(unittest.TestCase):
    """ Tests the Metaphor Builder """

    def setUp(self):
        self.parser = parser.parser
        self.builder = system.Builder()

    def test_all(self):
        fl = open("examples/parametric.lsys")
        st = ""
        for line in fl:
            st += line
        parser.lex.input(st)
        root = parser.parser.parse(st)
        self.builder = system.Builder(root)
        self.builder.build_system()

    def test_init(self):
        node = parser.Node("system", data="lsys")
        bl = system.Builder(node)
        assert bl.root == node
        assert bl.root.type == "system"
        assert bl.root.data == "lsys"

    def test_build_axiom(self):
        # Mock the nodes and send to the builder
        node = parser.Node("axiom", children=[])
        node.children.append(["F"])
        ax = self.builder.build_axiom(node)
        # Test the result of the build
        assert len(ax) == 1
        ax = ax[0]
        assert ax.symbol == "F"
        assert ax.params == []


class TestSystem(unittest.TestCase):
    """ Test the Metaphor LSystem class and API """

class TestEnvironment(unittest.TestCase):
    """ Tests the Metaphor Environment and API """
