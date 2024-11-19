import unittest
from FizzBuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_generate_upto_1(self):
        self.assertEqual(FizzBuzz.generate(1), ["1"])

    def test_generate_upto_15(self):
        self.assertEqual(FizzBuzz.generate(15), [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ])

    def test_multiple_of_3(self):
        output = FizzBuzz.generate(10)
        self.assertEqual(output[2], "Fizz")
        self.assertEqual(output[5], "Fizz")
        self.assertEqual(output[8], "Fizz")

    def test_multiple_of_5(self):
        output = FizzBuzz.generate(10)
        self.assertEqual(output[4], "Buzz")
        self.assertEqual(output[9], "Buzz")

    def test_multiple_of_3_and_5(self):
        output = FizzBuzz.generate(15)
        self.assertEqual(output[14], "FizzBuzz")

    def test_no_fizzbuzz_for_non_multiples(self):
        output = FizzBuzz.generate(7)
        self.assertEqual(output[0], "1")
        self.assertEqual(output[1], "2")
        self.assertEqual(output[3], "4")
        self.assertEqual(output[6], "7")

    def test_empty_range(self):
        with self.assertRaises(ValueError):
            FizzBuzz.generate(0)
        with self.assertRaises(ValueError):
            FizzBuzz.generate(-5)

    def test_edge_case_of_3_and_5(self):
        output = FizzBuzz.generate(5)
        self.assertEqual(output[2], "Fizz")  # 3 is "Fizz"
        self.assertEqual(output[4], "Buzz")  # 5 is "Buzz"

    def test_type_error(self):
        with self.assertRaises(TypeError):
            FizzBuzz.generate("10")
        with self.assertRaises(TypeError):
            FizzBuzz.generate(10.5)

if __name__ == "__main__":
    unittest.main()
