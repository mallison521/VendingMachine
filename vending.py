class VendingMachine:
    def __init__(self):
        self.service_password = "nancy"
        self.inventory = {
            "Coke": 0,
            "Pepsi": 0,
            "RC": 0,
            "Jolt": 0,
            "Faygo": 0,
            "Nickels": 0,
            "Dimes": 0,
            "Quarters": 0,
            "One Dollar Bills": 0,
            "Five Dollar Bills": 0,
            "Cups": 0
        }
        self.deposited_amount = 0.0
        self.is_locked = True  # start in service mode
        self.locked_password = ""

    def run(self):
        print("Please Enter a command and its parameter")
        print("(Type Help for list of commands, EXIT to quit)")

        while True:
            if self.is_locked:
                prompt = "[SERVICE MODE]>"
            else:
                prompt = "[NORMAL MODE]>"

            command = input(prompt).strip().lower()

            if command == "exit":
                break
            elif command == "help":
                self.help()
            elif self.is_locked and command.startswith("lock "):
                self.lock(command[5:])
            elif not self.is_locked and command.startswith("unlock "):
                self.unlock(command[7:])
            elif not self.is_locked:
                self.execute(command)

    def help(self):
        if self.is_locked:
            print("Commands in Service Mode are:")
            print("Status")
            print("Add [COLA|CUPS] brand <quantity>")
            print("Add|Remove [Coins|Bills] <denomination> <quantity>")
            print("Exit")
            print("Lock [password]")
        else:
            print("Commands in Normal Mode are:")
            print("Coin <value> where value is 5 10 25 nickel dime quarter")
            print("Bill <value> where value is 1 5")
            print("Cola <value> where value is coke pepsi rc jolt faygo")
            print("Exit")
            print("Unlock [password]")

    def lock(self, password):
        if password == self.service_password:
            self.is_locked = False
            self.locked_password = password
            print("[NORMAL MODE]>")
        else:
            print("Invalid password, try again")

    def unlock(self, password):
        if password == self.locked_password:
            self.is_locked = True
            self.locked_password = ""
            print("[SERVICE MODE]>")
        else:
            print("Invalid password, try again")

    def execute(self, command):
        parts = command.split(" ")
        main_command = parts[0]

        if main_command == "coin":
            self.add_coin(parts[1])
        elif main_command == "bill":
            self.add_bill(parts[1])
        elif main_command in ["cola", "pepsi", "rc", "jolt", "faygo"]:
            self.dispense_drink(main_command, parts[1] if len(parts) > 1 else "1")
        elif main_command == "exit":
            return
        else:
            print("Invalid command, try again")

    def add_coin(self, denomination):
        if denomination == "5":
            self.inventory["Nickels"] += 1
            self.deposited_amount += 0.05
        elif denomination == "10":
            self.inventory["Dimes"] += 1
            self.deposited_amount += 0.1
        elif denomination == "25":
            self.inventory["Quarters"] += 1
            self.deposited_amount += 0.25
        else:
            print("Invalid coin denomination")

    def add_bill(self, denomination):
        if denomination == "1":
            self.inventory["One Dollar Bills"] += 1
            self.deposited_amount += 1
        elif denomination == "5":
            self.inventory["Five Dollar Bills"] += 1
            self.deposited_amount += 5
        else:
            print("Invalid bill denomination")

    def add_cola(self, brand, quantity):
        brand = brand.lower().capitalize()
        if brand in self.inventory.keys() and brand != "Cups":
            self.inventory[brand] += quantity
        else:
            print("Invalid brand")

    def add_cups(self, brand, quantity):
        brand = brand.lower().capitalize()
        if brand == "Cups":
            self.inventory[brand] += quantity
        else:
            print("Invalid item")

    def remove_coin(self, denomination, quantity):
        if denomination in ["5", "10", "25"]:
            if self.inventory[self._get_coin_name(denomination)] >= quantity:
                self.inventory[self._get_coin_name(denomination)] -= quantity
                self.deposited_amount -= denomination * quantity / 100
            else:
                print("Not enough coins in inventory")
        else:
            print("Invalid coin denomination")

    def remove_bill(self, denomination, quantity):
        if denomination in ["1", "5"]:
            if self.inventory[self._get_bill_name(denomination)] >= quantity:
                self.inventory[self._get_bill_name(denomination)] -= quantity
                self.deposited_amount -= denomination * quantity
            else:
                print("Not enough bills in inventory")
        else:
            print("Invalid bill denomination")

    def remove_cola(self, brand, quantity):
        brand = brand.lower().capitalize()
        if brand in self.inventory.keys() and brand != "Cups":
            if self.inventory[brand] >= quantity:
                self.inventory[brand] -= quantity
            else:
                print("Not enough " + brand + " in inventory")
        else:
            print("Invalid brand")

    def remove_cups(self, brand, quantity):
        brand = brand.lower().capitalize()
        if brand == "Cups":
            if self.inventory[brand] >= quantity:
                self.inventory[brand] -= quantity
            else:
                print("Not enough cups in inventory")
        else:
            print("Invalid item")


