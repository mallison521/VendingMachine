import sys

class VendingMachine:
    def __init__(self):
        self.mode = "service"
        self.inventory = {
            "coke": {"count": 0, "price": 0.75},
            "pepsi": {"count": 0, "price": 0.75},
            "sprite": {"count": 0, "price": 0.75},
            "rc": {"count": 0, "price": 0.75},
            "faygo": {"count": 0, "price": 0.75},
            "jolt": {"count": 0, "price": 0.75},
            "cups": {"count": 0},
            "coins": {"count": {"nickels": 0, "dimes": 0, "quarters": 0}},
            "coinsCustomer": {"count": {"nickels": 0, "dimes": 0, "quarters": 0}},
            "bills": {"count": {"ones": 0, "fives": 0}},
            "billsCustomer": {"count": {"ones": 0, "fives": 0}}
        }
        self.password = "1234"

    def run(self):
        print("Please Enter a command and its parameter \n\
(Type Help for list of commands, EXIT to quit)\n")
        while True:
            if self.mode == "service":
                command = input("[Service Mode]> ").split()
            else:
                command = input("[Normal Mode]> ").split()
            if len(command) == 0:
                continue
            elif command[0].lower() == "lock":
                if len(command) != 2 or command[1] != self.password:
                    print("Invalid password, try again")
                else:
                    self.mode = "normal"
                    print("Switched to normal mode")
            elif command[0].lower() == "unlock":
                if len(command) != 2 or command[1] != self.password:
                    print("Invalid password, try again")
                else:
                    self.mode = "service"
                    print("Switched to service mode")
            elif self.mode == "service":
                self.handle_service_command(command)
            elif self.mode == "normal":
                self.handle_normal_command(command)

    def handle_service_command(self, command):
        if command[0].lower() == "help":
                print("Commands in Service Mode are:")
                print("STATUS")
                print("ADD [COLA|CUPS] brand <quantity>")
                print("ADD|REMOVE [COINS|BILLS] <denomination> <quantity>")
                print("EXIT")
                print(f"LOCK [{self.password}]")
        elif command[0].lower() == "add":
            if command[1].lower() == "cola":
                if command[2].lower() == "coke" or command[2].lower() == "pepsi" or command[2].lower() == "sprite" or command[2].lower() == "faygo" or command[2].lower() == "rc" or command[2].lower() == "jolt":
                    count = int(command[3])
                    if count < 0:
                        print("Count cannot be negative")
                    else:
                        self.inventory[command[2].lower()]["count"] += count
                        print(f"Added {count} {command[2]}")
                else:
                    print("Not a valid command")
            elif command[1].lower() == "cups":
                count = int(command[2])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    self.inventory[command[1].lower()]["count"] += count
                    print(f"Added {count} cups")
            elif command[2].lower() == "nickels" or command[2].lower() == "dimes" or command[2].lower() == "quarters":
                count = int(command[3])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    self.inventory["coins"]["count"][command[2].lower()] += count                        
                    print(f"Added {count} {command[2]}")
            elif command[2].lower() == "ones" or command[2].lower() == "fives":
                count = int(command[3])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    self.inventory["bills"]["count"][command[2]] += count
                    print(f"Added {count} {command[2]}")
            else:
                print("Invalid command")
        elif command[0].lower() == "remove":
            if command[1].lower() == "coke" or command[1].lower() == "pepsi" or command[1].lower() == "sprite" or command[1].lower() == "faygo" or command[1].lower() == "rc" or command[1].lower() == "jolt":
                count = int(command[2])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    if self.inventory >= count: 
                        self.inventory[command[1].lower()]["count"] -= count
                        print(f"Removed {count} {command[1]}")
                    else:
                        print("Sorry there is not enough in the machine")
            elif command[1].lower() == "cups":
                count = int(command[2])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    if self.inventory[command[1].lower()]["count"] >= count:
                        self.inventory[command[1].lower()]["count"] -= count
                        print(f"Removed {count} cups")
                    else:
                        print("Sorry there is not enough in the machine")
            elif command[2].lower() == "nickels" or command[2].lower() == "dimes" or command[2].lower() == "quarters":
                count = int(command[3])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    if self.inventory["coins"]["count"][command[2].lower()] >= count:
                        self.inventory["coins"]["count"][command[2].lower()] -= count                        
                        print(f"Removed {count} {command[2]}")
                    else:
                        print("Sorry there is not enough in the machine")
            elif command[2].lower() == "ones" or command[2].lower() == "fives":
                count = int(command[3])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    if self.inventory["bills"]["count"][command[2].lower()] >= count:
                        self.inventory["bills"]["count"][command[2].lower()] -= count                        
                        print(f"Removed {count} {command[2]}")
                    else:
                        print("Sorry there is not enough in the machine")    
        elif command[0].lower() == "status":
            print("Total Amount in Machine = ${:.2f}".format(self.get_money_inserted() - self.get_money_inserted_customer()))
            print("total One Dollar Bills = " + str(self.inventory["bills"]["count"]["ones"]))
            print("total Five Dollar Bills = " + str(self.inventory["bills"]["count"]["fives"]))
            print("total Nickels = " + str(self.inventory["coins"]["count"]["nickels"]))
            print("total Dimes = " + str(self.inventory["coins"]["count"]["dimes"]))
            print("total Quarters = " + str(self.inventory["coins"]["count"]["quarters"]))
            print("total Coke = " + str(self.inventory["coke"]["count"]))
            print("total Pepsi = " + str(self.inventory["pepsi"]["count"]))
            print("total RC = " + str(self.inventory["rc"]["count"]))
            print("total Jolt = " + str(self.inventory["jolt"]["count"]))
            print("total Faygo = " + str(self.inventory["faygo"]["count"]))
            print("total Cups = " + str(self.inventory["cups"]["count"]))
        elif command[0].lower() == "exit":
            print("Now exiting... Have a nice day.")
            sys.exit()
        else:
            print("Invalid command")

    def handle_normal_command(self, command):
        if command[0].lower() == "help":
            print("Commands in Normal Mode are:")
            print("Coin <value> where value is 5 10 25 nickel dime quarter")
            print("Bill <value> where value is 1 5")
            print("Cola <value> where value is coke pepsi sprite rc jolt faygo")
            print("Exit")
            print("Unlock [password]")
        elif command[0].lower() == "coin":
            if command[1] == "5" or command[1] == "nickel".lower():
                self.inventory["coinsCustomer"]["count"]["nickels"] += 1
                print("5 cents received total amount is: {:.2f}".format(self.get_money_inserted_customer()))
            elif command[1] == "10" or command[1] == "dime".lower():
                self.inventory["coinsCustomer"]["count"]["dimes"] += 1
                print("10 cents received total amount is: {:.2f}".format(self.get_money_inserted_customer()))
            elif command[1] == "25" or command[1] == "quarter".lower():
                self.inventory["coinsCustomer"]["count"]["quarters"] += 1
                print("25 cents received total amount is: {:.2f}".format(self.get_money_inserted_customer()))
            else:
                print("Not a valid coin amount")
        elif command[0].lower() == "bill":
            if command[1] == "1":
                self.inventory["billsCustomer"]["count"]["ones"] += 1
                self.inventory["bills"]["count"]["ones"] += 1
                print("1 dollar received total amount is: {:.2f}".format(self.get_money_inserted_customer()))
            elif command[1] == "5":
                self.inventory["billsCustomer"]["count"]["fives"] += 1
                self.inventory["bills"]["count"]["fives"] += 1
                print("5 dollars received total amount is: {:.2f}".format(self.get_money_inserted_customer()))
        elif command[0].lower() == "cups":
            item = command[0].lower()
            if self.inventory[item] == "cups" and self.inventory[item]["count"] < 1:
                print("No cups available")
            elif self.inventory[item]["count"] == 0:
                print(f"{item} is out of stock")
        elif command[0].lower() == "cola":
            if command[1].lower() == "coke":
                price = self.inventory["coke"]["price"]
                item = command[1].lower()
                if self.inventory["coke"]["count"] > 0 and self.inventory["cups"]["count"] > 0:
                    print("Coke costs $" + str(price))
                    if self.get_money_inserted_customer() < self.inventory["coke"]["price"]:
                        print(f"Insert ${price - self.get_money_inserted_customer():.2f} more to buy {item}")
                    else:
                        self.dispense_item(item)
                        change = self.get_money_inserted_customer() - price
                        print(f"Your change is ${change}")
                else:
                    print("Sorry coke is out or there are no cups left")
            elif command[1].lower() == "sprite":
                price = self.inventory["sprite"]["price"]
                item = command[1].lower()
                if self.inventory["sprite"]["count"] > 0 and self.inventory["cups"]["count"] > 0:
                    print("Sprite costs $" + str(price))
                    if self.get_money_inserted_customer() < self.inventory["sprite"]["price"]:
                        print(f"Insert ${price - self.get_money_inserted_customer():.2f} more to buy {item}")
                    else:
                        self.dispense_item(item)
                        change = self.get_money_inserted_customer() - price
                        print(f"Your change is ${change}")
                else:
                    print("Sorry sprite is out or there are no cups left")
            elif command[1].lower() == "rc":
                price = self.inventory["rc"]["price"]
                item = command[1].lower()
                if self.inventory["rc"]["count"] > 0 and self.inventory["cups"]["count"] > 0:
                    print("RC cola costs $" + str(price))
                    if self.get_money_inserted_customer() < self.inventory["rc"]["price"]:
                        print(f"Insert ${price - self.get_money_inserted_customer():.2f} more to buy {item}")
                    else:
                        self.dispense_item(item)
                        change = self.get_money_inserted_customer() - price
                        print(f"Your change is ${change}")
                else:
                    print("Sorry RC cola is out or there are no cups left")
            elif command[1].lower() == "jolt":
                price = self.inventory["jolt"]["price"]
                item = command[1].lower()
                if self.inventory["jolt"]["count"] > 0 and self.inventory["cups"]["count"] > 0:
                    print("Jolt costs $" + str(price))
                    if self.get_money_inserted_customer() < self.inventory["jolt"]["price"]:
                        print(f"Insert ${price - self.get_money_inserted_customer():.2f} more to buy {item}")
                    else:
                        self.dispense_item(item)
                        change = self.get_money_inserted_customer() - price
                        print(f"Your change is ${change}")
                else:
                    print("Sorry Jolt is out or there are no cups left")
            elif command[1].lower() == "faygo":
                price = self.inventory["faygo"]["price"]
                item = command[1].lower()
                if self.inventory["faygo"]["count"] > 0 and self.inventory["cups"]["count"] > 0:
                    print("Faygo costs $" + str(price))
                    if self.get_money_inserted_customer() < self.inventory["faygo"]["price"]:
                        print(f"Insert ${price - self.get_money_inserted_customer():.2f} more to buy {item}")
                    else:
                        self.dispense_item(item)
                        change = self.get_money_inserted_customer() - price
                        print(f"Your change is ${change}")
                else:
                    print("Sorry Faygo is out or there are no cups left")
            elif command[1].lower() == "pepsi":
                price = self.inventory["pepsi"]["price"]
                item = command[1].lower()
                if self.inventory["pepsi"]["count"] > 0 and self.inventory["cups"]["count"] > 0:
                    print("Pepsi costs $" + str(price))
                    if self.get_money_inserted_customer() < self.inventory["pepsi"]["price"]:
                        print(f"Insert ${price - self.get_money_inserted_customer():.2f} more to buy {item}")
                    else:
                        self.dispense_item(item)
                        change = self.get_money_inserted_customer() - price
                        print(f"Your change is ${change}")
                else:
                    print("Sorry Pepsi is out or there are no cups left")
        elif command[0].lower() == "exit":
            print("Now exiting... Have a nice day.")
            sys.exit()
        else:
            print("Invalid command")
    

    def get_money_inserted_customer(self):
        return self.inventory["coinsCustomer"]["count"]["nickels"] * 0.05 \
               + self.inventory["coinsCustomer"]["count"]["dimes"] * 0.1 \
               + self.inventory["coinsCustomer"]["count"]["quarters"] * 0.25 \
               + self.inventory["billsCustomer"]["count"]["ones"] * 1 \
               + self.inventory["billsCustomer"]["count"]["fives"] * 5 
    
    def get_money_inserted(self):
        return self.inventory["coins"]["count"]["nickels"] * 0.05 \
               + self.inventory["coins"]["count"]["dimes"] * 0.1 \
               + self.inventory["coins"]["count"]["quarters"] * 0.25 \
               + self.inventory["bills"]["count"]["ones"] * 1 \
               + self.inventory["bills"]["count"]["fives"] * 5 

    def dispense_item(self, item):
        total = self.inventory["bills"]["count"]["ones"] * 1 + self.inventory["bills"]["count"]["fives"] * 5 + self.inventory["coins"]["count"]["nickels"] * 0.05 + self.inventory["coins"]["count"]["dimes"] * .1 + self.inventory["coins"]["count"]["quarters"] * .25
        if self.inventory[item]["count"] > 0:
            self.inventory[item]["count"] -= 1
            total -= total
            print(f"Dispensed {item}")


vm = VendingMachine()
vm.run()

