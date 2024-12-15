#Viernes Aldion I.

#WEIGHTS
print ("Conversion of Kilogram and Pound:")
print ("  ", "Enter 1 for Kilograms to Pounds")
print ("  ", "Enter 2 for Pounds to Kilograms")
print ("\n")
mass_choice=int(input("Enter number to convert = "))
if(mass_choice==1):
    weight_lbs=int(input("Enter amount of kilograms to convert = "))
    print ("            ")
    weight_kgs=weight_lbs*2.2
    print ("The weight in pounds is = :", weight_kgs )
if(mass_choice==2):
    weight_kgs=int(input("Enter amount of pounds to convert = "))
    print ("             ")
    weight_lbs=weight_kgs/2.2
    print("The weight in kilogram is = :", weight_lbs)
print ("\n")

#DISTANCE
print ("Conversion of miles and km:")
print ("  ", "Enter 3 for mile to km.")
print ("  ", "Enter 4 for km to mile.")
print ("\n")
dist_choice=int(input("Enter number to convert = "))
if(dist_choice==3):
      miles=float(input("Enter amount of miles to convert = "))
      km=miles*.621371
      print("The distance in kilometers is =", km)
if(dist_choice==4):
      km=int(input("Enter the distance to convert = "))
      miles=km/.621371
      print("The distance in miles is =", miles)
print ("\n")

#TEMPERATURE
print ("Temperature conversion:\n")
print ("   ", "Enter 5 for Fahrenheit.")
print ("   ", "Enter 6 for Celsius.")
temp_type=int(input("Enter number to convert"))
if(temp_type==5):
     cTemp=float(input("Enter temperature in Celsius degrees:"))
     fTemp=(cTemp*(9/5)+32)
     print("The temperature in Fahrenheit is=", fTemp)
if(temp_type==6):
     fTemp=float(input("Enter temperature in Fahrenheit:"))
     cTemp=((fTemp-32)*5/9)
     print("The temperature in Celsius is=", cTemp)
print ("\n")
     
#Average of age of the students
student1 = 19
student2 = 20
student3 = 21
student4 = 22
student5 = 18
student6 = 19
student7 = 20
student8 = 21
student9 = 18
student10 = 19

print ("Age of the student1 = 19")
print ("Age of the student2 = 20")
print ("Age of the student3 = 21")
print ("Age of the student4 = 22")
print ("Age of the student5 = 18")
print ("Age of the student6 = 19")
print ("Age of the student7 = 20")
print ("Age of the student8 = 21")
print ("Age of the student9 = 18")
print ("Age of the student10 = 19")
average_age = (student1 + student2 + student3 + student4 + student5 + student6 + student7 + student8 + student9 + student10) / 10
print ("Average age of the students = ", average_age)
print ("\n")
    

#FANTASY STORY

# CHARACTER
shadow_master_name = "Sid Kagenou"
loyal_disciple_name = "Alpha"
rival_adventurer_name = "Diablo"
mysterious_strategist_name = "Christine Hope"
masked_antagonist_name = "Zenon"

# EQUIPMENT AND ITEM
shadow_cloak_name = "Cloak of Umbrage"
illusionary_blade_name = "Excalibs"
shuriken_set_name = "Whispering Shadows Shurikens"
ancient_relic_name = "Shade Stone"
concealed_mask_name = "Veil of Deception"

# ABILITIES
shadow_master_ability = "Atomic"
loyal_disciple_ability = "Compress magic"
rival_adventurer_ability = "Blade Dance of Radiance"
mysterious_strategist_ability = "Strategic Illusion"
masked_antagonist_ability = "Nightfall Eclipse"

# STORY
# inspired by "The Eminence in Shadow"
print ("""
In the clandestine world of shadows, a master known only as {shadow_master_name} rose to eminence. Clad in the mystical {shadow_cloak_name} and wielding the {illusionary_blade_name}, {shadow_master_name} manipulated the threads of darkness with the skill of a true Umbral Master.

His loyal disciple, {loyal_disciple_name}, moved with the grace of the shadows, employing the {loyal_disciple_ability} to remain unseen and unheard. Together, they traversed the realm, leaving behind a trail of mystery and whispers.

However, a formidable rival named {rival_adventurer_name}, with the dazzling {rival_adventurer_ability}, sought to challenge the shadowy dominance. Their clashes resonated like a dance of opposing forces, light against darkness.

In the midst of the unfolding conflict, the mysterious strategist {mysterious_strategist_name}, utilizing the {shuriken_set_name} and her strategic {mysterious_strategist_ability}, joined the intricate game of shadows. Her moves were as unpredictable as the shifting winds, adding a layer of complexity to the unfolding narrative.

Yet, looming in the shadows was the enigmatic masked antagonist known as {masked_antagonist_name}. With the {ancient_relic_name}, a mystical artifact known as the {ancient_relic_name}, and the formidable {masked_antagonist_ability}, Nightfall Eclipse, their true motives remained veiled in darkness.

As the tale of eminence in shadow unfolded, alliances were formed, betrayals were concealed, and the dance between light and darkness reached its zenith. In the end, only the shadows knew the secrets woven into the fabric of the clandestine world, leaving behind a legacy that whispered through the ages.
""")

