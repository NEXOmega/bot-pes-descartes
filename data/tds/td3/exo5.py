def startswith(text, prefix):
    for i in range(0, len(prefix)):
        if not (text[i] == prefix[i]):
            return False
    return True
print(startswith("Quoi d'neuf Scooby-Doo", "Quoi"))
print(startswith("Nous on te suis partout", "Il"))

def endwith(text, prefix):
    for i in range(1, len(prefix)):
        if not (text[len(text)-i] == prefix[len(prefix)-i]):
            return False
        return True
print(endwith("On va résoudre ce mystère" , "mystère"))
print(endwith("Les indices après tout", "Il"))

def get_verb_group(verb):
    if(endwith(verb, "er")):
        return "Premier groupe"
    elif (endwith(verb, "ir")):
        return "Second Grupe"
    else:
        return "Troisième Groupe"
verbe=input("Donner moi un verbe non conjugué : \n")
print(f"Le verbe {verbe} est du {get_verb_group(verbe)}")
