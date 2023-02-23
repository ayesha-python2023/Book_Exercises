print("Enter your temperature reading in Celsius")
answer = int(input())

#next there is a need to add a formula for the temperature conversion

readingFahrenheit = answer * (9/5) + 32
stringAnswer = str(readingFahrenheit)
print(f"Your entered temperature value in Fahrenheit is {stringAnswer}")
# print(stringAnswer)



#####convert you temperature reading from fahrenheit to celsius

print("Enter your reading in Fahrenheit")
answer = int(input())

#now we need to add a formula for temperature conversion
##

readingCelsius = (answer - 32) * (5/9)

##convert you integer value into string
stringAnswer2 = str(readingCelsius)
print(f"Your temperature reading in Celsius is {stringAnswer2}")
