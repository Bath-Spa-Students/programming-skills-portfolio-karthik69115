#Q.4 Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {
    'nile':'Egypt',
    'Yukon River':'United States',
    'Saskatchewan ':'Canada',
    'Koyukuk':'Alaska',
    'amur river':'China',
    }

for river, country in rivers.items():
    print("The "+river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this set of data:")
for river in rivers.keys():
    print("- "+river.title())

print("\nThe following countries are included in this set of data:")
for country in rivers.values():
    print("- "+country.title())