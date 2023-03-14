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
            "bills": {"count": {"ones": 0, "fives": 0}}
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
            if command[1].lower() == "coke" or command[1].lower() == "pepsi" or command[1].lower() == "sprite" or command[1].lower() == "faygo" or command[1].lower() == "rc" or command[1].lower() == "jolt":
                count = int(command[2])
                if count < 0:
                    print("Count cannot be negative")
                else:
                    self.inventory[command[1].lower()]["count"] += count
                    print(f"Added {count} {command[1]}")
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
            total = self.inventory["bills"]["count"]["ones"] * 1 + self.inventory["bills"]["count"]["fives"] * 5 + self.inventory["coins"]["count"]["nickels"] * 0.05 + self.inventory["coins"]["count"]["dimes"] * .1 + self.inventory["coins"]["count"]["quarters"] * .25
            print("Amount Deposited = " + str(total))
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
        elif command[0].lower() in self.inventory:
            item = command[0].lower()
            if self.inventory[item] == "cups" and self.inventory[item]["count"] < 1:
                print("No cups available")
            elif self.inventory[item]["count"] == 0:
                print(f"{item} is out of stock")
            else:
                price = self.inventory[item]["price"]
                if self.get_money_inserted() < price:
                    print(f"Insert {price - self.get_money_inserted():.2f} more to buy {item}")
                else:
                    self.dispense_item(item, price)
                    self.return_change(self.get_money_inserted() - price)
        elif command[0].lower() == "cola":
            if command[1].lower() == "coke":
                print("Coke costs $" + str(self.inventory["coke"]["price"]))
            elif command[1].lower() == "sprite":
                print("Sprite costs $" + str(self.inventory["sprite"]["price"]))
            elif command[1].lower() == "rc":
                print("RC Cola costs $" + str(self.inventory["rc"]["price"]))
            elif command[1].lower() == "jolt":
                print("Jolt costs $" + str(self.inventory["jolt"]["price"]))
            elif command[1].lower() == "faygo":
                print("Faygo costs $" + str(self.inventory["faygo"]["price"]))
            elif command[1].lower() == "pepsi":
                print("Peps costs $" + str(self.inventory["pepsi"]["price"]))
        elif command[0].lower() == "coin":
            if command[1] == "5" or command[1] == "nickel".lower():
                print("Add 5 cents to inventory")
            elif command[1] == "10" or command[1] == "dime".lower():
                print("Add 10 cents to inventory")
            elif command[1] == "25" or command[1] == "quarter".lower():
                print("Add 25 cents to inventory")
            else:
                print("Not a valid coin amount")
        else:
            print("Invalid command")

    def get_bill_value(self, bill):
        if bill.lower() == "ones":
            return 1
        elif bill.lower() == "fives":
            return 5
        elif bill.lower() == "tens":
            return 10
        elif bill.lower() == "twenties":
            return 20
        else:
            return 0

    def get_money_inserted(self):
        return sum(self.inventory["coins"]["count"]["nickels"].values()) * 0.05 \
               + sum(self.inventory["coins"]["count"]["dimes"].values()) * 0.1 \
               + sum(self.inventory["coins"]["count"]["quarters"].values()) * 0.25 \
               + sum(self.inventory["bills"]["count"]["ones"].values()) * 1 \
               + sum(self.inventory["bills"]["count"]["fives"].values()) * 5 

    def dispense_item(self, item, price):
        self.inventory[item]["count"] -= 1
        self.inventory["coins"]["price"] += price
        print(f"Dispensed {item}")

    def return_change(self, change):
        if change > 0:
            print(f"Change: ${change:.2f}")
            self.inventory["Coins"]["price"] -= change
            self.inventory["Coins"]["count"]["Quarters"] -= int(change // 0.25)
            change = change % 0.25
            self.inventory["Coins"]["count"]["Dimes"] -= int(change // 0.1)
            change = change % 0.1
            self.inventory["Coins"]["count"]["Nickels"] -= int(change // 0.05)

vm = VendingMachine()
vm.run()

