income = []
expenses = []

def addincome():
    while True:
        choice = input("A to add, X to exit ").upper()
        if choice == "A":
            title = input("What is it? ")
            money = input("How much is it? ")
            rate = input("How often (days)? ")
            currentincome = [title, money, rate]
            income.append(currentincome)
        if choice == "X":
            return

def addexpense():
    while True:
        choice = input("A to add, X to exit ").upper()
        if choice == "A":
            title = input("What is it? ")
            money = input("How much is it? ")
            rate = input("How often (days)? ")
            currentexpense = [title, money, rate]
            expenses.append(currentexpense)
        if choice == "X":
            return

def save():
    with open("budgeter.txt", "w") as file:
        file.write("Income\nTitle, Money, Rate (days)\n")
        file.write(str(income) + "\n")
        file.write("Expenses\nTitle, Money, Rate (days)\n")
        file.write(str(expenses) + "\n")
        
        file.write("Income, Expense, Net\n")
        totalincome = 0
        for eachincome in income:
            incomeadd = int(eachincome[1])
            totalincome += incomeadd
        totalincomestr = str(totalincome)
        file.write(totalincomestr + "     ")
        
        totalexpense = 0
        for eachexpense in expenses:
            expenseadd = int(eachexpense[1])
            totalexpense += expenseadd
        totalexpensestr = str(totalexpense)
        file.write(totalexpensestr + "     ")
        
        net = totalincome - totalexpense
        netstr = str(net)
        file.write(netstr + "\n")
        
        totalincomem = 0
        for eachincome in income:
            incomemaths = int(eachincome[2])
            monthly_income = (30 / incomemaths) * int(eachincome[1])
            totalincomem += monthly_income
        totalincomemstr = str(totalincomem)
        file.write("Monthly income: " + totalincomemstr + "\n")
        
        totalexpensem = 0
        for eachexpense in expenses:
            expensemaths = int(eachexpense[2])
            monthly_expense = (30 / expensemaths) * int(eachexpense[1])
            totalexpensem += monthly_expense
        totalexpensemstr = str(totalexpensem)
        file.write("Monthly expense: " + totalexpensemstr + "\n")
        
        netm = totalincomem - totalexpensem
        netmstr = str(netm)
        file.write("Monthly net: " + netmstr + "\n")

# MAIN
print("Welcome to Budgeter")
while True:
    choice = input("I to add income, E to add expense, S to save to file (will overwrite) ").upper()
    if choice == "I":
        addincome()
    if choice == "E":
        addexpense()
    if choice == "S":
        save()
