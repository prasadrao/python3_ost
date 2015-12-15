# import the logging module
import logging
#set p the logger
#logging.basicConfig(filename='forestry.log', level = logging.DEBUG)
logging.basicConfig(filename='forestry.log', level = logging.ERROR)
#log a message
logging.info('Starting up the forestry program')

class Tree(object):
    "Represent a tree in a forest that can be converted into boards."
    sizes = dict(S=1, M=2, L=3, XL=4, XXL=5)

    def __init__(self, size="L"):
        "Initialize: insist that size is a valid code."
        if size not in self.sizes:
            message = "Tree size must be one of: %s" % ",".join(self.sizes.keys())
            logging.error(message)
            raise ValueError(message)
        self.size = size
        logging.info('Instantiated a tree')

    def get_boards(self):
        "Return number of boards equivalent."
        logging.info('tree.get_boards method called')
        return self.sizes[self.size]

    def __str__(self):
        "Render as a string"
        return "Tree: Size %s" % self.size

class Lumberjack(object):
    "Represent a lumberjack who can cut down tree."
    def __init__(self):
        "Initialize: start with no tree."
        self.tree = None
        logging.info('Instantiated a Lumberjack')

    def cut_down_tree(self):
        "Convert tree to boards and go back to not having a tree."
        if not self.tree:
            #raise TypeError("Cannot cut_down_tree(): Lumberjack has no tree!")
            msg = "Cannot cut_down_tree(): Lumberjack has no tree!"
            logging.error(msg)
            raise TypeError(msg)
        boards = self.tree.get_boards()
        self.tree = None
        logging.info('Lumberjack.tree cut down')
        return boards

if __name__ == "__main__":
    "Demonstrate basic usage."
    john = Lumberjack()
    john.tree = Tree("XXL")
    if john.cut_down_tree() != 5:
        print("Error: XXL tree should yield 5 boards")
