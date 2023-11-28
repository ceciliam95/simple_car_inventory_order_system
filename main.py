# your imports goes here


from car import Car
from car_retailer import CarRetailer
import random
import os
import math
import time

def main_menu():
	"""
	Print out main menu
	:return:
	"""
	print()
	print('Welcome to the Car Purchase Advisor System.\n Please select from the following:')
	print('a.Look for the nearest car retailer')
	print('b.Get car purchase advice')
	print('c.Place a car order')
	print('d.Exit')
	print()

def prompt_list_retailer(input_retailer_list):
	"""
	This function is to list all retailers' information based on the input list
	:param retailer_list: a list of retailers
	:return:
	"""
	if len(input_retailer_list) == 0:
		print('No any retailer in the system!')
		return

	for i in range(0, len(input_retailer_list)):
		converted_char = chr(i + 97)
		print(f'{converted_char}. {str(input_retailer_list[i])}')
	print()

def prompt_option_b_sub_menu():
	"""
	This function is to display the sub-menu for option b
	:param input_retailer: a retailer object
	:return:
	"""
	print()
	print('a. Recommend a car')
	print('b. Get all cars in stock')
	print('c. Get cars in stock by car type. e.g ["AWD","RWD"]')
	print('d. Get probationary licence permitted cars in stock')
	print('e. Back to main menu')
	print()
	return

def prompt_menu_input(input_len):
	"""
	To ask for user input until it is valid

	param input_len: length of valid options
	:return: a validated user_input
	"""
	valid_option_set = [chr(i + 97) for i in range(0,input_len)]

	# ask for user input:
	user_input = input(f'Please select from option {valid_option_set}.')
	check_user_input, validated_user_input = validate_menu_input(user_input, input_len)

	while check_user_input is False:
		user_input = input(f'Please select from option {valid_option_set}.')
		check_user_input, validated_user_input = validate_menu_input(user_input, input_len)

	return validated_user_input



def validate_menu_input(user_input, input_len):
	"""
	To validate the user input  for main menu

	param input_len: length of valid options
	:return: True - valid. False - invalid
	"""
	valid_option_set = [chr(i + 97) for i in range(0,input_len)]

	# convert into ideal format:
	invalid_message = f'user input {user_input} not valid. Please enter {valid_option_set} '

	user_input = user_input.replace("'","")
	if user_input.isdigit():
		try:
			converted_user_input = chr(int(user_input) + 96)
		except:
			print(invalid_message)
			return (False,user_input)
	elif user_input.isalpha():
		converted_user_input = user_input.lower()
	else:
		print(invalid_message)
		return (False,user_input)

	if converted_user_input in valid_option_set:
		confirm_message = f'option {converted_user_input} is selected.\n'
		print(confirm_message)
		return (True,converted_user_input)
	else:
		print(invalid_message)
		return (False,user_input)

def validate_user_input_option_a(user_input):
	"""
	To validate the user input  for option a - postcode
	:return: True - valid. False - invalid
	"""
	if  user_input.isdigit() is False:
		print(f'Invalid user input postcode {user_input}')
		return (False, user_input)

	if int(user_input) < 800 or int(user_input) > 7999:
		print(f'postcode {user_input} is not a valid Australian postcode (800 - 7999)')
		return (False, user_input)

	cleaned_user_input = int(user_input)
	return (True, cleaned_user_input)

def validate_option_b_car_type(user_input):
	"""
	To validate the input for option b sub-menu car type.
	Valid inputs: list that contains ['AWD','RWD','FWD']
	:param user_input:
	:return:
	"""
	if '[' not in user_input:
		user_input = '[' + user_input + ']'

	cleaned_user_input_0 = user_input[1:len(user_input)-1].replace("'","")

	cleaned_user_input_1 = cleaned_user_input_0.split(',')

	for item in cleaned_user_input_1:
		if item.upper() not in ['AWD','RWD','FWD']:
			print(f"invalid user input {user_input}. \nPlease enter a list from ['AWD','RWD','FWD]")
			return (False, user_input)
		else:
			cleaned_user_input_2 = [item.upper() for item in cleaned_user_input_1]
			return (True, cleaned_user_input_2)

def validate_place_order_input(user_input):
	"""
	To validate the user input for placing an order:
	- Retailer ID and Car ID are separated by a space
	- Retailer ID and Car ID exists
	- The Car is currently in stock

	:param user_input:
	:return: True/False, and validated user input: a tuple of Retailer instance and Car instance
	"""
	try:
		user_input_list = user_input.replace(',',' ').split(' ')
		retailer_id = user_input_list[0].replace('(','').replace('[','').replace("'",'').upper()
		car_id = user_input_list[1].replace(')','').replace(']','').replace("'",'').upper()
	except:
		print(f'Invalid input {user_input}. Please separate retailer and car by a space')
		return (False, user_input)
	else:
		retailer_id_list = [retailer.get_retailer_id() for retailer in CarRetailer.retailer_object_universe_list]
		if retailer_id not in retailer_id_list:
			print(f'Retailer {retailer_id} does not exists')
			return (False, user_input)
		else:
			target_retailer = None
			for each_retailer in CarRetailer.retailer_object_universe_list:
				if each_retailer.get_retailer_id() == retailer_id:
					target_retailer = each_retailer

			if car_id not in target_retailer.get_carretailer_stock():
				print(f'Invalid car id: {car_id} not in Retailer {retailer_id} stock')
				return (False, user_input)
			else:
				target_car = None
				for each_car in Car.car_object_universe_list:
					if each_car.get_car_code() == car_id:
						target_car = each_car

				validated_user_input = [target_retailer, target_car]
				return (True, validated_user_input)

def print_retailer_car_details(input_retailer, input_car_list):
	"""
	This function is to print well-formatted retailer car details
	:param input_retailer: a retailer object
	:param input_car_list: a corresponding car list
	:return:
	"""
	this_retailer_id = input_retailer.get_retailer_id()
	this_retailer_name = input_retailer.get_retailer_name()
	print('\nRetailer Information:')
	print(f'Retailer ID: {this_retailer_id}')
	print(f'Retailer Name: {this_retailer_name}')

	# print car information:
	print('\nStock information:')
	if len(input_car_list) == 0:
		print('No matched cars found!')
		return

	for each_car in input_car_list:
		this_car_id = each_car.get_car_code()
		this_car_name = each_car.get_car_name()
		this_car_type = each_car.get_car_type()
		this_car_capacity = each_car.get_car_capacity()
		this_car_horsepower = each_car.get_car_horsepower()
		this_car_weight = each_car.get_car_weight()
		this_car_probationary = each_car.probationary_licence_prohibited_vehicle()
		this_car_probation_ratio = math.ceil((this_car_horsepower / this_car_weight) * 1000)

		print(f'Car Code: {this_car_id}')
		print(f'Car Name: {this_car_name}')
		print(f'Car Type: {this_car_type}')
		print(f'Car Capacity: {this_car_capacity}')
		print(f'Car Horsepower: {this_car_horsepower}')
		print(f'Car Weight: {this_car_weight}')
		print(f'Car Power Mass ratio {this_car_probation_ratio}')
		print(f'If is probationary licence prohibited vehicle: {this_car_probationary}')
		print()

def print_retailer_info(input_retailer):
	"""
	To display the retailer details without showing the current stock
	:param input_retalier: a CarRetailer object
	:return:
	"""
	this_retailer_id = input_retailer.get_retailer_id()
	this_retailer_name = input_retailer.get_retailer_name()
	this_retailer_address = input_retailer.get_carretailer_address()

	print('\nRetailer Information:')
	print(f'Retailer ID: {this_retailer_id}')
	print(f'Retailer Name: {this_retailer_name}')
	print(f'Retailer Address: {this_retailer_address}')
	print()

def create_car_retailer_universe():
	"""
	This function is to create 3 car retailers, and all their info will be randomly generated
	The output will be a list of car_retailers
	This is the only place where CarRetailer objects can be created

	:return:
	"""
	for i in range(0,5):
		this_car_retailer = CarRetailer()

		# set the retailer's information (randomly generate):
		this_car_retailer.set_retailer_id()
		this_car_retailer.set_retailer_name()
		this_car_retailer.set_carretailer_address()
		this_car_retailer.set_carretailer_business_hours()


	return

def create_car_universe():
	"""
	This function is to create 12 cars, and all their info will be randomly generated
	The output will be a list of cars
	This is the only place where Car objects can be created

	:return:
	"""
	this_car_list = []
	for i in range(0,30):
		this_car = Car()

		# set the car's information (randomly generate):
		this_car.set_car_code()
		this_car.set_car_name()
		this_car.set_car_capacity()
		this_car.set_car_horsepower()
		this_car.set_car_weight()
		this_car.set_car_type()

	return


def assign_cars_to_retailer():
	"""
	This function is to assign created cars to crated retailers as their starting-point stock.
	:return: a dictionary, the key is the retailer and values are car list
	"""
	input_retailer_list = CarRetailer.retailer_object_universe_list
	input_car_list = Car.car_object_universe_list


	no_retailers = len(input_retailer_list)
	no_cars = len(input_car_list)

	# average #cars each retailer can get:
	avg_cars_per_retailer = int(no_cars/no_retailers)

	this_car_list = input_car_list[:]
	this_retailer_list = input_retailer_list[:]

	# initialise the dictionary to store the assignment:
	this_assignment_dict = {retailer: [] for retailer in this_retailer_list}

	for each_retailer in this_retailer_list:
		assigned_cars = random.sample(this_car_list, avg_cars_per_retailer)
		this_assignment_dict[each_retailer] = assigned_cars

		# remove the assigned cars:
		for each_car in assigned_cars:
			this_car_list.remove(each_car)

	# will update the current_stock attribute for each retailer:
	for each_retailer in this_retailer_list:
		this_assigned_cars = this_assignment_dict[each_retailer]
		car_code_list = [each_car.get_car_code() for each_car in this_assigned_cars]
		each_retailer.set_carretailer_stock(car_code_list)

	#return the assignment dictionary:
	return this_assignment_dict


def generate_test_data():
	"""
	This function is to generate test data for stock.txt and also order.txt
	:return:
	"""
	stock_file_path = CarRetailer.static_stock_file_path

	# create retailer and car universes, and do the assignment:
	create_car_retailer_universe()
	create_car_universe()
	car_retailer_assignment = assign_cars_to_retailer()

	car_retailer_universe_list = CarRetailer.retailer_object_universe_list


	stock_line = ''
	for each_retailer in car_retailer_universe_list:
		assigned_cars = car_retailer_assignment[each_retailer]
		assigned_car_str = str([str(this_car) for this_car in assigned_cars])
		this_retailer_str = f'{each_retailer.retailer_id}, {each_retailer.retailer_name}, {each_retailer.carretailer_address}, {each_retailer.carretailer_business_hours}'

		this_stock_line = f'{this_retailer_str}, {assigned_car_str} \n'
		stock_line += this_stock_line


	with open(stock_file_path, 'w') as stock_file:
		# Write the text to the file
		stock_file.write(stock_line)
	stock_file.close()

	print('stock txt generated!')

def advise_nearst_retailer(input_postcode):
	retailer_distance_dict = {}
	for each_retailer in CarRetailer.retailer_object_universe_list:
		retailer_distance_dict[each_retailer] = each_retailer.get_postcode_distance(input_postcode)

	nearst_retailer= min(retailer_distance_dict, key=lambda k: retailer_distance_dict[k])

	del retailer_distance_dict[nearst_retailer]
	second_retailer = min(retailer_distance_dict, key=lambda k: retailer_distance_dict[k])

	return (nearst_retailer, second_retailer)


def main():

	# Step 0: Set up file path etc.
	current_dir = os.getcwd()
	output_dir = f'{current_dir}\data'
	stock_file_path = f'{current_dir}\data\/stock.txt'
	order_file_path = f'{current_dir}\data\/order.txt'

	# Ensure the directory is there:
	os.makedirs(output_dir, exist_ok=True)
	CarRetailer.static_stock_file_path = stock_file_path
	CarRetailer.static_order_file_path = order_file_path

	print(f'Stock txt file path: {CarRetailer.static_stock_file_path}')
	print(f'Order txt file path: {CarRetailer.static_order_file_path}')
	print()

	# Function 1: generate test data
	generate_test_data()

	# load data into memory:
	stock_file = open(stock_file_path, 'r')
	stock_data = stock_file.readlines()
	stock_file.close()

	# Store car retailer into a list:
	retailer_list = CarRetailer.retailer_object_universe_list

	# Function 2: bring up the main menu
	while True:
		main_menu()

		# Ask for input:
		validated_user_input = prompt_menu_input(4)

		# Go through options

		# Check for nearest retailer:

		if validated_user_input == 'a':
			user_input_option_a = input('Please enter your Australian postcode (800 - 7999): ')
			check_user_input_a, validated_user_input_a = validate_user_input_option_a(user_input_option_a)
			while check_user_input_a is False:
				user_input_option_a = input('Please enter your Australian postcode (800 - 7999): ')
				check_user_input_a, validated_user_input_a = validate_user_input_option_a(user_input_option_a)

			nearst_retailer = advise_nearst_retailer(validated_user_input_a)
			print(f'Your postcode is {validated_user_input_a}, the nearst retailer is retailer id: {nearst_retailer.get_retailer_id()}')

			print_retailer_info(nearst_retailer)
			print('Back to Main Menu!')
			continue

		elif validated_user_input == 'b':
			# Firstly list all retailers.
			print(f'Retailers in the system are as follows, Please select the retailer: ')
			prompt_list_retailer(retailer_list)

			# Ask for user input:
			validated_user_input_option_b_retailer = prompt_menu_input(len(retailer_list))

			selected_retailer_index = ord(validated_user_input_option_b_retailer) - 97
			selected_retailer = retailer_list[selected_retailer_index]

			# Display the sub menu:
			print(f'Selected retailer {selected_retailer.get_retailer_id()}\n Please select from following options: ')

			# Enter the sub menu
			while True:
				prompt_option_b_sub_menu()
				validated_user_input_option_b_sub_menu = prompt_menu_input(5)

				if validated_user_input_option_b_sub_menu == 'a':
					selected_car = selected_retailer.car_recommendation()
					print('The Recommended car is:')
					print(f'Car Code: {selected_car.get_car_code()}')
					print(f'Car Name: {selected_car.get_car_name()}')
					print(f'Car Type: {selected_car.get_car_type()}')
					print(f'Car Capacity: {selected_car.get_car_capacity()}')
					print(f'Car Horsepower: {selected_car.get_car_horsepower()}')
					print(f'Car Weight: {selected_car.get_car_weight()}')
					print()
					print('Return to sub menu!')
					continue

				elif validated_user_input_option_b_sub_menu == 'b':

					print('Getting all cars in stock:')
					this_car_list = selected_retailer.get_all_stock()
					print_retailer_car_details(selected_retailer, this_car_list)
					print('Return to sub menu!')
					continue

				elif validated_user_input_option_b_sub_menu == 'c':
					# Ask for input
					user_input_option_b_car_type = input("Please enter the car type (e.g. ['AWD','RWD']")
					check_option_b_car_type, validated_user_input_car_type = validate_option_b_car_type(user_input_option_b_car_type)

					while check_option_b_car_type is False:
						user_input_option_b_car_type = input("Please enter the car type (e.g. ['AWD','RWD']")
						check_option_b_car_type, validated_user_input_car_type = validate_option_b_car_type(user_input_option_b_car_type)

					# Find the car by car type
					selected_car_by_type = selected_retailer.get_stock_by_car_type(validated_user_input_car_type)

					# Print the formatted cars:
					print_retailer_car_details(selected_retailer, selected_car_by_type)

					print('Return to sub menu!')
					continue


				elif validated_user_input_option_b_sub_menu == 'd':
					# Print the option and ask for input:
					print('Please select the driver licence type from the following:\n')
					print('a. Learner License (L)')
					print('b. Full License (Full)')
					print('c. Probationary License (P)')

					option_map = {'a': 'L', 'b': 'FULL', 'c': 'P'}
					validated_user_input_option_b_license = option_map[prompt_menu_input(3)]

					# Get the stock by license type:
					selected_car_by_license = selected_retailer.get_stock_by_licence_type(validated_user_input_option_b_license)

					# Print the formatted ones:
					print_retailer_car_details(selected_retailer, selected_car_by_license)
					print('Return to sub menu!')
					continue

				else:
					# Exit
					break

			print('Back to Main Menu!')
			continue

		# Create Order
		elif validated_user_input == 'c':

			# Step 1 Ask for input Retailer ID and Car ID
			user_input_place_order = input('Please enter the Retailer ID and Car ID, separating by a space: ')
			check_if_user_input_valid, validated_user_input_place_order = validate_place_order_input(user_input_place_order)

			while check_if_user_input_valid is False:
				user_input_place_order = input('Please enter the Retailer ID and Car ID, separating by a space: ')
				check_if_user_input_valid, validated_user_input_place_order = validate_place_order_input(user_input_place_order)

			# Check Retailer operating time:

			target_retailer = validated_user_input_place_order[0]
			target_car = validated_user_input_place_order[1]
			current_time = time.localtime()
			# Format the time as a 24-hour clock with one decimal place for seconds
			current_hour = int(current_time.tm_hour)
			current_min = round(float(current_time.tm_min/60),1)
			current_time_converted = current_hour + current_min

			if_operating = target_retailer.is_operating(current_time_converted)

			if if_operating is False:
				print(f'Current time is {current_time.tm_hour}.{current_time.tm_min}')
				print(f'The Retailer {target_retailer.get_retailer_id()} is not operating.')
				print(f'The Retailer is operating during {target_retailer.get_carretailer_business_hours()}')

			else:
				print('The retailer is still operating!')
				target_retailer.create_order(target_car.get_car_code())

			print('Back to Main Menu!')
			continue

		else:
			print('Exit!')
			break



if __name__ == "__main__":
	main()