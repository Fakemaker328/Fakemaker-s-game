import random
play = True
happiness = 100
health = 100
number = 1
print("Game Start\n")
print("You are a FBI agent. You caught an agent who works for other country, you need to get nuclear code from him about other countries. You need to tortue him in two weeks to get the nuclear code, but make sure don't let him died. Everyday you can choose an action to do to torture him or make sure he eat and drink something so that he will not died.\n")
while play:
  print("Day",number,"\n")
  print("1.Water torture:Cover the prisoner's face with a cloth and pour water continuously to make him feel like he is drowning.\n")
  print("2.Tiger bench:Tie the prisoner to a bench and gradually raise his legs to cause severe pain.\n")
  print("3.Finger clamping:Use wooden or iron clamps to gradually clamp the prisoner's finger until it hurts or breaks bones.\n")
  print("4.Gallows:Put a rope around the prisoner's neck and gradually tighten it to cause suffocation.\n")
  print("5.Check prisoner's status\n")
  print("6.Give him some food and drink\n")
  print("7.Let him rest a day\n")
  choice = input("Enter 1,2,3,4,5,6,7\n")
  if choice == "1":
    health -= (random.randint(0,10))
    happiness -= (random.randint(0,10))
    print("\nYou choose Water torture.\nThe prisoner choked on the water and then said fuck you\n")
    number += 1
  if choice == "2":
    health -= (random.randint(5,15))
    happiness -= (random.randint(5,15))
    print("\nYou choose Tiger Bench.\nThe prisoner shouted a few times and then said fuck you\n")
    number += 1
  if choice == "3":
    health -= (random.randint(10,20))
    happiness -= (random.randint(10,20))
    print("\nYou choose Finger clamping.\nThe prisoner's hand was swollen and then he said fuck you\n")
    number += 1
  if choice == "4":
    health -= (random.randint(15,25))
    happiness -= (random.randint(15,25))
    print("\nYou choose Gallows.\nThe prisoner was unconscious for a while and then he woke up and said fuck you\n")
    number += 1
  if choice == "5":
    print("\nYou choose to check the prisoner's status.\n")
    print("The prisoner's health is",health,"\n")
    print("The prisoner's happiness is",happiness,"\n")
  if choice == "6":
    health += (random.randint(20,30))
    print("\nYou choose give him some food and drink.\n")
    print("The prisoner had a good meal and then said thank you\n")
    number += 1
  if choice == "7":
    happiness += (random.randint(20,30))
    print("You choose let him rest a day.\n")
    print("The prisoner had a good rest\n")
    number += 1
  if health <= 15 and happiness <= 15:
    if health >= 0 or happiness >= 0:
      play = False
      print("\nThe prisoner couldn't bear the penalty and said the nuclear code.")
    if health <= 0 and happiness <= 0:
      play = False
      print("\nThe prisoner couldn't bear the penalty and died.")
  if health >= 200 or happiness >= 200:
    play = False
    print("\nThe prisoner was touched by you and said the nuclear code.")
  if number > 14:
    play = False
    print("\nThe prisoner didn't said anything and you didn't get the nuclear code, your country was destroyed by his country")