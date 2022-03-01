# strings and formatting
s = '      immutable     '
n = s.strip()
S = n.capitalize()

print(s, n, S)

# format options
temperature = 6
desc = 'overcast'
wind_speed = 2.67943 # leave any rounding until the print format - maintains accuracy
x = 'The weather is {0} at {1} degrees with a wind speed of {2:0.2f}'
output = x.format(desc, temperature, wind_speed)
print(output)
