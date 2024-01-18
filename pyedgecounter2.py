import csv

edge_dictionary = {"dictservice,dictservices": 0}
block_list = ["service_item"]

with open ("bacterialtraits.csv", "r") as csvfile1:
    traitreader = csv.reader (csvfile1, delimiter = ';')
    for row in traitreader:
        trait_list = row
        for first_string in trait_list:
            for second_string in trait_list:
                if first_string !=second_string:
                    key_string = first_string+","+second_string
                    block_string = second_string+","+first_string
                    if key_string not in edge_dictionary:
                        if key_string not in block_list:
                            edge_dictionary[key_string] = 1
                    if key_string in edge_dictionary:    
                        edge_dictionary[key_string] += 1 
                    if block_string not in block_list:
                        block_list.append(block_string)                     
    

with open ("edgelist.txt", "w") as csvfile2:
    for key, value in edge_dictionary.items():
        csvfile2.write(f'{key}, {value}\n')

print ("Pyedgecounter job complete!")  