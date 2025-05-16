''' Performing operations on tuple 
    |
    --->count(), index()'''

#Creating a tuple
coordinates = (40.1555, -74.5468, 36.0561, 40.1555 )

#count()- Count the occurences of specific elements
count_lattitude = coordinates.count(40.1555)
print(f"Count of 40.1555 :", count_lattitude)

#index()- find the index of specific element
index_of_lattitde = coordinates.index(36.0561)
print(f"Index of 36.0561 :", index_of_lattitde)

