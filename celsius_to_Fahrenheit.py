# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of Celsius temperatures
celsius_values = [0, 25, 30, 37, 100]

# Convert using map function
fahrenheit_values = list(map(celsius_to_fahrenheit, celsius_values))

# Display results
print("Celsius:", celsius_values)
print("Fahrenheit:", fahrenheit_values)
