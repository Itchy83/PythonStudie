Forfattere = ['king','lindgren','andersen','reuter','ditlevsen']
Writers = ['king','lindgren','andersen','reuter','ditlevsen']


Kopi = Forfattere
Kopi.append('Dostojevski')
print(Kopi)
print(Forfattere)


WritersVer2 = Writers[0:-1]
WritersVer2.append('Dostojevski')
print(WritersVer2)
print(Writers)

#Observation: Det sidst tilføjede navn mangler, ved brug af = er de to udtryk altid lig hinanden
#Ved hjælp af slice går udtrykket kun den ene vej.


