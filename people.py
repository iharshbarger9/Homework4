'I consulted the official python 3.6.4 documentation'
import random as r
from datetime import datetime as dt

def make_ssn():
	'''Creates and returns a fake Social Security Number Ex: 123-45-6789'''
	ssn = ''
	for x in range(9):
		if x in [3, 5]:
			ssn += '-'
		ssn += str(r.randint(0, 9))
	return ssn

def make_routingNumber():
	'''Creates and returns a fake routing number Ex: 123456789'''
	routing_number = ''
	for n in range(9):
		routing_number += str(r.randint(0, 9))
	return routing_number

class person():
	customer_list = [] 		# Every instance of customer will be added to this list
	past_customer_list = []

	def __init__(self):
		print('\n\n\n Welcome to I.L.L & Sons Bank!\n')

		self.employee_permissions = False
		self.manager_permissions = False
		self.advisor_permissions = False

		print("\nLet's set up the profile.")

		'''Have user input person's name and check for valid entries'''
		self.first_name = input('\nFirst name: ')
		while len(self.first_name) == 0 or not self.first_name.isalpha():		
			self.first_name = input('Enter a valid first name: ')

		self.middle_name = input('\nMiddle name (Press enter if unavailable): ')
		while len(self.middle_name) != 0 and not self.middle_name.isalpha():
			self.middle_name = input('Enter a valid middle name, if available: ')

		self.last_name = input('\nLast name: ')
		while len(self.last_name) == 0 or not self.last_name.isalpha():
			self.last_name = input('Enter a valid last name: ')

		self.name = '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)

		'''Have user input person's birthdate'''
		birthdate = input('\nDate of birth: mm/dd/YYYY: ')

		'''Verify correct birthday format'''
		valid_birthdate = False
		while not valid_birthdate:
			try:
				self.birthdate = dt.strptime(birthdate, '%m/%d/%Y').date()
				valid_birthdate = True
			except:
				 birthdate = input('\nEnter a valid birthdate. mm/dd/YYYY: ')

		'''Calculate age'''
		self.age = dt.today().year - self.birthdate.year
		if self.birthdate.month > dt.today().month:
			self.age -= 1
		elif self.birthdate.month == dt.today().month and self.birthdate.day > dt.today().day:
			self.age -= 1

		'''Have user input person's address and check for valid entries'''
		self.street_address = input('\nStreet address (Ex: 3 South Market St.): ')
		while not len(self.street_address.split(' ')) >= 2 or not self.street_address.split(' ')[0].isdigit():
			self.street_address = input('Enter a valid street address: ')

		self.city = input('\nCity: ')
		while not len(self.city) >= 2:
			self.city = input('Enter the city: ')

		self.state = input('\nState (Ex: PA): ').upper()
		while self.state not in ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']:
			self.state = input('\nEnter a valid US state abbreviation: ').upper()

		self.zip_code = input('\nZip Code: ')
		while len(self.zip_code) != 5:
			self.zip_code = input('\nEnter a 5-digit zip code: ')

		self.address = '{} {}, {} {}'.format(self.street_address, self.city, self.state, self.zip_code)

		'''Create a fake Social Security number for the person'''
		self.__ssn = make_ssn()
		print('\nSSN is on file.')

class customer(person):
	customer_number = 0
	acct_number_addition = 1234567

	def __init__(self):
		person.__init__(self)
		self.account_number = customer.customer_number + customer.acct_number_addition
		self.routing_number = make_routingNumber()
		self.balance = 0
		self.customer_number = customer.customer_number
		self.investment_acct_balance = 0
		self.outstanding_balance = 0
		customer.customer_number += 1
		customer.acct_number_addition += r.randint(10, 50)
		person.customer_list.append(self)
		
		print('\nBank account has been opened for {}.'.format(self.name))

		self.__pin = input('\nSet a 4-digit pin: ')
		while len(self.__pin) != 4 or not self.__pin.isnumeric():
			self.__pin = input('\nPlease enter a 4-digit pin: ')

		deposit = input('\nWhat is the initial deposit?: $')
	
		while not deposit.isnumeric() or not float(deposit) > 0:
			deposit = input('\nEnter a valid amount to deposit: $')

		self.balance += float(deposit)

		print('\nDone.\n')

	def __str__(self):
		return 'Customer: {}\nD.O.B: {}/{}/{}\nAddress: {}\nAccount Number: {}\nRoutingNumber: {}\nBalance: {}'.format(self.name, self.birthdate.month, self.birthdate.day, self.birthdate.year, self.address, str(self.account_number).zfill(12), self.routing_number, self.balance)

	def __deposit(self):
		done = False
		deposit = input('\nAmount to deposit: $')
		while not done:	
			if not deposit.isnumeric():
				deposit = input('\nEnter a valid amount to deposit: $')
			elif float(deposit) < 0:
				deposit = input('\nEnter a positive amount to deposit: $')
			else:
				self.balance += float(deposit)
				done = True

		print('\nDone.\n')
		print('\nNew balance: $%.2f' % self.balance)

	def __withdrawal(self):
		done = False
		amount = input('\nAmount to withdraw: $')
		while not done:	
			if not amount.isnumeric():
				amount = input('\nEnter a valid amount to withdraw: $')
			elif not float(amount) > 0:
				amount = input('\nEnter a positive amount to withdraw: $')
			elif not float(amount) <= self.balance:
				amount = input('\nAmount exceeds balance. Enter a valid amount to withdraw: $')
			else:
				self.balance -= float(amount)
				done = True

		print('\nDone.\n')
		print('\nNew balance: $%.2f' % self.balance)	

	def __check_balance(self):
		print('Balance: $%.2f' % self.balance)

	def check_outstanding_balance(self):
		print('Outstanding: ${}'.format(self.outstanding_balance))


	def atm(self):
		pin = input('\nEnter your pin: ')
		incorrect_attempts = 0
		access_granted = False
		while not access_granted and incorrect_attempts <= 3:
			if pin == self.__pin:
				access_granted = True
			else:
				incorrect_attempts += 1
				pin = input('\nTry again: ')

		if not access_granted:
			print('\nToo many failed attempts.')


		if access_granted:
			print('\n\n     Welcome to I.L.L & Sons Bank!     \n\n      Thank you for choosing us!')
			print('\n\n       How may we help you?\n')

		done = False
		while not done and access_granted:
			choice = input('\nEnter (1):      Balance Inquiry  \n\nEnter (2):      Deposit  \n\nEnter (3):      Withdrawal  \n\nEnter (4):      Exit\n\nEntry: ')
			if choice == '1':
				self.__check_balance()
				y_n = input('\nWould you like another transaction? (yes/no): ')
				if y_n.lower() in ['yes', 'y']:
					continue
				else:
					done = True
			elif choice == '2':
				self.__deposit()
				y_n = input('\nWould you like another transaction? (yes/no): ')
				if y_n.lower() in ['yes', 'y']:
					continue
				else:
					done = True
			elif choice == '3':
				y_n = input('\nThere will be a $3 surcharge for ATM withdrawals. Accept this fee? (yes/no): ')
				if y_n.lower() in ['yes', 'y']:
					self.balance -= 3
					self.__withdrawal()
				y_n = input('\nWould you like another transaction? (yes/no): ')
				if y_n.lower() in ['yes', 'y']:
					continue
				else:
					done = True
			elif choice == '4':
				done = True
			else:
				choice = input('\nEnter (1):      Balance Inquiry  \n\nEnter (2):      Deposit  \n\nEnter (3):      Withdrawal  \n\nEnter (4):      Exit\n\nEntry: ')


class employee(person):

	def __init(self):
		person.__init__(self)
		self.employee_permissions = True

	def show_customer_info(self, other):
		print( 'Customer: {}\nD.O.B: {}/{}/{}\nAddress: {}\nAccount Number: {}\nRoutingNumber: {}\nBalance: {}'.format(other.name, other.birthdate.month, other.birthdate.day, other.birthdate.year, other.address, str(other.account_number).zfill(12), other.routing_number, other.balance))
			
	def delete_customer(self, other):
		print('\nAction denied. Must be a manager to perform this action.')

	def see_customers(self):
		print('\nNumber of customers: {}'.format(len(person.customer_list)))

class manager(employee):

	def __init__(self):
		employee.__init__(self)
		self.manager_permissions = True

	def show_customer_info(self, other):
		print('Customer: {}\nD.O.B: {}/{}/{}\nAddress: {}\nSocial Security Number: {}\nAccount Number: {}\nRoutingNumber: {}\nBalance: {}'.format(other.name, other.birthdate.month, other.birthdate.day, other.birthdate.year, other.address, other._person__ssn, str(other.account_number).zfill(12), other.routing_number, other.balance))

	def see_customers(self):
		for customer in person.customer_list:
			print('\nName: {}      Acct #: {}'.format(customer.name, str(customer.account_number).zfill(12)))

	def delete_customer(self, other):
		done = False
		while not done:
			y_n = input('\nDelete {}? (yes/no): '.format(other.name))
			if y_n.lower() in ['yes', 'y']:
				print('Deleting...')
				person.past_customer_list.append(person.customer_list.pop(other.customer_number))
				done = True
			elif y_n.lower() in ['no', 'n']:
				print('\nNot deleted.')
				done = True


class advisor(employee):

	def __init__(self):
		employee.__init__(self)
		self.advisor_permissions = True

	def __offer_loan(self, other):
		done1 = False
		amount = input("\n    You've chosen a great lender in I.L.L & Sons. How much would you like to borrow? The least amount you can borrow is $50\n\nAmount: ")

		while not done1:
			try:
				amount = float(amount)
				if amount >= 50:
					done1 = True
				else:
					amount = input('\nHow much would you like to borrow, again? The least amount possible is $50.\n\nAmount: ')
			except:
				amount = input('\nHow much would you like to borrow, again? The least amount possible is $50.\n\nAmount: ')


		period = input('\n    Over how long would you like to pay back the loan?\n    We can offer 1-year, 5-year, or 25-year loans.\n\nNumber of years: ')
		while not period.isnumeric() or period not in ['1', '5', '25']:
			period = input('\nWe can offer 1-year, 5-year, or 25-year loans only.\n\nWhich best suits you?\nNumber of years: ')
		period = int(period)

		interest_rate = 4 + r.randint(10, 70)/100

		accept = input('\n\n{}, we can offer you a {}-year loan of ${} at an interest rate of {}%. Would you like to accept this loan? (yes/no):  '.format(other.first_name, period, format(amount, '.2f'), interest_rate))
		if accept.lower() in ['yes', 'y']:
			other.balance += amount
			other.outstanding_balance += int(format(((1 + interest_rate/ period / 100) ** period) * amount, '.2f'))
			other.check_outstanding_balance()
			print('\n    Each year you will owe {} / {} = ${} on this loan'.format(format(other.outstanding_balance, '.2f'), period, format(other.outstanding_balance/period), '.2f')
		else:
			print('\n    Okay. If you reconsider, please come back and we can talk again.')

	def __open_investment_account(self, other):
		print('Have not yet enabled this function.')

	def give_advice(self, other):
		print('\n    Hello, {}. I am your advisor {} {}'.format(other.first_name, self.first_name, self.last_name))
		entry = input('\n\n     I am here to advise you on your financial options and goals. What would you like to discuss today?\n\nEnter (1) to discuss a loan.\nEnter (2) to open an investment account.\n\nEntry: ')

		done = False
		while not done:
			if entry == '1':
				self.__offer_loan(other)
				y_n = input('\n    Will that be all for today, {}? (yes/no): '.format(other.first_name))
				if y_n.lower() in ['yes', 'y']:
					done = True
				elif y_n.lower() in ['no', 'n']:
					open_invstmnt_acct = input('\n    Okay, so you would like to open an investment account then? (yes/no): ')
					if open_invstmnt_acct.lower() in ['yes', 'y']:
						self.__open_investment_account
						done = True
					else:
						print('\n    Nice seeing you today, {}.'.format(other.first_name))
						done = True
				
			elif entry == '2':
				self.__open_investment_account(other)
				y_n = input('\n    Will that be all for today, {}? (yes/no): '.format(other.first_name))
				if y_n.lower() in ['yes', 'y']:
					done = True
				elif y_n.lower() in ['no', 'n']:
					discuss_loan = input('\n    Okay, so you would like to discuss a loan then? (yes/no): ')
					if discuss_loan.lower() in ['yes', 'y']:
						self.__offer_loan(other)
						done = True
					else:
						print('\n    Nice seeing you today, {}.'.format(other.first_name))
						done = True
				
			else:
				entry = input('\nEnter(1) to discuss a loan.\nEnter (2) to open an investment account.\nEnter (3) to exit.\n\nEntry: ')
				if entry == '3':
					done = True
