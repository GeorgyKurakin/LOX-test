This short code counts co-occurrences of entities for graph analysis, to further be used as edges of the graph. 
To use this code, you must list all entities in a CSV file of the following format:

entity1;entity2;entity3;entity4

entity1;entity4;entity5

entyty1;entyty2;entyty4;entity6;entyty7

The output CSV file will be in the following format:

entyty1;entity4;4

entity1;entity2;3

Thus, the code counts the co-occurrences of entities in the rows of input file. 

WARNING! 
Based on the example above, you could see that this code overstates the co-occurrence number by 1. In my project, I corrected this systematic error in Excel during further data processing. You could also correst in programmatically.
