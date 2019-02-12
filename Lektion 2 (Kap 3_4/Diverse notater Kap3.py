# Diverse øvelser med List

MinFamilie = ['villy','inger','bjarne','mille-My']
print(MinFamilie)

print(MinFamilie[2])            # Ved at skrive flg, printer den det overstående nr i listen, 0 skal altid tælles med
print(MinFamilie[0].title())
print(MinFamilie[-1].title())   # Hvis der skrives -1, tages den sidste i listen

knallerter = ['sachs','yamaha','puch','kreidler']
print(knallerter)
knallerter[2] = 'vespa'     # En position i en liste kan overskrives på følgende måde
print(knallerter)

knallerter.append('suzuki')     # For at tilføje til sidst i en liste, bruges append på en eksiterende liste
print(knallerter)

frugter = []

frugter.append('Æble')          # Append er for at tilføje til en liste
frugter.append('Pære')
frugter.append('banan')
print(frugter)
frugter.insert(2, 'Appelsin')   # Insert er for at indsætte noget på en specifik plads i liste, en position + variabel data
print(frugter)

del frugter[0]                  # Del kan bruges til at slette noget på en specifik position i en liste
print(frugter)

MorrisDele = ['baghjul','rat','forskærm','nøgler','motorhjelm']
print(MorrisDele)
EnDelMorris = MorrisDele.pop(3)  # Pop kan bruges til at tage en variabel ud af en liste, når det er gjort er den ikke længere tilgængelig i listen
print(EnDelMorris)
print(MorrisDele)

SkuffeIndhold = ['Kniv','Gaffel','Ske']
print(SkuffeIndhold)
SkuffeIndhold.remove('Gaffel')      #Remove gør det muligt at fjerne en variabel, ved dens værdi!
print(SkuffeIndhold)
SpiseSuppe = 'Ske'                  #Du kan også fjerne den ved at benævne den som en anden variabel
SkuffeIndhold.remove(SpiseSuppe)
print(SkuffeIndhold)
print("Jeg spiser suppe med en " + SpiseSuppe)

Biler = ['vw', 'audi','volvo','suzuki','bmw']
print(Biler)
Biler.sort()                        #Sort bruges til at arrangere biler i alfabetisk orden
print(Biler)
Biler.sort(reverse=True)            #reverse=True, så bliver de håndteret baglæns
print(Biler)
print(sorted(Biler))                #sorted kan bruges til at sortere en liste midlertidigt

Tal = ['1','4','3','2','5']         #reverse bruges for at vende rækkefølgen i en liste
Tal.reverse()
print(Tal)
print(len(Tal))