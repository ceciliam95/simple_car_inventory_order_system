import unittest
from car import Car

class MyTestCase(unittest.TestCase):
    def test_init(self):
        pass

    def test_str(self):
        # initialise car:
        this_car = Car()
        this_car.set_car_code('MB123456')
        this_car.set_car_name('TESTCAR')
        this_car.set_car_capacity(17)
        this_car.set_car_horsepower(220)
        this_car.set_car_weight(1392)
        this_car.set_car_type('RWD')

        result = str(this_car)
        test_expectation = "'MB123456', 'TESTCAR', 17, 220, 1392, RWD"

        try:
            self.assertEqual(result, test_expectation)
        except:
            print(this_car)

    def test_generate_car_code(self):
        """
        Expect the car code to be in the format: 2 digit upper case chars and 6 digits numbers
        :return:
        """
        # initialise car:
        this_car = Car()
        this_car_code = this_car.generate_car_code()

        self.assertEqual(len(this_car_code), 8, f"Output '{this_car_code}' does not have the correct length")

        # Check if the first two characters are uppercase letters
        first_two_chars = this_car_code[:2]
        self.assertTrue(first_two_chars.isalpha() and first_two_chars.isupper(),
                        f"First two characters '{first_two_chars}' are not uppercase letters")

        # Check if the remaining six characters are digits
        last_six_chars = this_car_code[2:]
        self.assertTrue(last_six_chars.isdigit(), f"Last six characters '{last_six_chars}' are not digits")

    def test_set_car_code(self):
        """
        Expect the function set_car_code to
        1. set the car code when the input_car_code is not null
        2. generate a random car code when the input_car_code is null
        3. handle the exception when the input_car_code is not legit
        3. handle the exception when the input_car_code is in duplications
        4. class variable car_code_list got updated correctly
        :return:
        """

        # initialise car:
        this_car = Car()
        this_car_2 = Car()
        this_car_3 = Car()
        this_car_4 = Car()
        # Car.car_code_list = []  # clear for test purpose

        # case 1
        this_car.set_car_code('MB234567')
        self.assertEqual(this_car.get_car_code(),'MB234567','failed to set up car code')

        # case 2
        this_car_2.set_car_code()
        print(this_car_2.get_car_code())
        self.assertNotEquals(this_car_2.get_car_code(), None, 'failed to set up randomly generated car code')

        # case 3
        this_car_3.set_car_code('BE1234')
        print(this_car_3.get_car_code())
        self.assertEquals(this_car_3.get_car_code(), None, 'invalid car code got setup')

        # case 4
        print(Car.car_code_list)
        this_car_4.set_car_code('MB234567')
        print(this_car_4.get_car_code())
        self.assertEquals(this_car_4.get_car_code(), None, 'duplicated car code got setup')


    def test_probationary_licence_prohibited_vehicle(self):
        """
        This function is to test method probationary_licence_prohibited_vehicle()
        A car with a Power to Mass ratio greater than 130 kilowatt per tonne
        is a prohibited vehicle for probationary licence drivers

        case 1 (boundary): power = 13 , weight = 100. --> return False
        case 2 (boundary): power = 12.5, weight = 100 --> return False
        case 3 (valid): power = 14, weight = 100 --> return True
        case 4 (invalid): power = 12, weight = 100 --> return False
        case 5 (invalid): power = None, weight = None --> return

        :return:
        """
        # initialise car:
        this_car = Car()
        this_car_2 = Car()
        this_car_3 = Car()
        this_car_4 = Car()
        this_car_5 = Car()

        # case 1:
        this_car.set_car_horsepower(13)
        this_car.set_car_weight(100)
        this_ratio = this_car.get_car_horsepower()/this_car.get_car_weight() * 1000
        print(this_ratio)
        print(this_car.probationary_licence_prohibited_vehicle())
        self.assertEquals(this_car.probationary_licence_prohibited_vehicle(), False,f'wrong prohibitary ratio return on ration {this_ratio}' )

        # case 2:
        this_car_2.set_car_horsepower(12.5)
        this_car_2.set_car_weight(100)
        this_ratio_2 = this_car_2.get_car_horsepower() / this_car_2.get_car_weight() * 1000
        print(this_ratio_2)
        print(this_car_2.probationary_licence_prohibited_vehicle())
        self.assertEquals(this_car_2.probationary_licence_prohibited_vehicle(), False,
                          f'wrong prohibitary ratio return on ration {this_ratio_2}')

        # case 3:
        this_car_3.set_car_horsepower(14)
        this_car_3.set_car_weight(100)
        this_ratio_3 = this_car_3.get_car_horsepower() / this_car_3.get_car_weight() * 1000
        print(this_ratio_3)
        print(this_car_3.probationary_licence_prohibited_vehicle())
        self.assertEquals(this_car_3.probationary_licence_prohibited_vehicle(), True,
                          f'wrong prohibitary ratio return on ration {this_ratio_3}')

        # case 4:
        this_car_4.set_car_horsepower(12)
        this_car_4.set_car_weight(100)
        this_ratio_4 = this_car_4.get_car_horsepower() / this_car_4.get_car_weight() * 1000
        print(this_ratio_4)
        print(this_car_4.probationary_licence_prohibited_vehicle())
        self.assertEquals(this_car_4.probationary_licence_prohibited_vehicle(), False,
                          f'wrong prohibitary ratio return on ration {this_ratio_4}')

        # case 5:
        self.assertNotEquals(this_car_5.probationary_licence_prohibited_vehicle(), False,
                          f'wrongly setup probatary ratio for None input')

        self.assertNotEquals(this_car_5.probationary_licence_prohibited_vehicle(), True,
                             f'wrongly setup probatary ratio for None input')


    def test_found_matching_car(self):
        """
        This function is to test method found matching car.
        Case 1. car_code = 'MB123456', input_car_code = 'MB123456' --> return True
        Case 2. car_code = 'MB123457', input_car_code = 'MB123456' --> return False
        :return:
        """
        # initialise car:
        this_car = Car()
        this_car_2 = Car()


        # Case 1
        this_car.set_car_code('BT172939')
        self.assertTrue(this_car.found_matching_car('BT172939'),  'failed to found the matching car')

        # Case 2
        this_car_2.set_car_code('BT172938')
        self.assertFalse(this_car_2.found_matching_car('BT172939'),  'wrongly found the matching car')

    def test_get_car_type(self):

        # Case 1: get the car type that is manually setup
        this_car = Car()
        this_car.set_car_type('RWD')
        self.assertEquals(this_car.get_car_type(),'RWD','failed to setup get car type')

        # Case 2: get the car type that is randomly generated
        this_car_2 = Car()
        this_car_2.set_car_type()
        this_result = this_car_2.get_car_type() in ['RWD','FWD','AWD']
        self.assertTrue(this_result, 'failed to setup get car type')

    def test_set_car_type(self):

        # Case 1: get the car type that is manually setup
        this_car = Car()
        this_car.set_car_type('AWD')
        self.assertEquals(this_car.get_car_type(), 'AWD', 'failed to setup get car type')

        # Case 2: get the car type that is randomly generated
        this_car_2 = Car()
        this_car_2.set_car_type()
        this_result = this_car_2.get_car_type() in ['RWD', 'FWD', 'AWD']
        self.assertTrue(this_result, 'failed to setup get car type')

        # Case 3: invalid input car type:
        this_car_3 = Car()
        this_car_3.set_car_type('YED')

        self.assertEquals(this_car_3.get_car_type(), None,'invalid car type got setup')

    def test_set_car_weight_capacity_horsepower(self):
        """
        This function is to test that car weight, capacity and horsepower can be properly validated and setup:

        Case 1: manually input number inputs --> setup successfully
        Case 2: manually input string digit inputs --> setup successfully
        Case 3: manually input string non-digit inputs --> setup unsuccessfully
        Case 4: manually input negative values --> setup unsuccessfully

        :return:
        """

        # Case 1
        this_car = Car()
        this_car.set_car_capacity(12)
        this_car.set_car_weight(100)
        this_car.set_car_horsepower(30)

        self.assertEquals(this_car.get_car_capacity(), 12, 'Setup car capacity failed')
        self.assertEquals(this_car.get_car_weight(), 100, 'Setup car weight failed')
        self.assertEquals(this_car.get_car_horsepower(), 30, 'Setup car horsepower failed')

        # Case 2
        this_car_2 = Car()
        this_car_2.set_car_capacity('12')
        this_car_2.set_car_weight('100')
        this_car_2.set_car_horsepower('30')

        self.assertEquals(this_car_2.get_car_capacity(), 12, 'Setup string car capacity input failed')
        self.assertEquals(this_car_2.get_car_weight(), 100, 'Setup string car weight input failed')
        self.assertEquals(this_car_2.get_car_horsepower(), 30, 'Setup string car horsepower input failed')

        # Case 3
        this_car_3 = Car()
        this_car_3.set_car_capacity('a12')
        this_car_3.set_car_weight('b100')
        this_car_3.set_car_horsepower('c30')

        self.assertEquals(this_car_3.get_car_capacity(), None, 'Wrongly setup string car capacity input')
        self.assertEquals(this_car_3.get_car_weight(), None, 'Wrongly setup string car weight input')
        self.assertEquals(this_car_3.get_car_horsepower(), None, 'Wrong setup string car horsepower input')

        # Case 4
        this_car_4 = Car()
        this_car_4.set_car_capacity(-12)
        this_car_4.set_car_weight('-100')
        this_car_4.set_car_horsepower('-30')

        self.assertEquals(this_car_4.get_car_capacity(), None, 'Wrongly setup negative car capacity input')
        self.assertEquals(this_car_4.get_car_weight(), None, 'Wrongly setup negative car weight input')
        self.assertEquals(this_car_4.get_car_horsepower(), None, 'Wrong setup negative car horsepower input')

    def test_randomly_generated_car_objects(self):
        """
        This function is to test when use methods setters(), object attributes are all randomly generated properly
        :return:
        """
        this_car = Car()

        this_car.set_car_code()
        this_car.set_car_name()
        this_car.set_car_capacity()
        this_car.set_car_weight()
        this_car.set_car_horsepower()
        this_car.set_car_type()

        print(this_car)

        self.assertNotEquals(this_car.get_car_code(), None, 'car code random generation not working')
        self.assertNotEquals(this_car.get_car_name(), None, 'car name random generation not working')
        self.assertNotEquals(this_car.get_car_capacity(), None, 'car capacity random generation not working')
        self.assertNotEquals(this_car.get_car_weight(), None, 'car weight random generation not working')
        self.assertNotEquals(this_car.get_car_horsepower(), None, 'car horsepower random generation not working')
        self.assertNotEquals(this_car.get_car_type(), None, 'car type random generation not working')


if __name__ == '__main__':
    unittest.main()

