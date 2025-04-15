#greetings

name = input("Enter Name: ")
print("Hello "+ name +" !")


# calculator

num1 = input("Enter first num: ")
num2 = input("Enter sec num: ")

num1= int(num1)
num2 =int (num2)
sum = num1+num2
print("Total:", sum)


#celcius to farenhite¸

celcius = input("Enter celcius: ")
celcius = float(celcius)

farenheit = (celcius * 9/5) + 32
print(farenheit)

#principal

principal = input("Enter principal: ")
rate = input("Enter rate of interest: ")
time = input("Enter time(years): ")

principal = float(principal)
rate = float(rate)
time = float(time)

interest = (principal*rate*time)/100
print("Yearly Interest: ",interest)







