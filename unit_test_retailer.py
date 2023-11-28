import unittest

from retailer import Retailer

class MyTestCase(unittest.TestCase):
    def test_str(self):
        """
        To test if the __str__ is working as expected
        :return:
        """
        this_retailer = Retailer()
        this_retailer.set_retailer_id()
        this_retailer.set_retailer_name()

        expected_str = f'{this_retailer.get_retailer_id()}, {this_retailer.get_retailer_name()}'
        print(this_retailer)

        self.assertEquals(str(this_retailer), expected_str, f'__str__ not working')

    def test_generate_retailer_id(self):
        """
        To test if the randomly generated retailer id is valid:
        - 8 digit
        - all numbers
        :return:
        """
        this_retailer = Retailer()
        this_result = this_retailer.generate_retailer_id()
        print(this_result)

        self.assertEquals(len(this_result), 8 , f'failed to generate 8 digits: {this_result}')
        self.assertTrue(this_result.isdigit(), f'failed to generate all digits: {this_result}')

    def test_set_retailer_id(self):
        """
        Expect the function set_retailer_id to
        1. set the retailer_id when the input_id is not null
        2. generate a random retailer_id when the input_id is null
        3. handle the exception when the input_id is not legit
        3. handle the exception when the input_id is in duplications
        4. class variable retailer_id got updated correctly
        :return:
        """

        # initialise car:
        this_retailer = Retailer()
        this_retailer_2 = Retailer()
        this_retailer_3 = Retailer()
        this_retailer_4 = Retailer()
        this_retailer_5 = Retailer()

        # case 1
        this_retailer.set_retailer_id('12345678')
        self.assertEqual(this_retailer.get_retailer_id(),'12345678','failed to set up retailer id')

        # case 2
        this_retailer_2.set_retailer_id()
        print(this_retailer_2.get_retailer_id())
        self.assertNotEquals(this_retailer_2.get_retailer_id(), None, 'failed to set up randomly generated retailer id')

        # case 3
        this_retailer_3.set_retailer_id('BE1234')
        print(this_retailer_3.get_retailer_id())
        self.assertEquals(this_retailer_3.get_retailer_id(), None, 'invalid retailer id got setup')

        # case 3b
        this_retailer_4.set_retailer_id('12B45678')
        print(this_retailer_4.get_retailer_id())
        self.assertEquals(this_retailer_4.get_retailer_id(), None, 'invalid retailer id got setup')

        # case 4
        this_retailer_5.set_retailer_id('12345678')
        print(this_retailer_5.get_retailer_id())
        self.assertEquals(this_retailer_5.get_retailer_id(), None, 'duplicated retailer id got setup')

    def test_set_retailer_name(self):
        """
        To test if the set_retailer_name work as expected:
        1. set the retailer name when the input is a valid name: only consists of character and whitespace
        2. do not set the retailer name and print error message when the input is not a valid name
        3. generate a retailer name when no input is given
        :return:
        """
        # Case 1
        this_retailer = Retailer()
        this_retailer.set_retailer_name('Eydbe i')
        self.assertEquals(this_retailer.get_retailer_name(),'Eydbe i', 'failed to setup valid retailer name' )

        # Case 2
        this_retailer_2 = Retailer()
        this_retailer_2.set_retailer_name('E1dbei')
        self.assertEquals(this_retailer_2.get_retailer_name(),None, 'wrongly setup invalid retailer name' )

        # Case 3
        this_retailer_3 = Retailer()
        this_retailer_3.set_retailer_name()
        print(this_retailer_3.get_retailer_name())
        self.assertNotEquals(this_retailer_3.get_retailer_name(),None, 'failed to setup randomly generated retailer name' )

if __name__ == '__main__':
    unittest.main()
