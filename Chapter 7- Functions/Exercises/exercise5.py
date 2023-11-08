# Define a function called 'describe_city' that takes two parameters: 'city' and 'country'.
# The 'country' parameter has a default value of 'India'.
def describe_city(city, country='India'):
    msg=city.title()+" is in "+country.title()+"."
    print(msg)
describe_city('Mumbai')
describe_city('Kerala')
describe_city('Delhi')
