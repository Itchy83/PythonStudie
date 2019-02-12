
StudyBuddies = ['Christian', 'Anel', 'Allan']
for buddi in StudyBuddies:
    print(buddi)

StudyBuddies = ['Christian', 'Anel', 'Allan']
print('\n')
for buddi in StudyBuddies:
    print('\nNavn:')
    print(buddi.title() + ' er på aftenskole i Python')
print('\nVi ses på onsdag Boys!')

for Value in range(1, 5):        # Der defineres value direkte i loopet, range er for at lave en talrække
    print(Value)

Numre = list(range(1, 6))
print(Numre)

UnderVandet = list(range(10, 100+1, 10))        # List og range kan også bruges til at generere
print(UnderVandet)                              # en talrække fra, i det her eksempel 10-100, 10 tabellen

IAnden = []
for Tal in range(1, 6,):                        # ** bruger til at opløfte noget i anden potens
    IAnden.append(Tal**2)                       # Her er lavet et loop som tager tal fra 1-5 og sætter dem i anden
print(IAnden)                                   # hvorefter at ligge dem i listen i anden

FlereTal = list(range(0, 80+1, 4))
print(FlereTal)

print(min(FlereTal))                            # min bruges til at finde det mindste tal
print(max(FlereTal))                            # max bruges til at finde det største tal
print(sum(FlereTal))                            # sum bruges til at finde summen af tallene

IAnden = []
for Tal in range(1, 6,):        # Det her udtryk kan skrives simplere
    IAnden.append(Tal**2)
print(IAnden)

IAndenVer2 = [TalVer2**2 for TalVer2 in range(1, 11)]   # Overstående udtryk skrevet simplere
print(IAndenVer2)

Spillere = ['Finn', 'Henrik', 'Christian', 'Lars', 'Jeppe'] # Slicing kan bruges hvis man skal bruge et udsnit af en list
print(Spillere[3:5])    # Slicing fra 3 til 5
print(Spillere[:3])     # Undlades det første slice ciffer, slices der fra starten af listen
print(Spillere[3:])     # Undlades det sidste ciffer, slices der fra slutningen af listen
print(Spillere[-3:])    # De sidste 3 printes, da der printes fra -3 til slut
print(Spillere[:-3])    # De første 2 printes, da der printes fra start og hen til -3

print('\nHer er dem som er tilbage på Eltronic!\n')
for Spiller in Spillere[-4:]:       # Her bruges slice i et loop
    print(Spiller.title())

JbsMad = ['Æble', 'Pære', 'Banan']
AljMad = JbsMad                 # I det her tilfælde, kigger de variabler på den samme liste og vil altid være det samme
AljMad.append('Drue')
print(JbsMad)
print(AljMad)

JbsMad = ['Æble', 'Pære', 'Banan']
AljMad[:] = JbsMad      # I det her tilfælde, laves den ene list som slice af den anden og er derfor en selvstændig list
AljMad.append('Drue')
print(JbsMad)
print(AljMad)

