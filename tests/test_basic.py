
import unittest

class TestBasic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_basic(self):
        print("")
        import ggpython
        print("____ ____ ____ ____ ____ ____ ____ ____")
        print("TEST:","test_basic")
        valo = ggpython.ValorantTrackerWebsiteAPI()
        print("____ ____ ____ ____ ____ ____ ____ ____")
if __name__ == "__main__":
    pass
