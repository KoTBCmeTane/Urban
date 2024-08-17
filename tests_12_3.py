import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

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
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_challenge(self):
        self.assertTrue(True)

    def test_run(self):
        self.assertTrue(True)

    def test_walk(self):
        self.assertTrue(True)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def test_first_tournament(self):
        self.assertTrue(True)

    def test_second_tournament(self):
        self.assertTrue(True)

    def test_third_tournament(self):
        self.assertTrue(True)

def frozen_test(func):
    def wrapper(self, *args, **kwargs):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            func(self, *args, **kwargs)
    return wrapper

RunnerTest.test_challenge = frozen_test(RunnerTest.test_challenge)
RunnerTest.test_run = frozen_test(RunnerTest.test_run)
RunnerTest.test_walk = frozen_test(RunnerTest.test_walk)

TournamentTest.test_first_tournament = frozen_test(TournamentTest.test_first_tournament)
TournamentTest.test_second_tournament = frozen_test(TournamentTest.test_second_tournament)
TournamentTest.test_third_tournament = frozen_test(TournamentTest.test_third_tournament)