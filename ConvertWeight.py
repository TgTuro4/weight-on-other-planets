print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = input("Input weight value for conversion: ")
weight = int(weight)
planet = input("Input number of conversion planet: ")
planet = int(planet)
unit = ""

# Write an if statement below:
if planet == 1:
  weight = weight * .91
elif planet == 2:
  weight = weight * .38
elif planet == 3: 
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * .92
elif planet == 6:
  weight = weight * 1.19
else: 
  weight = "You chose a number that doesn't exist within my knowledge."

if weight <= 1:
  unit = "lb"
elif weight < 0:
  print("You cannot input a negative weight")
  exit()
else:
  unit = "lbs"
print("Your weight will be " + str(weight) + str(unit))
