# printer(elements)
# - Accepts a list
# - Prints every element of the list

elements = ["winter","fall", "spring", "summer"]
def printer(elements):
    # Your code here
    for element in elements:
        print(element)

# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
temperatures = [32, 98, 101, 85, 70, 63, 42, 55]
def to_celsius(temperatures):
    # Your code here
    converted = []
    for temp in temperatures: 
        celsius = int((temp - 32) * (5/9))
        converted.append(celsius)
    print(converted)
    return converted



# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
temps = [20, 30, 45, 15, 10, 37, 50]
thresh = 35
def hottest_days(temperatures, threshold):
    # Your code here
    hot_days = []
    for temp in temps:
        if temp > thresh:
            hot_days.append(temp)
        else:
            pass
    print(hot_days)
    return hot_days


    

# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
thresh_in_f = 78
def print_hottest_days(temperatures, threshhold):
    # Your code here
    final = []
    thresh_in_c = int((thresh_in_f - 32) * (5/9))
    new_temps = to_celsius(temperatures)
    hot_days_in_c = hottest_days(new_temps, thresh_in_c)
    for temp in hot_days_in_c:
        if temp > thresh_in_c:
            final.append(temp)
        else:
            pass
    print(final)
    return final # returns a list
            




printer(elements)
to_celsius(temperatures)
hottest_days(temps, thresh)
print_hottest_days(temperatures, thresh_in_f)