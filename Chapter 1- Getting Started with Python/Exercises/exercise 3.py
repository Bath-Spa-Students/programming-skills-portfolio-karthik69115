# Import the 'datetime' module to work with date and time information.
import datetime
# Get the current date and time by calling 'datetime.now()' method.
now = datetime.datetime.now()
# Print a header to indicate that we are displaying the current date and time.
print ("Current date and time : ")
# The format specified here will display the date and time in the format "YYYY-MM-DD HH:MM:SS".
print (now.strftime("%Y-%m-%d %H:%M:%S"))
