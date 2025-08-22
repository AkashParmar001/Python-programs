data = []
header = ["Name","Age","City"]
print("Enter your data..enter 'done'whwn completed")
while True:
    name=input("Enter your Name.:")
    if name.lower() == 'done':
        break
    age=input("Enter your Age.:")
    city=input("Enter your City.:")
    
    
    data.append([name,age,city])
    
    from tabulate import tabulate
    print(tabulate(data, headers=header))