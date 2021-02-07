def find_substring(text, query, start):
    for i in range(0, len(text)-start):
        if(text[start+i:start+i+len(query)] == query):
            return i+start
    return -1

#print(find_substring("Conduisent à toi mon chou", "à toi", 5))
#print(find_substring("Conduisent à toi mon chou", "à lui", 0))


def count_substring(text, query):
    start = 0
    count = 0
    while(find_substring(text, query, start) >= 0):
        print( "Start ", start, " ici : ", find_substring(text, query, start), " Count ", count)
        count += 1
        start = find_substring(text, query, start)+1
    return count

print("Occurences : ", count_substring("Quoi d'neuf Scooby-Doo", "oo"))
