# Unit testing and integration testing, two fields where this is most used

import unittest


def sum(num_1, num_2):
    return num_1 + num_2


class BlackBoxTest(unittest.TestCase):

    def test_add_two_positive(self):
        num_1 = 10
        num_2 = 5

        result = sum(num_1, num_2)

        self.assertEqual(result, 15)

    def test_add_two_negative(self):
        num_1 = -10
        num_2 = -5

        result = sum(num_1, num_2)

        self.assertEqual(result, -15)


if __name__ == '__main__':
    unittest.main()

# if there are errors in the functions the console is printing the errors