import unittest
from histogram import Histogram


class HistogramTests(unittest.TestCase):

    def setUp(self):
        self.h = Histogram()

        self.h.add("Apache")
        self.h.add("Apache")
        self.h.add("nginx")
        self.h.add("IIS")
        self.h.add("nginx")

    def test_init(self):
        self.assertTrue(isinstance(self.h, Histogram))

    def test_add(self):
        self.h.add("Apache")
        self.assertEqual(self.h.get_dict(), {"Apache": 3, "nginx": 2, "IIS": 1})

    def test_count(self):
        self.assertTrue(self.h.count("Apache"), 2)

    def test_get_dict(self):
        self.assertEqual(self.h.get_dict(), {"Apache": 2, "nginx": 2, "IIS": 1})

if __name__ == '__main__':
    unittest.main()
