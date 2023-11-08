# Define the cost of a USB stick as 'usb_price' and the amount of money the person has in pounds as 'pound'.
usb_price = 6
pound = 50
# Calculate the maximum number of USB sticks the person can buy by dividing the amount of money by the price per USB stick.
shecanget = pound // usb_price
# Calculate the amount of change the person will receive after buying the USB sticks.
p_change = pound - shecanget * usb_price
# Print the number of USB sticks the person can buy and the amount of change she will receive.
print("sticks she can buy:", shecanget)
print("The amount she will get back:", p_change)
