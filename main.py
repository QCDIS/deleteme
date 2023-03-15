# This is a sample Python script.
from pack.my_class import WorkflowParser

def print_hi(name):
    node = {'a':'b'}
    wp = WorkflowParser(node)
    wp.do_stuf(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
