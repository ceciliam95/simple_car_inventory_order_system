import string
import random
import math


class Car:

    # use a class variable car_code_list to collect all car codes
    car_code_list = []
    # use a class variable to store all car objects that have been created
    car_object_universe_list = []

    def __init__(self):
        self.car_code = None
        self.car_name = None
        self.car_capacity = None
        self.car_horsepower = None
        self.car_weight = None
        self.car_type = None
        # self.car_color = None

        # append this object to the car universe once initiated:
        Car.car_object_universe_list.append(self)

    # def generate_random_car_color(self):
    #     random_color = ['R','Y','B']
    #     random_choice = random.choice(random_color)
    #
    #     return random_choice

    def generate_car_code(self):
        """
        Generate a unique 6-digit car code (2 uppercase + 6 digits)
        e.g MB123456
        """
        use_car_code = ''
        input_car_code_list = [each_car.get_car_code() for each_car in Car.car_object_universe_list]
        while True:
            this_car_code = ''
            digits_set = string.digits
            upper_char_set = string.ascii_uppercase

            for i in range(0, 8):
                if i <= 1:
                    this_digit = random.choice(upper_char_set)
                else:
                    this_digit = random.choice(digits_set)
                this_car_code += this_digit

            if this_car_code not in input_car_code_list:
                use_car_code = this_car_code
                break
        return use_car_code

    def generate_random_car_name(self):
        """
        The function is to generate a random car name
        Sample output: 'jEJPRJ qNTOlvhmWpw'

        :return:
        """
        random_car_name_length = random.randint(10,20)
        random_car_name_str = ''
        choice_set = string.ascii_letters + ' '
        for i in range(0,random_car_name_length):
            this_char = random.choice(choice_set)
            random_car_name_str += this_char

        return random_car_name_str

    def generate_random_car_capacity(self):
        """
        This function is to generate random car capacity (5,50)
        Sample Output: 17
        :return:
        """
        this_car_capacity = random.randint(5,50)
        return this_car_capacity

    def generate_random_car_horsepower(self):
        """
        This function is to generate random car horsepower (180,250)
        Sample Output: 17
        :return:
        """
        this_car_horsepower = random.randint(180,250)
        return this_car_horsepower

    def generate_random_car_weight(self):
        """
        This function is to generate random car weight (1300,2000) kg
        Sample Output: 17
        :return:
        """
        this_car_weight = random.randint(1300,2000)
        return this_car_weight

    def generate_random_car_type(self):
        """
        This function is to generate a random car type, from list ['FWD', 'RWD', 'AWD']
        Sample Output: 'FWD'
        :return:
        """
        choice_set = ['FWD', 'RWD', 'AWD']
        this_car_type = random.choice(choice_set)
        return this_car_type

    # def set_car_color(self, input_car_color = None):
    #     if inpu

    def set_car_code(self, input_car_code = None):
        """
        to set the car_code from generate_car_code (if no input car code)
        """

        if input_car_code != None:

            if self.validate_car_code (input_car_code) == True:
                self.car_code = input_car_code
                Car.car_code_list.append(input_car_code)
        else:
            this_car_code = self.generate_car_code()
            self.car_code = this_car_code
            Car.car_code_list.append(this_car_code)

    def set_car_name(self, input_car_name = None):

        if input_car_name != None:
            self.car_name = input_car_name
        else:
            self.car_name = self.generate_random_car_name()


    def set_car_capacity(self, this_capacity = None):
        if this_capacity != None:
            if self.validate_car_capacity_weight_horsepower(this_capacity) == True:
                self.car_capacity = float(this_capacity)
        else:
            self.car_capacity = self.generate_random_car_capacity()


    def set_car_horsepower(self, this_horsepower = None):
        if this_horsepower != None:
            if self.validate_car_capacity_weight_horsepower(this_horsepower) == True:
                self.car_horsepower = float(this_horsepower)
        else:
            self.car_horsepower = self.generate_random_car_horsepower()

    def set_car_weight(self, this_car_weight = None):
        if this_car_weight != None:
            if self.validate_car_capacity_weight_horsepower(this_car_weight) == True:
                self.car_weight = float(this_car_weight)
        else:
            self.car_weight = self.generate_random_car_weight()


    def set_car_type(self, this_car_type = None):
        if this_car_type in ['FWD', 'RWD', 'AWD']:
            self.car_type = this_car_type

        elif this_car_type == None:
            self.car_type = self.generate_random_car_type()

        else:
            print(f'Invalid input car type: {this_car_type}')

    def validate_car_capacity_weight_horsepower(self, input_info):
        """
        This method is to ensure the input for car capacity, car weight and car horsepower is valid:
        1. Valid digits
        2. No Negative values

        :param input_info:
        :return: True: valid input; False: invalid input
        """
        if isinstance(input_info,str) == True:
            if input_info.isdigit() == False:
                print(f'{input_info} is not digits')
                return False

        cleaned_info = float(input_info)
        if cleaned_info <= 0:
            print(f'{input_info} is negative')
            return False
        else:
            return True


    def validate_car_code (self, input_car_code, input_car_code_list = car_code_list):
        """
        To validate if the car code is valid:
        1. 2 uppercases + 6 digits
        2. not in duplication
        :param input_car_code_list:
        :return: True - valid; False - not valid
        """
        try:
            first_two_digits = input_car_code[:2]
            last_dix_digits = input_car_code[2:]
        except:
            print(f'invalid car code format {input_car_code}')

        if input_car_code in input_car_code_list:
            print(f"Duplicated car code {input_car_code}")
            print(f"Following car codes already in the system {input_car_code_list}")
            return False

        elif len(input_car_code) != 8:
            print(f'{input_car_code} does not have 8 digits')
            return False

        elif (first_two_digits.isalpha() and first_two_digits.isupper()) == False:
            print(f"{first_two_digits[:2]} are not uppercase letters")
            return False

        elif last_dix_digits.isdigit() == False:
            print(f"Last six characters '{last_dix_digits}' are not digits")
            return False
        else:
            return True


    def get_car_code(self):
        return self.car_code

    def get_car_name(self):
        return self.car_name

    def get_car_capacity(self):
        return self.car_capacity

    def get_car_horsepower(self):
        return self.car_horsepower

    def get_car_weight(self):
        return self.car_weight

    def get_car_type(self):
        return self.car_type

    def __str__(self):
        output_str = f'{self.car_code}, {self.car_name}, {self.car_capacity}, {self.car_horsepower}, {self.car_weight}, {self.car_type}'

        return output_str

    def probationary_licence_prohibited_vehicle(self):
        this_power = self.get_car_horsepower()
        this_mass = self.get_car_weight()
        try:
            this_power_to_mass = math.ceil((this_power / this_mass) * 1000)
        except (TypeError, ZeroDivisionError, ValueError):
            print(f'Invalid inputs: car power {this_power}, car weight: {this_mass}')
            return
        else:
            if this_power_to_mass > 130:
                return True
            else:
                return False

    def found_matching_car(self, this_car_code):
        if this_car_code == self.car_code:
            return True
        else:
            return False


