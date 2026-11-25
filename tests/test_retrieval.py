import unittest
from assistant_core.documents import chunks
from assistant_core.retrieval import DocumentIndex

class RetrievalTests(unittest.TestCase):
    def test_page_preserved(self):
        self.assertEqual(chunks([(3, "hello world")])[0][0], 3)
    def test_relevant_passage(self):
        index = DocumentIndex([(1, "invoice payment due"), (2, "holiday schedule")])
        self.assertEqual(index.search("invoice")[0][0], 1)
    def test_unknown_query(self):
        self.assertEqual(DocumentIndex([(1, "invoice")]).search("zebra"), [])
