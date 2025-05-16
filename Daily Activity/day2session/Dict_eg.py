''' Performing operations on Dictionary 
    |
    --->get(), keys(), values(), update(), pop(), popitem(), clear()'''

#Creating Dictionary

cars = {
    101:{"prodName":"Porsche 911 GT3RS", "prodPrice":"$500,000", "prodQuantity":25},
    102:{"prodName":"Nissan GT-R34", "prodPrice":"$800,000", "prodQuantity":15},
    103:{"prodName":"Toyota Supra MK5", "prodPrice":"$700,000", "prodQuantity":45}
}

#get()-Retrieve the value for a given key, Returns none if key not found
car_101 = cars.get(101)
print(f"Car 101 :", car_101,"\n")

#keys()- Returns a view of all the keys in the dictionary
keys=cars.keys()
print("Keys of all records :", keys,"\n")

#values() - Returns a view of all the values 
values = cars.values()
print("Values of all records :",values,"\n")

#update()
cars.update({103:{"prodName":"Mazda RX7", "prodPrice":"$200,000", "prodQuantity":5}})
print("Cars after update :", cars,"\n")

#pop()-removes and returns the key-value pair of the given key
removed_car = cars.pop(102)
print("Removed Car :", removed_car,"\n")

#popitem() - Removes and returns the last key value pair
last_item = cars.popitem()
print("Popped Car :", last_item,"\n")

#clear() - removes all elements from the Dictionary
cars.clear()
print("Dict after clearing :", cars,"\n")

search_item = input("Enter Item : ")
for item in cars.values():
    print(item)

