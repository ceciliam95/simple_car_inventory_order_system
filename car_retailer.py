from retailer import Retailer
from car import Car
from order import Order

import os
import random
import string



class CarRetailer(Retailer):
	# Keep the file path fixed:
	current_dir = os.getcwd()
	static_stock_file_path = f'{current_dir}\data\/test_stock.txt'
	static_order_file_path = f'{current_dir}\data\/test2_order.txt'


	def __init__(self):
		# Call the constructor of the parent class to initialize 'name'

		# retailer id and name constructed
		super().__init__()
		self.carretailer_address = None
		self.carretailer_business_hours = None   # should be a tuple
		self.carretailer_stock = []

	def __str__(self):
		out_str = f'{self.retailer_id}, {self.retailer_name}, {self.carretailer_address}, {self.carretailer_business_hours}, {self.carretailer_stock}'

		return out_str

	def generate_random_postcode(self):
		"""
		This function is used to randomly generate postcode and state
		The sample output should be "VIC3170" "NSW2000" etc
		:return:
		"""
		# Step 1: randomly generate a four-digit string first
		random_number = random.randint(800, 7999)
		random_string = str(random_number).zfill(4)

		# Step 2: determine the state based on the randomly-generated number:
		if random_number <= 999:
			cor_state = 'NT'
		elif (random_number <= 2999) and random_number not in range(2600, 2920):
			cor_state = 'NSW'
		elif random_number <= 3999:
			cor_state = 'VIC'
		elif random_number <= 4999:
			cor_state = 'QLD'
		elif random_number <= 5999:
			cor_state = 'SA'
		elif random_number <= 6999:
			cor_state = 'WA'
		elif random_number <= 7999:
			cor_state = 'TAS'
		else:
			cor_state = 'ACT'

		# Step 3: output the postcode:
		final_postcode = cor_state + random_string

		return final_postcode

	def generate_random_address(self):
		"""
		This function is to generate some random address
		Output should be a string
		Sample output: Clayton Rd Clayton, VIC3170
		:return:
		"""
		# generate road type:
		road_type = ['Road', 'Crescent', 'Drive', 'Lane', 'Street']
		this_index = random.randint(0, 4)
		road_type_string = road_type[this_index]

		# generate road name:
		road_name_length = random.randint(5, 15)
		road_name_string = ''
		for i in range(0, road_name_length):
			if i == 0:
				this_char = random.choice(string.ascii_uppercase)
			else:
				choice_set = string.ascii_lowercase + " "
				this_char = random.choice(choice_set)
			road_name_string += this_char

		# generate suburb name:
		suburb_length = random.randint(5, 8)
		suburb_name_string = ''
		for i in range(0, suburb_length):
			if i == 0:
				this_char = random.choice(string.ascii_uppercase)
			else:
				this_char = random.choice(string.ascii_lowercase)
			suburb_name_string += this_char

		# generate random postcode:
		post_code_str = self.generate_random_postcode()

		final_address = road_name_string + " " + road_type_string + " " + suburb_name_string + ", " + post_code_str
		return final_address


	def generate_random_business_hour(self):
		"""
		This function is to randomly generate business hours
		Ouput will be a tuple
		Sample output: (10.9,14.5)
		:return:
		"""
		# step 1: get the start time:
		start_time = round(random.uniform(0.0, 23.0), 1)

		# step 2: get the end time, ensure at least one hour of operating time:
		end_time = round(random.uniform(start_time + 1, 24.0), 1)

		final_operating_hour = (start_time, end_time)

		return final_operating_hour


	def set_carretailer_address(self, input_address = None):
		if input_address != None:
			self.carretailer_address = input_address
		else:
			self.carretailer_address = self.generate_random_address()

	def set_carretailer_business_hours(self, input_business_hours = None):
		if input_business_hours != None:
			self.carretailer_business_hours = input_business_hours
		else:
			self.carretailer_business_hours = self.generate_random_business_hour()

	def set_carretailer_stock(self, input_car_stock):
		self.carretailer_stock = input_car_stock

	def get_carretailer_stock(self):
		return self.carretailer_stock

	def get_carretailer_address(self):
		return self.carretailer_address

	def get_carretailer_business_hours(self):
		return self.carretailer_business_hours

	def get_carretailer_stock(self):
		return self.carretailer_stock

	def validate_file_path(self, file_name_key_word ,input_stock_file_path ):
		"""
		Validate if the input file path is legit:
		1. it exists
		2. it contains file name key word: e.g stock.txt
		:param input_stock_file_path:
		:return: True - valid; False - invalid
		"""
		if os.path.exists(input_stock_file_path) == False:
			print(f'this file path does not exists: {input_stock_file_path}')
			return False
		elif str(file_name_key_word) not in input_stock_file_path:
			print(f'this file is not the one to use: {input_stock_file_path}')
			print(f'please look for file with key word {file_name_key_word} in name')
			return False
		else:
			return True


	def read_stock_data(self, stock_file_path):
		"""
		This function is to read the stock.txt data
		:return: a dictionary with retailer as the key and car stock as the values
		"""
		print(stock_file_path)
		# read the entire content of the file and return it as a list
		file_handle = open(stock_file_path, 'r')
		list_of_lines = file_handle.readlines()
		file_handle.close()

		output_retailer_stock_dict = {}

		#clean the input data
		stock_data_input = []
		for item in list_of_lines:
			components = item.replace("\n", "").split('), [')
			retailer_str = components[0] + ')'
			stock_str = '['+components[1]

			# clean retailer component:
			retailer_component = retailer_str.split(',')

			retailer_component_cleaned = [each_str.replace("(", "").strip('(').strip("')").lstrip(' ') for each_str in retailer_component]


			stock_component = stock_str.split("',")
			stock_component_cleaned = []
			# clean stock component:
			for each_stock_component in stock_component:
				each_car_list = each_stock_component.split(',')
				cleaned_car_list = [each_str.strip('[').strip(']').strip('] "').lstrip(' ').strip("'") for each_str in each_car_list]
				stock_component_cleaned.append(cleaned_car_list)

			output_retailer_stock_dict[tuple(retailer_component_cleaned)] = stock_component_cleaned

		return output_retailer_stock_dict

	def update_stock_file(self, stock_file_path):
		"""
		This function is to update the stock file. Only update the line related to this CarRetailer
		:param stock_file_path: provided at the beginning of the py file as a default value
		:return:
		"""
		# Step 1: get current stock of car objects
		updated_car_codes = self.get_carretailer_stock()

		current_stock_car_obj = [each_car for each_car in Car.car_object_universe_list if each_car.get_car_code() in updated_car_codes ]

		assigned_car_str = str([str(this_car) for this_car in current_stock_car_obj])
		this_retailer_id = self.get_retailer_id()

		retailer_str = f'{self.retailer_id}, {self.retailer_name}, {self.carretailer_address}, {self.carretailer_business_hours}'

		this_updated_line = f'{retailer_str}, {assigned_car_str} \n'


		# Step 2: open the file and update it
		try:
			with open(stock_file_path, 'r') as this_file:
				lines = this_file.readlines()
				target_index = None
				for each_line in lines:
					if this_retailer_id in each_line:
						target_index = lines.index(each_line)

				updated_lines = lines[:]
				# print('Line:')
				# for i in range(0, len(lines)):
				# 	print(f'{i}: {lines[i]}')

				if (target_index != None):
					initial_line = updated_lines[target_index]
					if initial_line != this_updated_line:
						updated_lines[target_index] = this_updated_line

				# print('Updated:')
				# for i in range(0, len(updated_lines)):
				# 	print(f'{i}: {updated_lines[i]}')
			this_file.close()

			with open(stock_file_path, 'w') as this_file:
				this_file.writelines(updated_lines)
			this_file.close()



		except:
			print('File update failed')
			return False
		else:
			print('stock txt file updated')
			return True

	def update_order_file(self, input_order, order_file_path):
		"""
		To update the order file. Append new order as new lines
		:param input_order: an Order object.
		:param order_file_path:
		:return: boolean
		"""
		this_order_line = str(input_order) +'\n'

		try:
			with open(order_file_path, 'a+') as this_file:
				this_file.writelines(this_order_line)
			this_file.close()
		except:
			print('order file update failed.')
			return False
		else:
			print('order file updated')
			return True

	def search_car_objects (self, car_object_list, by_type = None, match_by = None):
		"""
		This function is to return a list of car objects based on searching type and searching key words
		E.g. when by_type = 'car_code', this function will return a list of car objects by
		searching the car_object_list and looking for the car code == match_by

		:param car_object_list: input car object list to search on
		:param by_type: can only be one from ['car_code', 'car_type','licence_type']
		:param match_by: the key word use to find matched cars. can be a list or a string
		:return: a list of car objects matched by criteria
		"""
		# step 1: ensure the by_type is valid:
		if by_type not in ['car_code', 'car_type', 'licence_type']:
			print('Invalid search by type')
			return

		if by_type == 'car_code':
			if isinstance(match_by,list):
				output_car_object_list = [car for car in car_object_list if car.get_car_code() in(match_by)]
			else:
				output_car_object_list = [car for car in car_object_list if car.found_matching_car(match_by)]

		elif by_type == 'car_type':
			if isinstance(match_by, list):
				output_car_object_list = [car for car in car_object_list if car.get_car_type() in(match_by)]
			else:
				output_car_object_list = [car for car in car_object_list if car.get_car_type() == match_by]

		else:
			if match_by.upper() not in ['L', 'P', 'FULL']:
				print('Invalid license type')
				return
			if match_by.upper() in ['L','FULL']:
				output_car_object_list = [car for car in car_object_list]
			else:
				output_car_object_list = [car for car in car_object_list if car.probationary_licence_prohibited_vehicle() == False]
		return output_car_object_list

	def load_current_stock(self, input_stock_path):
		"""
		To load the current stock from the stock file, and update the carretailer_stock
		:param input_stock_path:
		:return:
		"""
		# step 0: validate input file path:
		if self.validate_file_path('stock.txt',input_stock_path) == False:
			return

		# step 1: use method read_stock_data to get a retailer_stock_dictionary
		retailer_stock_dict = self.read_stock_data(input_stock_path)
		target_retailer_id = self.get_retailer_id()
		retailer_id_in_file = [item[0] for item in list(retailer_stock_dict.keys())]

		# return if the retailer is not there
		if target_retailer_id not in retailer_id_in_file :
			print(f'{target_retailer_id} not in the file')
			print(f'these retailers are in the file: {retailer_id_in_file} ')
			return

		# step 2: find the corresponding key-value pair and extract car code from there:
		all_car_codes = []
		for each_retailer in list(retailer_stock_dict.keys()):
			this_retailer_id = each_retailer[0]
			if this_retailer_id == target_retailer_id:
				for each_car in retailer_stock_dict[each_retailer]:
					all_car_codes.append(each_car[0])

		# step 3: update self.carretailer_stock if there is any difference:

		if (sorted(all_car_codes) != sorted(self.get_carretailer_stock())) and (all_car_codes != []):
			self.set_carretailer_stock(all_car_codes)
			print('current stock loaded.')


	def is_operating(self, cur_hour):
		"""
		to check if current hour is within business hour
		:param cur_hour:
		:return:
		"""

		# Step 0: validate the input cur_hour and also the business hour
		if (isinstance(cur_hour, float) is False) or (float(cur_hour) > 24.0) or (float(cur_hour) < 0.0):
			print(f'This is not valid hour format {cur_hour}')
			print(f'Please enter input between 0.0 - 24.0')
			return False

		if self.get_carretailer_business_hours() is None:
			print(f'This retailer does not have business hour setup')
			return False

		# Step 1:
		this_hour_start = self.get_carretailer_business_hours()[0]
		this_hour_end = self.get_carretailer_business_hours()[1]

		if (float(cur_hour) >= this_hour_start) and (float(cur_hour) <= this_hour_end):
			return True
		else:
			return False

	def get_all_stock(self):
		"""
		This function is to find and return a list of car objects based on current stock car code
		Note. a static variable list car_universe_list is required
		:return: a list of car objects that are currently in retailer's stock
		"""

		self.load_current_stock(CarRetailer.static_stock_file_path)
		stock_car_code_list = self.get_carretailer_stock()

		# step 0: ensure car code list is not Empty:
		if stock_car_code_list is []:
			print('this retailer does not have car stock setup')
			return

		# step 1: get the list of car codes of current stock:
		stock_car_code_list = self.get_carretailer_stock()

		# step 2: return the list of car objects based on the car code:
		output_car_object_list = self.search_car_objects(Car.car_object_universe_list,'car_code',stock_car_code_list)

		return output_car_object_list

	def get_stock_by_car_type(self,input_car_types):
		"""
		This function is to find and return a list of car objects that match the input car type
		:param input_car_types: a string or a list. muse be in ['FWD', 'AWD', 'RWD']
		:return: a list of car objects that match the input car type
		"""

		# tidy up string input to list input:
		if isinstance(input_car_types, str):
			input_car_types = [input_car_types]

		# ensure input car type valid
		for each_type in input_car_types:
			if each_type.upper() not in ['FWD', 'AWD', 'RWD']:
				print(f'invalid input car type: {each_type}')
				return

		current_all_stock_object = self.get_all_stock()

		matched_stock_by_car_type = self.search_car_objects(current_all_stock_object, 'car_type', input_car_types)

		return matched_stock_by_car_type


	def get_stock_by_licence_type(self,input_licence_type):
		"""
		This function is to find and return a list of car objects that match the input licence type
		:param input_licence_type: a string. muse be in ['L','P','FULL']
		:return: a list of car objects that match the input licence
		"""

		# ensure input car type valid
		for each_type in input_licence_type:
			if each_type.upper() not in ['L', 'P', 'FULL']:
				print(f'invalid input licence type: {each_type}')
				return

		current_all_stock_object = self.get_all_stock()

		matched_stock_by_licence_type = self.search_car_objects(current_all_stock_object, 'licence_type', input_licence_type)

		return matched_stock_by_licence_type

	def car_recommendation(self):
		"""
		This function is to randomly select a car that is currently in stock and return it
		:return: a car object
		"""

		# Step 1: get current stock
		current_stock_car_obj_list = self.get_all_stock()

		# Step 2: randomly pick a car:
		if len(current_stock_car_obj_list) > 0:
			picked_car = random.choice(current_stock_car_obj_list)
			return picked_car
		else:
			print('No car in stock')
			return


	def get_postcode_distance(self, input_postcode):
		"""
		return the absolute difference to the input postcode

		:param input_postcode:
		:return:
		"""
		# Step 0: validate input postcode:
		try:
			cleaned_input_postcode = int(input_postcode)
		except (ValueError,TypeError) as e:
			print(f'{e}: input postcode invalid {input_postcode}')
			return

		else:
			this_address = self.get_carretailer_address()
			if this_address is None:
				print('The retailer does not have address specified')
				return

			this_address_list = this_address.split(',')
			this_post_str = this_address_list[len(this_address_list) - 1]
			this_postcode = this_post_str[len(this_post_str) - 4:len(this_post_str)]

			try:
				this_postcode_int = int(this_postcode)
			except (ValueError,TypeError) as e:
				print(f'{e}: input postcode invalid {this_address}')
				return

			else:
				this_abs_diff = abs(this_postcode_int - cleaned_input_postcode)
				return this_abs_diff


	def remove_from_stock(self,input_car_code):
		"""
		This function is to remove a car with input car code from stock
		:param input_car_code:
		:return: Boolean value: True -- remove successful; False - Not removed
		"""
		if input_car_code not in self.get_carretailer_stock():
			print(f'Car with {input_car_code} not in stock')
			return False

		updated_car_code_stock = [i for i in self.get_carretailer_stock() if i != input_car_code]


		# Step 1: update the carretailer_stock
		self.set_carretailer_stock(updated_car_code_stock)
		# Step 2: update the stock file:
		if_file_updated = self.update_stock_file(CarRetailer.static_stock_file_path)
		if if_file_updated is True:
			return True
		else:
			return False

	def add_from_stock(self, input_car_code):
		"""
		This function is to add a car with input car code from stock
		Note. a static variable list car_universe_list will be used
		:param input_car_code:
		:return: Boolean value: True -- addition successful; False - Not added
		"""
		car_code_universe = [car.car_code for car in Car.car_object_universe_list]

		# case 1: car code already in stock
		if input_car_code in self.get_carretailer_stock():
			print(f'Car with {input_car_code} already in stock')
			return False

		# case 2: car code does not exist at all
		elif input_car_code not in car_code_universe:
			print(f'Car with {input_car_code} does not exist')
			return False

		else:
			updated_car_code_stock = [i for i in self.get_carretailer_stock()]
			updated_car_code_stock.append(input_car_code)


			# Step 1: update the carretailer_stock
			self.set_carretailer_stock(updated_car_code_stock)
			# Step 2: update the stock file:
			if_updated = self.update_stock_file(CarRetailer.static_stock_file_path)
			if if_updated is True:
				return True
			else:
				return False

	def create_order(self, input_car_code):
		"""
		To create an order for the input car code:
		-- An order object should be returned
		-- stock.txt should be modified accordingly
		-- order.txt should be modified

		:param input_car_code: the car code that this order relates to
		:return: An order object
		"""
		current_stock_car_code = self.get_carretailer_stock()
		car_code_universe = [this_car.get_car_code() for this_car in Car.car_object_universe_list]

		# Step 0: sanity check on input car code:
		if input_car_code not in current_stock_car_code:
			print(f'Car {input_car_code} not in the retailer"s stock.')
			return
		if input_car_code not in car_code_universe:
			print(f'Car {input_car_code} does not exists.')
			return

		# Step 1: create order
		this_car = [this_car for this_car in Car.car_object_universe_list if this_car.get_car_code() == input_car_code][0]

		this_order = Order()
		this_order.set_order_car(this_car)
		this_order.set_order_creation_time()
		this_order.set_order_id()
		this_order.set_order_retailer(self)
		print('Order Created')
		print(this_order)

		# Step 2: remove relevant stock:
		self.remove_from_stock(input_car_code)

		# Step 3: update order file
		self.update_order_file(this_order, CarRetailer.static_order_file_path)























