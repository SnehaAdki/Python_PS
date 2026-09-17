def old_mcdonals(name):
    first_letter = name[0].upper()
    inbetween = name[1:3]
    fourth_letter = name[3].upper()
    remaining_letter = name[4:]
    print(first_letter+inbetween+fourth_letter+remaining_letter)

    first_hald = name[0:3]
    next_haf = name[3:]
    print(first_hald.capitalize() + next_haf.capitalize())

old_mcdonals('macdonald')