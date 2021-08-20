def crypter_mc(s):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for lettre in s:
        occurence = s.count(lettre)
        pos = 0
        if occurence % 2 == 0:
            pos = occurence//2
        else:
            pos = occurence*2
        ordre = alpha.find(lettre)
        indice = pos+ordre
        if indice > 25:
            indice = indice % 26
        res += alpha[indice]
    return res
 
 
print(crypter_mc("Hello wordl !"))
print("")
fin = input("Fin du cryptage..")