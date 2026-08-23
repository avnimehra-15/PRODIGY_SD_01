#Build a Temperature Convertion Program
print("TEMPERATURE CONVERTER")
temp=float(input("Enter temperature you want to convert "))
print("Select the original unit")
print("1. Celcius")
print("2. Fahrenheit")
print("3. Kelvin")
ch=int(input("Enter your choice from above "))
if ch==1:
    print("Option Selected is 1")
    fahrenheit=(temp*9/5)+32
    kelvin=temp+273.15
    print("Fahrenheit ",fahrenheit)
    print("Kelvin ",kelvin)
elif ch==2:
    print("Option Selected is 2")
    celsius=(temp-32)*5/9
    kelvin=celsius+273.15
    print("Celsius ",celsius)
    print("Kelvin ",kelvin)
elif ch==3:
    print("Option Selected is 3")
    celsius=temp-273.15
    fahrenheit=(celsius*9/5)+32
    print("Celsius:",celsius)
    print("Fahrenheit:",fahrenheit)
else:
    print("Invalid Choice")
