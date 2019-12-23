from turtle import *
import time
t=Turtle()
t.speed(0)
t.hideturtle()
bgcolor("black")

#Define hybrid house colors:
colors_Gryffinpuff=['yellow', 'black', 'red', 'yellow']
colors_Gryffinclaw=['blue', 'red', 'bronze', 'yellow']
colors_Gryfferin=['red', 'green', 'yellow', 'silver']
colors_Huffleclaw=['yellow', 'blue', 'bronze', 'black']
colors_Huffledor=['yellow', 'black', 'red', 'yellow']
colors_Hufferin=['yellow', 'green', 'black', 'silver']
colors_Raverin=['blue', 'green', 'bronze', 'silver']
colors_Raverdor=['blue', 'red', 'bronze', 'yellow']
colors_Raverpuff=['yellow', 'blue', 'bronze', 'black']
colors_Slytherpuff=['yellow', 'green', 'black', 'silver']
colors_Slytherclaw=['blue', 'green', 'bronze', 'silver']
colors_Slytherdor=['red', 'green', 'yellow', 'silver']
bad2 = ["\nHem, hem. This means detention.  It clearly states under educational decree number 91, Students are not allowed to use their own answers and can face expulsion. Be careful.\n", "\nDo it again!\n", "\nAgain!\n"]
bad3 = ["\nWant to live your life as an outcast, do you?\n", "\nBetter do it again...\n", "\nAGAIN, NOW!\n"]
# Start quiz
# Declare our variables. Each will store a number that tracks how any answers the user has given that correspond to a particular house
Gryffindor = 0
Ravenclaw = 0
Slytherin = 0
Hufflepuff = 0
bad = 1
print("*For each question type the letter of your answer.*")
print("\nI've done this job for centuries \nOn every student's head I've sat \nOf thoughts I take inventories \nFor I'm the famous Sorting Hat. \n\nI've sorted high, I've sorted low, \nI've done the job through thick and thin \nSo put me on and you will know \nWhich house you should be in...\n\n ")
while (bad >= 1):
  q1_answer = input("Would you rather be in:\na) The Order of the Phoenix \nb) The Inquisitorial Squad \nc) The Slug Club \nd) S.P.E.W?\n\n")
  if q1_answer == "a":
    Gryffindor += 1
    bad = 0
  elif q1_answer == "b":
    Slytherin += 1
    bad = 0
  elif q1_answer == "c":
    Ravenclaw += 1
    bad = 0
  elif q1_answer == "d":
    Hufflepuff += 1
    bad = 0
  else:
	  if (bad == 1):
		  print(bad2[0])
		  bad = bad + 1
	  elif (bad ==2):
		  print(bad2[1])
		  bad = bad + 1
	  elif (bad>=3):
		  print(bad2[2])
bad = 1
while (bad>=1):
	q2_answer = input("\nThe seeker on your opposing team has just seen the snitch. Do you: \na) Knoch her off her broom and grab the snitch or\nb) Will your broom to go as fast as possible?\n\n")
	if q2_answer == "a":
		Slytherin += 1
		bad = 0
	elif q2_answer == "b":
		Gryffindor+= 1
		bad = 0
	else:
	  if (bad == 1):
		  print(bad3[0])
		  bad = bad + 1
	  elif (bad ==2):
		  print(bad3[1])
		  bad = bad + 1
	  elif (bad>=3):
		  print(bad3[2])
q3_answer = input("\n Chose a hero: \na) Newt Scamander \nb) Albus Dumbledore \nc) Fred Weasley \nd) Luna Lovegood \ne) Severus Snape \nf) Regulus Black\n\n")
if q3_answer == "a":
    Hufflepuff += 1
elif q3_answer == "b":
    Gryffindor += 1
elif q3_answer == "c":
    Gryffindor += 1
elif q3_answer == "d":
    Ravenclaw += 1
elif q3_answer == "e":
    Slytherin += 1
elif q3_answer == "f":
    Slytherin += 1
else:
    print("Well, well, well, lookes like I may be able to give you the old punishment.")
q4_answer = input("\n Choose a Fantastic Beasts creature: \na) Bowtruckle \nb) Niffler \nc) Mooncalf \nd) Occamy \ne) Erumpent \nf) Thestral\n\n")
if q4_answer == "a":
    Hufflepuff += 1
elif q4_answer == "b":
    Ravenclaw += 1
elif q4_answer == "c":
    Hufflepuff += 1
elif q4_answer == "d":
    Gryffindor += 1
elif q4_answer == "e":
    Slytherin += 1
elif q4_answer == "f":
    Ravenclaw += 1
else:
    print("Be carefull, no headmaster to help you now.")
q5_answer = input("\nWhat is your favorite Honeydukes sweet? \na) Chocolate Frogs \nb) Bertie Botts Every Flavor Beans \nc) Acid Pops \nd) Cockroach Clusters \ne) Fizzing Whizbees \nf) Fudge Flies\n\n")
if q5_answer == "a":
    Gryffindor += 1
elif q5_answer == "b":
    Ravenclaw += 1
elif q5_answer == "c":
    Gryffindor += 1
elif q5_answer == "d":
    Slytherin += 1
elif q5_answer == "e":
    Hufflepuff += 1
elif q5_answer == "f":
    Slytherin += 1
else:
    print("I am warning you, one more nonexistent answer and you will be kicked out of the quiz.")
q6_answer = input ("\n Would you rather: \na) Have nothing bad ever happen to the people you love or \nb) Have nothing bad ever happen to you?\n\n")
if q6_answer == "a":
    Gryffindor += 1
elif q6_answer == "b":
    Slytherin += 1
q7_answer = input ("\n Either Hagrid is going to fall of a bridge or Dumbledore is going to be hit by the Avada Kedavra curse. You can only save one of them. Who do you save? \na) Hagrid \nb) Dumbledore\n\n")
if q7_answer == "a":
    Hufflepuff += 1
elif q7_answer == "b":
    Ravenclaw += 1
q8_answer = input ("\n Would you rather have: \na) Enough food to give everyone in the world \nb) The world's knowledge?\n\n")
if q8_answer == "a":
    Hufflepuff += 1
elif q8_answer == "b":
    Ravenclaw += 1
q9_answer = input ("\n Which quote speaks to you? \na) 'I saw someone without a smile so I gave them one of mine' \nb) 'Knowledge is a weapon. I intend to be formidably armed.'\n\n")
if q9_answer == "a":
    Hufflepuff += 1
elif q9_answer == "b":
    Ravenclaw += 1
print("\nYou've now completed the sorting quiz. In which house do you belong? \n\nWill you be Gryffindor, where dwell the brave at heart. Their daring nerve and chivalry set Gryffindors apart. \n\nOr will you be in Hufflepuff, where they are just and loyal. Those patient Hufflepuffs are true and unafraid of toil. \n\nOr do you belong in Ravenclaw? If you've a ready mind, where those of wit and learning will always find their kind. \n\nPerhaps you belong in Slytherin. You'll make your real friends those cunning folks use any means to achieve their ends. \n\nHmmm...Difficult. Very Difficult. \n\nYes,yes that may be the only option. You have been deemed suitable for a hydrid house. \n\n")
if ((Gryffindor > Hufflepuff and Gryffindor > Ravenclaw and Gryffindor > Slytherin) and (Hufflepuff > Ravenclaw or Hufflepuff > Slytherin)):
    print("Must be...Gryffinpuff!!!")
    bg()
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Gryffinpuff[x % 4])
      t.pendown()
      t.write("GRYFFINPUFF!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Gryffindor > Hufflepuff and Gryffindor > Ravenclaw and Gryffindor > Slytherin) and (Ravenclaw > Hufflepuff or Ravenclaw > Slytherin)):
    print("Must be...Gryffinclaw!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Gryffinclaw[x % 4])
      t.pendown()
      t.write("GRYFFINCLAW!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Gryffindor > Hufflepuff and Gryffindor > Ravenclaw and Gryffindor > Slytherin) and (Slytherin > Hufflepuff or Slytherin > Ravenclaw)):
    print("Must be...Gryfferin")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Gryfferin[x % 4])
      t.pendown()
      t.write("GRYFFERIN!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin) and (Ravenclaw > Gryffindor or Ravenclaw > Slytherin)):
    print("Must be...Huffleclaw!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.colors(colors_Huffleclaw[x % 4])
      t.pendown()
      t.write("HUFFLECLAW!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin) and (Gryffindor > Ravenclaw or Gryffindor > Slytherin)):
    print("Must be...Huffledor!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Huffledor[x % 4])
      t.pendown()
      t.write("HUFFLEDOR!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin) and (Slytherin > Ravenclaw or Slytherin > Gryffindor)):
    print("Must be...Hufferin!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Hufferin[x % 4])
      t.pendown()
      t.write("HUFFERIN!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin) and (Slytherin > Hufflepuff or Slytherin > Gryffindor)):
    print("Must be...Raverin!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Raverin[x % 4])
      t.pendown()
      t.write("RAVERINN!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin) and (Gryffindor > Hufflepuff or Gryffindor > Slytherin)):
    print("Must be...Raverdor!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Raverdor[x % 4])
      t.pendown()
      t.write("RAVERDOR!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin) and (Hufflepuff > Slytherin or Hufflepuff > Gryffindor)):
    print("Must be...Raverpuff!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Raverpuff[x % 4])
      t.pendown()
      t.write("RAVERPUFF!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw) and (Hufflepuff > Slytherin or Hufflepuff > Gryffindor)):
    print("Must be...Slytherpuff!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Slytherpuff[x % 4])
      t.pendown()
      t.write("SLYTHERPUFF!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw) and (Ravenclaw > Hufflepuff or Ravenclaw > Gryffindor)):
    print("Must be...Slytherclaw!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Slytherclaw[x % 4])
      t.pendown()
      t.write("SLYTHERCLAW!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
elif ((Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw) and (Gryffindor > Hufflepuff or Gryffindor > Ravenclaw)):
    print("Must be...Slytherdor!!!")
    # Write house name, written 200 times
    for x in range(200):
      t.color(colors_Slytherdor[x % 4])
      t.pendown()
      t.write("SLYTHERDOR!", font = ("Arial", "30", "bold"))
      time.sleep(0.25)
else:
    print("Hmmm...Looks as though you can not be confined to a house, you have everything you need for any of our houses at Hogwarts.")





