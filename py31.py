solar1=['태양','수성','금성','지구']
solar2=['Sun','Mercury','Venus','Earth']
solardict={}
for i,k in enumerate(solar1):
    val = solar2[i]
    solardict[k]=val
    
print(solardict)