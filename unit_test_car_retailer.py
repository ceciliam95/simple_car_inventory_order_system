import os
import unittest
from car_retailer import CarRetailer
from car import Car

test_car_1 = Car()
test_car_1.set_car_code('RV952919')
test_car_1.set_car_type('AWD')

test_car_2 = Car()
test_car_2.set_car_code('MW137203')
test_car_2.set_car_type('RWD')

test_car_3 = Car()
test_car_3.set_car_code('VD526034')
test_car_3.set_car_type('AWD')

class MyTestCase(unittest.TestCase):
    def test_load_current_stock(self):
        """
        This function is to test if load_current_stock is working as expected:

        Case 1: input with default stock.txt file path
        set retailer_id = '21980939' per test stock
        this_car_retailer.get_carretailer_stock() = ['EU565135','OQ533264','DM363293','FK953041']

        Case 2: input with stock.txt file path specified
        set retailer_id = '21980939' per test stock
        this_car_retailer.get_carretailer_stock() = ['EU565135','OQ533264','DM363293','FK953041']

        Case 3: this retailer_id does not exist in the input file:
        print an error message and return

        Case 4: the file path does not exist

        Case 5: wrong file (i.e not stock txt)

        :return:
        """
        # Case 1
        this_car_retailer = CarRetailer()
        this_car_retailer.set_retailer_id('21980939')

        this_car_retailer.load_current_stock(CarRetailer.static_stock_file_path)
        this_current_stock = this_car_retailer.get_carretailer_stock()

        this_expected_output = ['EU565135','OQ533264','DM363293','FK953041']
        print(this_current_stock)
        self.assertEquals(this_current_stock,this_expected_output, f'{this_current_stock} not updated correctly')

        # Case 2
        this_stock_file_path = f'{os.getcwd()}\data\stock.txt'
        this_car_retailer_2 = CarRetailer()
        this_car_retailer_2.set_retailer_id('22927521')

        this_car_retailer_2.load_current_stock(this_stock_file_path)
        this_current_stock_2 = this_car_retailer_2.get_carretailer_stock()

        this_expected_output_2 = ['PX101073', 'QZ278951', 'HP701271', 'GN448578']
        print(this_current_stock_2)
        self.assertEquals(this_current_stock_2, this_expected_output_2, f'{this_current_stock_2} not updated correctly')

        # Case 3
        this_stock_file_path = f'{os.getcwd()}\data\stock.txt'
        this_car_retailer_3 = CarRetailer()
        this_car_retailer_3.set_retailer_id('60661173')

        this_car_retailer_3.load_current_stock(this_stock_file_path)
        this_current_stock_3 = this_car_retailer_3.get_carretailer_stock()

        print(this_current_stock_3)
        self.assertEquals(this_current_stock_3, [], f'{this_current_stock_3} not updated correctly')

        # Case 4
        this_test_file_path = f'{os.getcwd()}\data\inventory.txt'
        this_car_retailer_4 = CarRetailer()
        this_car_retailer_4.set_retailer_id('60661171')

        this_car_retailer_4.load_current_stock(this_test_file_path)
        this_current_stock_4 = this_car_retailer_4.get_carretailer_stock()

        print(this_current_stock_4)
        self.assertEquals(this_current_stock_4, [], f'{this_current_stock_4} not updated correctly')

        # Case 5
        this_test_file_path_5 = f'{os.getcwd()}\data\order.txt'
        this_car_retailer_5 = CarRetailer()
        this_car_retailer_5.set_retailer_id('60661177')

        this_car_retailer_5.load_current_stock(this_test_file_path_5)
        this_current_stock_5 = this_car_retailer_5.get_carretailer_stock()

        print(this_current_stock_5)
        self.assertEquals(this_current_stock_5, [], f'{this_current_stock_5} not updated correctly')

    def test_is_operating(self):
        """
        To test if method is_operating() work as expected:

        Case 1 (valid case):
        --> set operating hour (14.5,22.5)
        --> check 17.5
        --> return True

        Case 2 (invalid case):
         --> set operating hour (14.5,22.5)
        --> check 22.7
        --> return False

        Case 3 (boundary case):
         --> set operating hour (14.5,22.5)
        --> check 22.5
        --> return True

        Case 4 (invalid case):
         --> set operating hour (14.5,22.5)
        --> check 'abc'
        --> return False, and also print error message

        Case 5 (invalid case):
         --> set operating hour (14.5,22.5)
        --> check 24.1
        --> return False, and also print error message

        Case 6 (invalid case):
        --> operating hour is None
        --> check 17.5
        --> return False and also print error message

        :return:
        """
        # Case 1
        this_retailer_1 = CarRetailer()
        this_retailer_1.set_carretailer_business_hours((14.5,22.5))
        print(this_retailer_1.get_carretailer_business_hours())
        self.assertTrue(this_retailer_1.is_operating(17.5))
        # Case 2
        self.assertFalse(this_retailer_1.is_operating(22.7))
        # Case 3
        self.assertTrue(this_retailer_1.is_operating(22.5))
        # Case 4
        self.assertFalse(this_retailer_1.is_operating('abc'))
        # Case 5
        self.assertFalse(this_retailer_1.is_operating(24.1))
        # Case 6
        this_retailer_2 = CarRetailer()
        print(this_retailer_2.get_carretailer_business_hours())
        self.assertFalse(this_retailer_2.is_operating(17.5))

    def test_get_postcode_distance(self):
        """
        To test if method get_postcode_distance() is working as expected:

        Case 1 (valid)
        --> set address as 'Jaqfb Crescent Oakry, VIC3431'
        --> check input address 3400
        --> return 31

        Case 2 (invalid)
        --> set address as 'Jaqfb Crescent Oakry, VIC3431'
        --> check input address '34ab'
        --> return and print error message

        Case 3 (invalid):
        --> don't set the address
        --> input 3400
        ..> return and print error message

        Case 4 (invalid):
        --> set address as 'Jaqfb Crescent Oakry'
        --> check input address '3400'
        --> return and print error message

        :return:
        """
        # Case 1
        this_retailer_1 = CarRetailer()
        this_retailer_1.set_carretailer_address('Jaqfb Crescent Oakry, VIC3431')
        self.assertEquals(this_retailer_1.get_postcode_distance(3400),31,f'get postcode distance does not work')
        self.assertEquals(this_retailer_1.get_postcode_distance('3400'), 31, f'get postcode distance does not work')

        # Case 2
        self.assertIsNone(this_retailer_1.get_postcode_distance('34ab'), f'did not handle invalid input')

        # Case 3
        this_retailer_2 = CarRetailer()
        self.assertIsNone(this_retailer_2.get_postcode_distance('3400'), f'did not handle None default')

        # Case 3
        this_retailer_3 = CarRetailer()
        this_retailer_3.set_carretailer_address('Jaqfb Crescent Oakry')
        self.assertIsNone(this_retailer_3.get_postcode_distance('3400'), f'did not handle invalid address default')

    def test_get_all_stock(self):
        """
        To test method get_all_stock() working as expected:

        Case 1:
        :return:
        """

        # Case 1

        #Reuse:

        # this_car_retailer = None
        # for each_retailer in CarRetailer.retailer_object_universe_list:
        #     if each_retailer.get_retailer_id() == '60661174':
        #         this_car_retailer = each_retailer

        this_car_retailer = CarRetailer()
        this_car_retailer.set_retailer_id('60661174')

        print(this_car_retailer)
        this_car_retailer.load_current_stock(CarRetailer.static_stock_file_path)
        this_current_stock = this_car_retailer.get_carretailer_stock()

        output_list = this_car_retailer.get_all_stock()

        output_car_code_list = [car.get_car_code() for car in output_list]

        for each_car in output_list:
           print(each_car)

        # check item in output_list are all Cars:
        self.assertTrue([isinstance(item,Car) for item in output_list], f'output not list of cars')
        self.assertEquals(output_car_code_list, ['RV952919','MW137203','VD526034'], f'output list not correct')

    def test_get_by_car_type(self):
        """
        To test if the method get_by_car_type is working as expected:

        Case 1: input a string of car type

        Case 2: input a list of car type

        Case 3: input invalid car type
        :return:
        """
        # Case 1

        #Reuse:
        this_car_retailer = None
        for each_retailer in CarRetailer.retailer_object_universe_list:
            if each_retailer.get_retailer_id() == '60661174':
                this_car_retailer = each_retailer

        selected_by_car_type = this_car_retailer.get_stock_by_car_type('AWD')
        output_car_code_list_1 = [car.get_car_code() for car in selected_by_car_type]


        for each_car in selected_by_car_type:
            print(each_car)

        #check item in output_list are all Cars:
        self.assertTrue([isinstance(item,Car) for item in selected_by_car_type], f'output not list of cars')
        self.assertEquals(output_car_code_list_1, ['RV952919','VD526034'], f'output list not correct')

        # Case 2
        selected_by_car_type_2 = this_car_retailer.get_stock_by_car_type(['AWD','RWD'])
        output_car_code_list_2 = [car.get_car_code() for car in selected_by_car_type_2]
        self.assertEquals(output_car_code_list_2, ['RV952919','MW137203', 'VD526034'], f'output list not correct')

        # Case 3
        selected_by_car_type_3 = this_car_retailer.get_stock_by_car_type(['AWD','TWD'])

        self.assertEquals(selected_by_car_type_3, None , f'invalid input not handled correctly')

    def test_remove_and_add_from_stock(self):
        """
        To test if remove_from_stock and add_from_stock method is working as expected:

        Case 1:
        Retailer 22480554
        Car Stock: ['HJ354434', 'HK914625','NB284994','YT833516']
        remove 'YT833516'
        --> should return True

        Case 2:
        remove 'YT833523'
        --> should return False

        Case 3
        add 'RV952919'
        --> should return True

        Case 4
        add UV302164
        --> should return False

        Case 5
        add 'UV088655'
        --> should return False
        :return:
        """
        current_dir = os.getcwd()
        stock_file_path = f'{current_dir}\data\/test2_stock.txt'

        CarRetailer.static_stock_file_path = stock_file_path

        this_car_retailer = CarRetailer()
        this_car_retailer.set_retailer_id('91353351')
        this_car_retailer.set_retailer_name('QVtlPAv')
        this_car_retailer.set_carretailer_address('Nxf oxwuqc Drive Gbxxwg, WA6426')
        this_car_retailer.set_carretailer_business_hours((10.8, 21.8))

        test_car_1 = Car()
        test_car_1.set_car_code('UV088664')
        test_car_1.set_car_name('ayuvkAZ hhAmfBocZ')
        test_car_1.set_car_type('AWD')
        test_car_1.set_car_capacity(17)
        test_car_1.set_car_horsepower(223)
        test_car_1.set_car_weight(1573)

        test_car_2 = Car()
        test_car_2.set_car_code('GD827949')
        test_car_2.set_car_name('fQKNksXQKYsP YRK')
        test_car_2.set_car_type('RWD')
        test_car_2.set_car_capacity(15)
        test_car_2.set_car_horsepower(219)
        test_car_2.set_car_weight(1379)

        test_car_3 = Car()
        test_car_3.set_car_code('GT229256')
        test_car_3.set_car_name('HAonNjsJPc')
        test_car_3.set_car_type('FWD')
        test_car_3.set_car_capacity(10)
        test_car_3.set_car_horsepower(202)
        test_car_3.set_car_weight(1696)

        test_car_4 = Car()
        test_car_4.set_car_code('AR014442')
        test_car_4.set_car_name('FaBkOTFMTRaZBt')
        test_car_4.set_car_type('AWD')
        test_car_4.set_car_capacity(14)
        test_car_4.set_car_horsepower(194)
        test_car_4.set_car_weight(1652)

        test_car_5 = Car()
        test_car_5.set_car_code('RV952921')
        test_car_5.set_car_name('liwJOxLdmtcyeM')
        test_car_5.set_car_type('FWD')
        test_car_5.set_car_capacity(7)
        test_car_5.set_car_horsepower(284)
        test_car_5.set_car_weight(1524)

        this_car_retailer.set_carretailer_stock(['UV088664','GD827949','GT229256'])

        # Case 1
        test_bool = this_car_retailer.remove_from_stock('UV088664')
        self.assertTrue(test_bool, f'remove from stock not correct')

        # Case 2
        test_bool_2 = this_car_retailer.remove_from_stock('IR325888')
        self.assertFalse(test_bool_2, f'remove from stock not correct')

        # Case 3
        test_bool_3 = this_car_retailer.add_from_stock('RV952921')
        self.assertTrue(test_bool_3, f'add from stock not correct')

        # Case 4
        test_bool_4 = this_car_retailer.add_from_stock('GD827949')
        self.assertFalse(test_bool_4, f'add from stock not correct')


        # Case 5
        test_bool_5 = this_car_retailer.add_from_stock('UV088655')
        self.assertFalse(test_bool_5, f'add from stock not correct')

        this_car_retailer.create_order('RV952921')





if __name__ == '__main__':
    unittest.main()
