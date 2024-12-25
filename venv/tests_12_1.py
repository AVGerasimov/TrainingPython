import unitscheck
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        x = unitscheck.Runner('Vasya')
        for i in range(1, 11):
            x.walk()
        self.assertEqual(x.distance, 50)

    def test_run(self):
        x = unitscheck.Runner('Alex')
        for i in range(1, 11):
            x.run()
        self.assertEqual(x.distance, 100)

    def test_challenge (self):
        x = unitscheck.Runner('Sam')
        y = unitscheck.Runner('Nik')
        for i in range(1, 11):
            x.run()
            y.walk()
        self.assertNotEqual(x.distance, y.distance)

