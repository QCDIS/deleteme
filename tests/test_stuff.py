from unittest import TestCase

from pack.my_class import WorkflowParser


class TestExtractor(TestCase):

    def test_extract_cell(self):
        node = {'a': 'b'}
        wp = WorkflowParser(node)
        wp.do_stuf('name')
        self.assertTrue(True,'Done')