A = 2
B = 4
C = 3


print(A)
print(int(B))   #Int foran float, viser dem som Int, men omdifinerer dem ikke
print(C)


print((str(B)+"\n")*10)     #\n i et string felt, skifter linie *10, så sker det ti gange


message = ("Hej med jeg")   #Det er muligt at ændre en variabel til noget andet undervejs i programmet
print(message)
message = ("Hej med dig også")
print(message)

print('Det her er "Nice"')      #Både " og * kan bruges til at definere en string, det gør det muligt at bruge dem i en sætning

name = "allan jensen"           #Strings kan behandles på forskellig vis, .title gør stort forbogstav på navn
print(name.title())
print(name.upper())
print(name.lower())

first_name = "allan"            #To strings ligges sammen
last_name = "jensen"
full_name = first_name + " " + last_name
message = ("Hey, " + full_name.title() + "!!")
print(message)

print("\nMin adresse er:\n\tFælledvej 72\n\t\t8700 Horsens\n\t\t\tDanmark\n")

whitespace = "      Allan      "
print(whitespace)
print(whitespace.rstrip().lstrip())     #For at fjerne overflødigt "whitespace"

Q = 0.2 + 0.1
print(Q)

alder = 23
print("\nIillykke med de " +str(alder) + " år!")

