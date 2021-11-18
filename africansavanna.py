import random
import sys

print("Welcome to the African Savanna")
print("Savanna Version is 1.0")
print("")

atree = int(input("How many Acacia trees are there? "))
print(atree, "Acacia trees")
print("")

btree = int(input("How many Bushwillow trees are there? "))
print(atree, "Bushwillow trees")
print("")

cutgrassbunch = int(input("How many bunches of Cutgrass are there? "))
print(cutgrassbunch, "Bunches of Cutgrass")
print("")

giraffe = int(input("How many Giraffes are there? (Remember that they only eat Acacia tree leaves) "))
print(giraffe, "Giraffes")
print("")

zebra = int(input("How many Zebras are there? (Remember that they only eat Grasses) "))
print(zebra, "Zebras")
print("")

lion = int(input("How many Lions are there? "))
print(lion, "Lions")
print("")

days = 0
prog = input("Ready to play (y/n): ")

while prog == "y":
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  print("")
  
  days = days + 1

  print("It is day", days)
  print("")
  print("")
  
  if cutgrassbunch > 100:
    print("Grass Fire! some of the cutgrass has caught fire!")
    plantburn = int(random.randint(1, 100))
    cutgrassbunch = cutgrassbunch - plantburn
    atree = atree - plantburn
    print(plantburn, "Of every plant has burnt to ashes")
    print("")

  growcutgrass = int(random.randint(1, 10))  
  growatree = int(random.randint(1, 10))

  if growatree > 5:
    growatreeamount = random.randint(10, 100)
    atree = atree + growatreeamount
    print(growatreeamount, "Acacia Trees have grown")
    print("")
    
  else:
    growatreeamount = random.randint(1, 10)
    atree = atree + growatreeamount
    print(growatreeamount, "Acacia Trees have grown")
    print("")

  if growcutgrass > 5:
    growcutgrassamount = int(random.randint(1, 10))
    cutgrassbunch = cutgrassbunch + growcutgrassamount
    print(growcutgrassamount, "Cutgrass Bunches have grown")
    print("")


  if giraffe > 0:
    atree = atree - giraffe
  if atree < 0:
    atree = 0
  if giraffe > 2:
      makegiraffe = random.randint(1, 2)
      print(makegiraffe, "Giraffes have been born")
      print("")
  if giraffe > atree:
     giraffe = giraffe - 1

  if zebra > 0:
    cutgrassbunch = cutgrassbunch - zebra

  giraffe = giraffe - lion
  if giraffe < 0:
    giraffe = 0
  if giraffe < lion:
    lion = lion - random.randint(1, 5)
  if giraffe > lion:
    makelion = random.randint(1, 5)
    lion = lion + makelion
    print(makelion, "Lions have been born")
    print("")
  


  points = atree + btree + giraffe + lion

  liveanimals = lion + giraffe
    

  print("There are", atree, "Acacia trees left")
  print("There are", cutgrassbunch, "Cutgrass bunches left")
  print("There are", giraffe, "Giraffes left")
  print("There are", lion, "Lions left")
  print("")
  print("You have", points, "points")
  print("")

  if liveanimals < 0:
    print("Oh No! all your animals died! Game Over.")
    sys.exit
    

  prog = input("Ready to continue? (y/n): ")
  
