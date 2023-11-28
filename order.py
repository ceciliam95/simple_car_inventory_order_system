import string
import random
import time
from car import Car
from retailer import Retailer

class Order:

    # Setup an order class variable
    order_id_list = []

    # Setup an order object universe list:
    order_obj_universe_list = []

    def __init__(self):
        self.order_id = None
        self.order_car = None
        self.order_retailer = None
        self.order_creation_time = None

        # Append to order object universe list once initiated:
        Order.order_obj_universe_list.append(self)

    def __str__(self):
        try:

            output_str = f'{self.order_id}, {self.order_car.car_code}, {self.order_retailer.retailer_id}, {self.order_creation_time}'
        except ValueError:
            print('Order not created')
        else:
            return output_str


    def generate_order_id(self, input_car_code = None):
        str_1 = "~!@#$%^&*"

        # Step 0: check if hte input car code is correct
        if input_car_code is None:
            # if None is inputted, default to self.car_code first:
            input_car_code = self.get_order_car().get_car_code()
            if input_car_code is None:
                print('input car code is None')
                return None

        if str(input_car_code) != self.get_order_car().get_car_code():
            print(f'{input_car_code} is not the car code for this order')
            print(f'the car code for this order: {self.get_order_car().get_car_code()}')
            return None


        if self.get_order_creation_time() is None:
            print('This order does not have a creation time')
            return None

        # step 1: generate random string
        this_random_code = ''
        lower_char_set = string.ascii_lowercase

        for i in range(0, 6):
            this_digit = random.choice(lower_char_set)
            this_random_code += this_digit

        # step 2: convert to upper case for every second
        this_upper_str = ''
        for i in range(0, 6):
            if i in (1, 3, 5):
                this_char = this_random_code[i].upper()
            else:
                this_char = this_random_code[i]
            this_upper_str += this_char

        # step 3: get ASCII code:
        this_ascii_list = [ord(i) for i in this_upper_str]

        # step 4: ^2 for each ASCII code and get remainder:
        this_str_1_len = len(str_1)
        this_index_list = []
        for i in range(0, len(this_ascii_list)):
            this_code = this_ascii_list[i]
            this_pwr_two = this_code ** 2
            this_remainder = this_pwr_two % this_str_1_len
            this_index_list.append(this_remainder)

        # step 5: get corresponding char from str_1:
        this_corr_char_list = []
        for item in this_index_list:
            this_char = str_1[item]
            this_corr_char_list.append(this_char)

        # step 6: append corr char to upper str:
        this_combo_str = this_upper_str[:]

        for i in range(0, len(this_upper_str)):
            this_corr_char = this_corr_char_list[i]
            this_corr_char_n = this_corr_char * i
            this_combo_str += this_corr_char_n

        # step_7: append car code and order creation time:
        this_final_str = this_combo_str[:]
        this_final_str += input_car_code
        this_final_str += str(self.order_creation_time)

        return this_final_str

    def generate_order_creation_time(self):
        """
        This method will return the now time in UNIX timestamp
        :return: a UNIX timestamp of now()
        """
        this_timestamp = int(time.time())
        return this_timestamp


    def set_order_id(self):
        if self.order_id == None:
            self.order_id = self.generate_order_id()
        else:
            print(f'This order already has an id: {self.get_order_id()}')

    def set_order_car(self, input_car):

        cars_ordered = [this_order.get_order_car() for this_order in Order.order_obj_universe_list]
        if isinstance(input_car, Car) is False:
            print(f'{input_car} is not a Car object.')
            return
        # Check if this car has been ordered:
        if input_car in cars_ordered:
            print(f'Car {input_car.get_car_code()} has been ordered.')
            return
        self.order_car = input_car

    def set_order_retailer(self, input_retailer):
        if isinstance(input_retailer, Retailer):
            self.order_retailer = input_retailer
        else:
            print(f'{input_retailer} is not a Retailer object.')

    def set_order_creation_time(self, input_timestamp = None):
        if self.order_creation_time == None:
            if input_timestamp == None:
                self.order_creation_time = self.generate_order_creation_time()
            else:
                if self.validate_order_creation_time(input_timestamp) == True:
                    self.order_creation_time = int(input_timestamp)
                else:
                    print(f'this input timestamp invalid: {input_timestamp}')
        else:
            print(f'this order already has an order creation time: {self.generate_order_creation_time()}')

    def validate_order_creation_time(self, input_timestamp):
        """
        to validate if the input is a valid UNIX timestamp
        :return:
        """
        try:
            # Attempt to convert the timestamp to a valid time using time.gmtime
            time.gmtime(int(input_timestamp))
            return True
        except (ValueError,TypeError):
            return False

    def get_order_id(self):
        return self.order_id

    def get_order_car(self):
        return self.order_car

    def get_order_retailer(self):
        return self.order_retailer

    def get_order_creation_time(self):
        return self.order_creation_time
