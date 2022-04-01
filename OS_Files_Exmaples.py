We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. The contents_of_file function reads this file into records and returns the information in a nicely formatted block. Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader.

import os
import csv

# Create a file with data in it
def create_file(filename):
with open(filename, "w") as file:
file.write("name,color,type\n")
file.write("carnation,pink,annual\n")
file.write("daffodil,yellow,perennial\n")
file.write("iris,blue,perennial\n")
file.write("poinsettia,red,perennial\n")
file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
return_string = ""

# Call the function to create the file 
create_file(filename)

# Open the file
with open(filename) as f:
# Read the rows of the file into a dictionary
reader = csv.DictReader(f)
# Process each item of the dictionary
for row in reader:
	return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
	return return_string
	
	#Call the function
	print(contents_of_file("flowers.csv")) 
	
	
	2.
	Question 2
	Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. How do you skip over the header record with the field names?



	import os
	import csv
	
	# Create a file with data in it
	def create_file(filename):
	with open(filename, "w") as file:
	file.write("name,color,type\n")
	file.write("carnation,pink,annual\n")
	file.write("daffodil,yellow,perennial\n")
	file.write("iris,blue,perennial\n")
	file.write("poinsettia,red,perennial\n")
	file.write("sunflower,yellow,annual\n")
	
	# Read the file contents and format the information about each row
	def contents_of_file(filename):
	return_string = ""
	# Call the function to create the file 
	create_file(filename)
	
	# Open the file
	with open(filename) as file:
	# Read the rows of the file
	rows = csv.reader(file)
	rows = list(rows)
	# Process each row
	for row in rows:
		name, color, ty = row
		# Format the return string for data rows only
		if row != rows[0]:
			return_string += "a {} {} is {}\n".format(color, name, ty.strip())
			return return_string
			
			#Call the function
			print(contents_of_file("flowers.csv"))#!/usr/bin/env python3
import re
import csv
def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):
    return True
  return False
def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address
def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '<csv_file_location>'
  report_file = '<path_to_home_directory>' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()
