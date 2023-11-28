import string
import unittest
from car import Car
from retailer import Retailer
from order import Order

class MyTestCase(unittest.TestCase):
    def test_generate_order_id(self):
        """
        To test if method generate_order_id work as expected:
        1. for valid car code and order creation time:
        the generated order id:

        Case 1:
        #first 6 chars are characters
        # 2nd, 4th and 6th char are uppercases
        # Only contains characters + digits +  "~!@#$%^&*"
        # Contains carcode and order creation time
        # Length should be 39

        Case 2. for None car code --> print message and does not generate order id
        Case 3. for None order creation time --> print message and does not generate order id
        Case 4. for different car code --> print message and does not generate order id
        :return:
        """
        # Case 1
        this_car = Car()
        this_order = Order()
        this_car.set_car_code('MB123456')
        this_order.set_order_car(this_car)
        this_order.set_order_creation_time(1672491601)

        this_generated_id = this_order.generate_order_id(this_order.get_order_car().get_car_code())
        print(this_generated_id)

        # first 6 chars are characters
        first_6_chars = this_generated_id[0:6]
        self.assertTrue(first_6_chars.isalpha(), f'{first_6_chars} not all characters')

        # 2nd, 4th and 6th char are upper cases
        even_chars = this_generated_id[1] + this_generated_id[3] + this_generated_id[5]
        self.assertTrue(even_chars.isupper(), f'{even_chars} not all upper cases')

        # Only contains characters + digits +  "~!@#$%^&*"
        permissable_chars = string.ascii_letters + string.digits + "~!@#$%^&*"
        self.assertTrue([a in permissable_chars for a in this_generated_id], f'{this_generated_id} contains non-permissble char')

        # Contains car code and order creation time
        must_contain_info = this_order.get_order_car().get_car_code() + str(this_order.get_order_creation_time())
        print(must_contain_info)
        self.assertTrue(must_contain_info in this_generated_id, f'{must_contain_info} does not in {this_generated_id}')

        # Check length: 39
        print(len(this_generated_id))
        self.assertEquals(len(this_generated_id),39 ,f'{this_generated_id} does not have 39 length')

        # Case 2
        this_car_2 = Car()
        this_order_2 = Order()
        this_order_2.set_order_car(this_car_2)
        this_order_2.set_order_creation_time(1672491601)
        self.assertEquals(this_order_2.generate_order_id(), None, 'order id for None car code wrongly setup')

        # Case 3
        this_car_3 = Car()
        this_car_3.set_car_code('MB123789')
        this_order_3 = Order()
        this_order_3.set_order_car(this_car_3)
        self.assertEquals(this_order_3.generate_order_id(), None, 'order id for None order creation time wrongly setup')

        # Case 4
        this_car_4 = Car()
        this_car_4.set_car_code('MB123788')
        this_order_4 = Order()
        this_order_4.set_order_car(this_car_4)
        self.assertEquals(this_order_4.generate_order_id('MB124788'), None, 'order id for different car code wrongly setup')

    def test_str(self):
        """
        To test if the __str__ is outputting correct format
        :return:
        """
        this_car = Car()
        this_car.set_car_code()

        this_retailer = Retailer()
        this_retailer.set_retailer_id()

        this_order = Order()
        this_order.set_order_car(this_car)
        this_order.set_order_retailer(this_retailer)
        this_order.set_order_creation_time()
        this_order.set_order_id()


        print( this_order)
        print(f'this order has a creation time: {this_order.get_order_creation_time()}')

        expected_output = f'{this_order.get_order_id()}, {this_order.get_order_car().get_car_code()}, {this_order.get_order_retailer().get_retailer_id()}, {this_order.get_order_creation_time()}'

        self.assertEquals(str(this_order), expected_output, f'{str(this_order)} does not follow the correct format')



if __name__ == '__main__':
    unittest.main()
