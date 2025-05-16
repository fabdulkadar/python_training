''' Performing operations on Sets 
    |
    --->add(), remove(), discard(), union(), intersection(), clear()'''

#Creating a set
numbers = {1,2,4,5,6,7,8}

#add()- Adds an elemnt ot the set
numbers.add(55)
print("Set after adding the element :", numbers,"\n")

#remove()-remove element
numbers.remove(4)
print("Set after removing element :",numbers,"\n")

#discard()- removes element, but doesnt throw error when not found
numbers.discard(60)
print("Set after discarding element :",numbers,"\n")

#union()- Returns a set with all elements from both sets
set_2={10,20,30,40,50,60,1,2,3,4,5}
union_set= numbers.union(set_2)
print("Unions Set :", union_set,"\n")

#intersection()- Returns a set containing common elements
intersection_set = numbers.intersection(set_2)
print("Intersection Set: ", intersection_set,"\n")

#clear() - removes all elements from the set
set_2.clear()
print("Cleared Set 2: ", set_2,"\n")