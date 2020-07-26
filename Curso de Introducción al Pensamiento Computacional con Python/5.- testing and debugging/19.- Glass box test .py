# it is based on the flow of the program, it tries all the different paths

# Regression testing o mocks, field where it is most used

import unittest


def It_is_old(age):
   if age >= 40:
        return True
   else:
        return False


class GlassBoxTest(unittest.TestCase):
    
    def test_it_is_old(self):
        age = 60

        result = It_is_old(age)
        self.assertEqual(result, True)

    def test_it_is_not_old(self):
        age = 20

        result = It_is_old(age)
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity throws more details information about the errors
