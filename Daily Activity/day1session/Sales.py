""" Read salesman id, sales value and then find his commission
    Commision - 10% if salesvalue >= 50000 else commision is 0 """

#Enter Data
salesId = int(input("Enter Sales Man ID :"))
salesValue = int(input("Enter the sales value :"))

#Check Commission percentage
if salesValue <= 10000:
    salesCommission = 0
elif salesValue > 10000 and salesValue <= 50000:
    salesCommission = salesValue*0.1
elif salesValue > 50000 and salesValue <= 100000 :
    salesCommission = salesValue*0.15
elif salesValue > 100000:
    salesCommission = salesValue*0.2


print(f"Salesman ID: {salesId}, Commission: {salesCommission}")