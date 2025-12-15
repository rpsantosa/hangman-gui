import unittest
from src.game.engine import GameEngine

class TestGameEngine(unittest.TestCase):

    def setUp(self):
        self.engine = GameEngine()

    def test_initial_state(self):
        self.assertEqual(self.engine.word, None)
        self.assertEqual(self.engine.guesses, [])
        self.assertEqual(self.engine.max_attempts, 6)
        self.assertEqual(self.engine.current_attempts, 0)

    def test_set_word(self):
        self.engine.set_word("TEST")
        self.assertEqual(self.engine.word, "TEST")

    def test_guess_correct_letter(self):
        self.engine.set_word("TEST")
        self.engine.guess("T")
        self.assertIn("T", self.engine.guesses)
        self.assertEqual(self.engine.current_attempts, 0)

    def test_guess_incorrect_letter(self):
        self.engine.set_word("TEST")
        self.engine.guess("A")
        self.assertIn("A", self.engine.guesses)
        self.assertEqual(self.engine.current_attempts, 1)

    def test_check_win_condition(self):
        self.engine.set_word("TEST")
        self.engine.guess("T")
        self.engine.guess("E")
        self.engine.guess("S")
        self.engine.guess("T")
        self.assertTrue(self.engine.check_win())

    def test_check_loss_condition(self):
        self.engine.set_word("TEST")
        self.engine.guess("A")
        self.engine.guess("B")
        self.engine.guess("C")
        self.engine.guess("D")
        self.engine.guess("E")
        self.engine.guess("F")
        self.assertTrue(self.engine.check_loss())

if __name__ == '__main__':
    unittest.main()