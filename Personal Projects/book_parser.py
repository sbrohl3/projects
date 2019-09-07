
count = 1
count2 = 1
count3 = 1
count4 = 1
count5 = 1

with open("desktop/personal projects/neuromancer.txt", "r") as neuromancer:
    for line in neuromancer:
        line_list = line.split(" ")
        for word in line_list:
            if word == "Case":
                count2 += 1

            elif word == "Molly":
                count3 += 1

            elif word == "Wintermute":
                count4 += 1

            elif word == "Neuromancer":
                count5 += 1
            
            count += 1

    print("There are " + '{0:,}'.format(count) + " words in Neuromancer.")
    print("\nCase is mentioned in the book " + str(count2) + " times.")
    print("\nMolly is mentioned in the book " + str(count3) + " times.")
    print("\nWintermute is mentioned in the book " + str(count4) + " times.")
    print("\nNeuromancer is mentioned in the book " + str(count5) + " times.")