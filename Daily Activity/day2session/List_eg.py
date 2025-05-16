''' Performing operations on list 
    |
    --->append(), remove(), pop(), sort(), reverse(), count(), index()'''

#Creating a list
phones = ["Apple iPhone", "Apple iPhone", "Samsung", "Google Pixel", "OnePlus", "Nothing" ]

#append()-add elements
phones.append("Blackberry")
print("Appended List : ",phones,"\n")

#remove()-remove element
phones.remove("OnePlus")
print("List after removing element :",phones,"\n")

#pop()-removes element from the end and returns it
popped_phone = phones.pop(2)
print(f"Phones that are removed from the list are : {popped_phone}","\n")

#sort()-Sort the list
phones.sort()
print("List after sorting :",phones,"\n")

#reverse()- Reverses the order of the list
phones.reverse()
print("Reversed List: ", phones,"\n")

#count()- Count the occurences of specific elements
print("Count of Apple iPhone :",phones.count("Apple iPhone"),"\n")

#index()- find the index of specific element
print("Index of Google Pixel",phones.index("Google Pixel"),"\n")

#Check if an element is present in the list
if "mango" in phones:
    print("Yes, Mango Present in List","\n")
else:
    print("No, Mango not in List","\n")

#Display in for loop
for i in phones:
    print(i)