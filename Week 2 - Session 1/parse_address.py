## Given an address
test_1 = "123 Main St., City Anystate USA 12345"
test_2 = "456 Commerce St., Colorado USA 54321"


# Print the street number and name on one line
# the city and state on the next line
# and the zip on the last line
"""
123 Main St. 
Anystate, USA
12345
"""  
# by the way this is called a "multiline string"

"""
Separate out the street address from the rest of the address
Print the street address
Separate out the state 
Separate out the country
Print the state and country with a comma in between
Separate out the zipcode
Print the zipcode
"""


def parse_address(address):
  address_parts  = address.split(", ")
  street_address = address_parts.pop(0)
  print(street_address)
  remaining_address = address_parts.pop()
  address_parts = remaining_address.split(" ")
  zipcode = address_parts.pop()

  middle_line = ", ".join(address_parts)
  print(middle_line)

  print(zipcode)




parse_address(test_1)