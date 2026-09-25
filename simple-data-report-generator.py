print("==== Simple Data Report Generator ====")

data =[]

n = int(input("How many values do you want to enter?"))

for i in range(n):
    value =float(input("Enter value:"))
    data.append(value)

total =sum(data)
average=total/len(data)
highest =max(data)
lowest=min(data)

print("\n ==== Data Report ====")
print("Total:", total)
print("Highest:",highest)
print("Lowest",lowest)
print("Number of values:",len(data))