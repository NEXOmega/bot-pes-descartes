nbr_notes = int(input("Nombre de notes"))
note = 0
for i in range(0, nbr_notes):
    note += int(input("Note : "))
print(f"Vous avez {note/nbr_notes}")