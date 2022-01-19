def cesar(cle:int,text:str):
    d = {chr(i+65):chr((i+cle) %26+65) for i in range(26)}
    char = " "
    for i in text:
        if i == " ":
            char += " "
        else:
            char += d[i]
    return char

message = "Bonjour, comment allez-vous ?"
cle = "mystère"
def chiffre(key,message):
    c = []
    char = []
    n =len(message)
    m =len(key)
    j = 0
    for i in range(n):
        c.append(ord(message[i])^ord(key[j]))
        j = (j+1)%m
    for i in c:
        char.append(chr(i))
    return char

def dechiffre_C(cle:int,text:str):
    d = {chr(i+65):chr((i+cle) %26+65) for i in range(26)}
    char = " "
    for i in text:
        if i == " ":
            char += " "
        else:
            char += get_key_C(i,cle)
    return char

def get_key_C(val,cle):
    d = {chr(i+65):chr((i+cle) %26+65) for i in range(26)}
    for key, value in d.items():
         if val == value:
             return key
    return None

def dechiffre_X(cle:int, text:str):
    c = []
    cha = " "
    j = 0
    m = len(cle)
    for i in text:
        c.append(ord(i)^ord(cle[j]))
        j = (j+1)%m
    for i in c:
        cha += chr(i)
    return cha

def analyse_text(text:str):
    #Analyse du texte
    d = {}
    n_t = len(text)                         #On défini les variables nécessaires
    lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    d = {chr(65+i) : 0 for i in range(26)}
    for i in text:                          #On parcours la variable qui contient le texte
        d[i] +=1                            #On ajoute actualise le dictionnaire à chaque occurence
    for i in range(26):                     #On parcours le dictionnaire
        d[lettre[i]] /= n_t                 #On divise le nombre d'occurence par la longueur du texte (on obtient un pourcentage/1)
        d[lettre[i]] = round(d[lettre[i]],2)#On arrondis à deux chiffre après la virgule
    
    #Obtention de la clé
    high = 0
    for i,j in d.items():       #On regarde dans le dictionnaire des occurences 
        if high < j:            #On compare les résultat et on obtient le couple avec la plus grande occurence
            high = j
            key = i
    dic = {chr(64+i):i for i in range(1,27)}    #On défini un dictionnaire qui associe  Lettre -> numéro dans l'alphabet
    cle = 5 - dic[key]                          #La clé = 5 (place du e dans l'alphabet) - place de la lettre codé en tant que e dans l'alphabet
    return cesar(cle,text)

diderot ="BWFWKSAKWFIMWDKWFKDWKHZADGKGHZWKGFLKMHHGKWIMWDSESLAWJWWLSALAFVAXXWJWFLWSMEGMNWEWFLWLSMJWHGKUWIMADQSVWTAWFUWJLSAFUWKLIMWLGMKDWKUGJHKYJSNALWFLDWKMFKKMJDWKSMLJWKUWKLIMWLGMLWKDWKHSJLAUMDWKVWKUGJHKYJSNALWFLDWKMFWKKMJDWKSMLJWKUWKLIMWVSFKUWLMFANWJKLGMLWKLWFLJSFKDSLAGFGMAFFAKMGMWFLJSFKDSLAGFWLAFFAKMSDSXGAKUWLLWKMHHGKALAGFVWKHZADGKGHZWKJWKKWETDWHWMLWLJWSUWDDWVWKYWGEWLJWKIMASVEWLLWFLVWKHGAFLKKSFKSMUMFWVAEWFKAGFVWKDAYFWKKSFKDSJYWMJFAHJGXGFVWMJVWKKMJXSUWKKSFKWHSAKKWMJGMHWMLWLJWHSJDWFLADKVMJWHGKJWDSLAXVMFWESKKWSMFWSMLJWLGMLWKLVSFKMFJWHGKJWDSLAXWFMFNSAKKWSMTSLLMHSJDSLWEHWLWJAWFFQWKLWFMFJWHGKSTKGDMHSKEWEWDWKEGDWUMDWKSYJWYSLANWKFAVMNSAKKWSMFAVWKUGJHKIMADJWFXWJEWKADKFWUGFUGANWFLHSKHDMKVWLWFVSFUWSMJWHGKIMSMEGMNWEWFLVSFKMFUGJHKIMWDUGFIMWUWKLIMSHHSJWEEWFLADKJWYSJVWFLDSESLAWJWUGEEWZGEGYWFWUWKLIMADKXGFLSTKLJSULAGFVWLGMLWKDWKIMSDALWKIMADMAKGFLWKKWFLAWDDWKUWKLIMADKDSUGFKAVWJWFLUGEEWAFSDLWJSTDWVSFKDAFKLSFLHJWKIMWAFVANAKATDWVWDWMJKHWUMDSLAGFUWKLIMADKJSAKGFFWFLVMJWHGKJWDSLAXVMFSYJWYSLSMFSMLJWSYJWYSLUWKLIMADKGMTDAWFLIMWLSFVAKIMADKJSAKGFFWFLVWDAFVAXXWJWFUWVMUGJHKSMEGMNWEWFLGMSMJWHGKDWTDGUVWESJTJWLWFVSKSVAKKGDMLAGFUWKLIMADKSFWSFLAKKWFLHSJDSHWFKWWWLDWEGMNWEWFLYWFWJSDIMASFAEWLGMKDWKUGJHKWLDWMJSULAGFHSJLAUMDAWJWVWKMFKKMJDWKSMLJWKIMADWKVWLJMALLGMKUWKLIMWUWLLWAFVAXXWJWFUWIMGAIMWXSMKKWWFWDDWEWEWESAKEGEWFLSFWWFWJWFVJSHSKDWKDGAKVMEGMNWEWFLWJJGFWWK"

print(analyse_text(diderot))