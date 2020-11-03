class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        tests = ["string", 1.5]
        for t in tests:
            with self.subTest(i=t):
                self.assertRaises(TypeError, factorize, x=t)

    def test_negative(self):
        tests = [-1, -10, -100]
        for t in tests:
            with self.subTest(i=t):
                self.assertRaises(ValueError, factorize, x=t)

    def test_zero_and_one_cases(self):
        tests = {
            0: (0,),
            1: (1,),
        }
        for key, value in tests.items():
            with self.subTest(i=key):
                self.assertEqual(factorize(x=key), value)

    def test_simple_numbers(self):
        tests = {
            3: (3,),
            13: (13,),
            29: (29,),
        }
        for key, value in tests.items():
            with self.subTest(i=key):
                self.assertEqual(factorize(x=key), value)

    def test_two_simple_multipliers(self):
        tests = {
            6: (2, 3),
            26: (2, 13),
            121: (11, 11),
        }
        for key, value in tests.items():
            with self.subTest(i=key):
                self.assertEqual(factorize(x=key), value)

    def test_many_multipliers(self):
        tests = {
            1001: (7, 11, 13),
            9699690: (2, 3, 5, 7, 11, 13, 17, 19),
        }
        for key, value in tests.items():
            with self.subTest(i=key):
                self.assertEqual(factorize(x=key), value)                
