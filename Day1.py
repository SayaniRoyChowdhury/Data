#############################
#1. Sum of two digits
#############################
x=int (input("Enter two digit"))
n= x[0]
n2= x[1]
s=n+n2
print(s)

############################
#2. BMI Calculator
############################
w=int(input("Enter your weight in kg"))
h=int(input("Enter your height in m"))
bmi= w/(h*h)
print (bmi)
if (bmi<=18.5):
  print("Underweight")
elif (bmi>18.5 && bmi <=25):
  print("Normal Weight")
elif(bmi>25 && bmi<=30):
  print("Overweight")
elif (bmi>30 && bmi<=35):
  print("Obese")
else:
  print("Clinically Obese")

##########################
#3.Life in weeks
#########################
age= int(input("What is your current age?"))
year=90-age
months= year * 12
weeks= year * 52
days= year * 365
print( f" You have {days} days {weeks} weeks, and {month} months left")

