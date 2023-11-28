import random
import string


class Retailer:

    # use a retailer_id_list to collect all retailer_ids
    retailer_id_list = []

    # use a retailer object list to collect all retailer objects created
    retailer_object_universe_list = []

    def __init__(self):
        self.retailer_id = None
        self.retailer_name = None

        # append to the object universe once initiated:
        Retailer.retailer_object_universe_list.append(self)

    def generate_retailer_id(self):
        """
        To generate a unique 8-digit retailer id
        :param self, retailer_id_list
        :return:
        """
        use_id = ''
        input_retailer_id_list = [each_retailer.get_retailer_id() for each_retailer in Retailer.retailer_object_universe_list]
        while True:
            this_id = ''
            digits_set = string.digits
            for i in range(0, 8):
                this_digit = random.choice(digits_set)
                this_id += this_digit

            if this_id not in input_retailer_id_list:
                use_id = this_id
                break
        return use_id


    def generate_random_retailer_name(self):
        """
        This function is to generate random retailer name.
        Output should be in format: ULTnkYQ QN
        :return:
        """
        retailer_name_length = random.randint(4, 15)
        retailer_name_str = ''

        for i in range(0, retailer_name_length):
            choice_set = string.ascii_letters + " "
            this_char = random.choice(choice_set)
            retailer_name_str += this_char

        return retailer_name_str



    def set_retailer_id(self, input_id = None):
        if input_id == None:
            this_retailer_id = self.generate_retailer_id()
            self.retailer_id = this_retailer_id
            Retailer.retailer_id_list.append(this_retailer_id)

        else:
            if self.validate_retailer_id(input_id) == True:
                self.retailer_id = str(input_id)
                Retailer.retailer_id_list.append(str(input_id))



    def set_retailer_name(self, input_name = None):
        if input_name == None:
            input_name = self.generate_random_retailer_name()

        if_valid = self.validate_retailer_name(input_name)
        if if_valid is True:
            self.retailer_name = str(input_name)
        else:
            print(f'Input name not valid {input_name}')

    def validate_retailer_id(self,input_id, input_retailer_id_list = retailer_id_list):
        """
        To validate if the retailer id is valid:
        - consists of 8 digits
        - not in duplicates

        :param input_id:
        :param input_retailer_id_list:
        :return: True: valid; False: Invalid
        """
        if len(input_id) != 8:
            print(f'{input_id} does not have 8 digits')
            return False

        elif str(input_id).isdigit() == False:
            print(f'{input_id} contains non-digit character')
            return False
        elif str(input_id) in input_retailer_id_list:
            print(f'{input_id} already exists')
            return False

        else:
            return True

    def validate_retailer_name(self, input_name):
        """
        to validate if the name only consists of letters and whitespace
        :param input_name:
        :return:
        """
        valid_chars = string.ascii_letters + " "

        valid_char_list = [i for i in valid_chars]

        this_name = str(input_name)
        for this_char in this_name:
            if this_char not in valid_char_list:
                return False

        return True

    def get_retailer_id(self):
        return self.retailer_id

    def get_retailer_name(self):
        return self.retailer_name

    def get_retailer_id_list(self):
        return Retailer.retailer_id_list

    def __str__(self):
        output_str = f'{self.retailer_id}, {self.retailer_name}'
        return output_str
