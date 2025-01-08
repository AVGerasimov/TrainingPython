import unitchekX
import unittest



class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        all_results = {} # словарь



    def setUp(self):
        #=== создание трех бегунов
        self.p1 = unitchekX.Runner('Усэйн', 10)
        self.p2 = unitchekX.Runner('Андрей', 9)
        self.p3 = unitchekX.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
   #     for key, value in self.all_results.items():
   #         print(f"{key}: {value}")
        """Tear down for class"""
        print("==========")
        print("tearDownClass")


    def test_run1(self):
        x = unitchekX.Tournament(90, self.p1, self.p3)
        self.all_results = x.start()
        val = self.all_results.get(1)
        self.assertTrue(val == 'Усэйн')
        for key, value in self.all_results.items():
            print(f"{key}: {value}", end=' ')
        print()

    def test_run2(self):
        x = unitchekX.Tournament(90, self.p2, self.p3)
        self.all_results = x.start()
        val = self.all_results.get(1)
        self.assertTrue(val == 'Андрей')
        for key, value in self.all_results.items():
            print(f"{key}: {value}", end=' ')
        print()

    def test_run3(self):
        x = unitchekX.Tournament(90, self.p1, self.p2, self.p3)
        self.all_results = x.start()
        val = self.all_results.get(1)
        self.assertTrue(val == 'Усэйн')
        for key, value in self.all_results.items():
            print(f"{key}: {value}", end=' ')
        print()






