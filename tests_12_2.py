import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        self.all_results.update(tournament.start())
        self.assertTrue(max(self.all_results, key=int) == 2)

    def test_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        self.all_results.update(tournament.start())
        self.assertTrue(max(self.all_results, key=int) == 2)

    def test_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        self.all_results.update(tournament.start())
        self.assertTrue(max(self.all_results, key=int) == 3)

    def test_usain_and_nik_speed(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.assertTrue("Усэйн" in results.values())

    def test_andrey_and_nik_speed(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue("Андрей" in results.values())

    def test_usain_andrey_and_nik_speed(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.assertTrue("Усэйн" in results.values())
        self.assertTrue("Андрей" in results.values())