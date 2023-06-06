import tkinter as tk
from random import randint


class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Management Software")

        # Create a new user
        self.create_user_frame = tk.Frame(self.root)
        self.create_user_frame.pack()

        tk.Label(self.create_user_frame, text="Enter your name:").grid(
            row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.create_user_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.create_user_frame, text="Enter your age:").grid(
            row=1, column=0, sticky=tk.W)
        self.age_entry = tk.Entry(self.create_user_frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self.create_user_frame, text="Enter your gender:").grid(
            row=2, column=0, sticky=tk.W)
        self.gender_entry = tk.Entry(self.create_user_frame)
        self.gender_entry.grid(row=2, column=1)

        tk.Label(self.create_user_frame, text="Enter your DNI:").grid(
            row=3, column=0, sticky=tk.W)
        self.dni_entry = tk.Entry(self.create_user_frame)
        self.dni_entry.grid(row=3, column=1)

        tk.Button(self.create_user_frame, text="Create User",
                  command=self.create_user).grid(row=4, columnspan=2)

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        self.passenger = None  # Passenger object

        # Create menu options
        tk.Button(self.menu_frame, text="Generate Taxi Card",
                  command=self.generate_card).grid(row=0, sticky=tk.W)
        tk.Button(self.menu_frame, text="Recharge Taxi Card",
                  command=self.recharge_card).grid(row=1, sticky=tk.W)
        tk.Button(self.menu_frame, text="Delete Taxi Card",
                  command=self.delete_card).grid(row=2, sticky=tk.W)
        tk.Button(self.menu_frame, text="Pay Travel",
                  command=self.pay_travel).grid(row=3, sticky=tk.W)
        tk.Button(self.menu_frame, text="View all Taxi Cards",
                  command=self.view_all_cards).grid(row=4, sticky=tk.W)

    def create_user(self):
        try:
            passenger_name = self.name_entry.get()
            passenger_age = int(self.age_entry.get())
            passenger_gender = self.gender_entry.get()
            passenger_dni = int(self.dni_entry.get())
            passenger_id = randint(1, 1000)

            self.passenger = Passenger(
                passenger_name, passenger_age, passenger_gender, passenger_dni, passenger_id
            )
            self.passenger.set_TaxiCard(self.passenger)

            self.create_user_frame.pack_forget()  # Hide create user frame
        except ValueError:
            print("Typing error, enter again.")

    def generate_card(self):
        self.passenger.generateCard()

    def recharge_card(self):
        self.passenger.rechargeCard()

    def delete_card(self):
        self.passenger.deleteCard()

    def pay_travel(self):
        self.passenger.payTravel()

    def view_all_cards(self):
        self.passenger.printAll()


class Person:
    def __init__(self, name: str, age: int, gender: str, dni: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.dni = dni

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age: int):
        self.age = age

    def get_age(self):
        return self.age

    def set_gender(self, gender: str):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_dni(self, dni: int):
        self.dni = dni

    def get_dni(self):
        return self.dni

    def logIn(self):
        pass

    def logOut(self):
        pass


class Passenger(Person):
    def __init__(self, name: str, age: int, gender: str, dni: int, idPassenger: int):
        super().__init__(name, age, gender, dni)
        self.idPassenger = idPassenger
        self.TaxiCard_Passanger = 0

    def set_TaxiCard(self, informationPassenger):
        self.TaxiCard_Passanger = TaxiCard(informationPassenger)

    def get_TaxiCard(self):
        return self.TaxiCard_Passanger

    def get_idPassenger(self):
        return self.idPassenger

    def requestTaxi(self):
        pass

    def cancelTaxi(self):
        pass

    def generateCard(self):
        dni = self.get_TaxiCard().generateTaxiCard()
        if dni != None:
            print(f"Your card DNI: {dni}.")
        else:
            print("Error generating card.")

    def rechargeCard(self):
        while True:
            try:
                dni_for_charge = int(input("Enter DNI for charge: "))
                money_for_charge = float(input("Enter money for charge: "))
                self.get_TaxiCard().rechargeTaxiCard(dni_for_charge, money_for_charge)
                break
            except ValueError:
                print("Typing error, enter again.")

    def deleteCard(self):
        while True:
            try:
                dni_for_delete = int(input("Enter DNI for delete: "))
                self.get_TaxiCard().deleteTaxiCard(dni_for_delete)
                break
            except ValueError:
                print("Typing error, enter again.")

    def payTravel(self):
        while True:
            try:
                dni_for_travel = int(input("Enter DNI for travel: "))
                travel_cost = float(input("Enter cost of travel: "))
                self.get_TaxiCard().payCardTravel(dni_for_travel, travel_cost)
                break
            except ValueError:
                print("Typing error, enter again.")

    def printAll(self):
        print(self.get_TaxiCard().printall())


class Driver(Person):
    def __init__(self, name: str, age: int, gender: str, dni: int, idDriver: int, drivingLicense: str, ):
        super().__init__(name, age, gender, dni)
        self.idDriver = idDriver
        self.drivingLicense = drivingLicense
        self.status = True

    def get_idDriver(self):
        return self.idDriver

    def acceptPassenger(self, passenger: Passenger):
        pass

    def cancelPassenger(self, passenger: Passenger):
        pass

    def startTravel(self):
        pass

    def endTravel(self):
        pass


class TaxiCard:
    def __init__(self, informationPassenger: Passenger):
        self.informationPassenger = informationPassenger
        self.cashOnCard = 0
        self.generatedCards = []

    def set_informationPassenger(self, informationPassenger: Passenger):
        self.informationPassenger = informationPassenger

    def get_informationPassenger(self):
        return self.informationPassenger

    def set_cashOnCard(self, cashOnCard: int):
        self.cashOnCard = cashOnCard

    def get_cashOnCard(self):
        return self.cashOnCard

    def generateTaxiCard(self):
        # Obtiene la información del pasajero
        name = self.informationPassenger.get_name()
        age = self.informationPassenger.get_age()
        gender = self.informationPassenger.get_gender()
        dni = self.informationPassenger.get_dni()
        self.cashOnCard = 2500
        bandera = True
        for card in self.generatedCards:
            dniCard = card["DNI"]
            if dniCard == dni:
                bandera = False
                break
            else:
                continue
        if bandera == True:
            # Genera una nueva tarjeta y la agrega a la lista de tarjetas generadas

            self.generatedCards.append(
                {"Name": name, "Age": age, "Gender": gender, "DNI": dni, "Cash on card": self.cashOnCard})
            print("Your card has been generated successfully.")
            return dni
        else:
            print("This card already exists.")
            return None

    def deleteTaxiCard(self, idPassenger: int):
        bandera = True
        for card in self.generatedCards:
            dniCard = card["DNI"]
            # Busca la tarjeta correspondiente al pasajero y la elimina de la lista de tarjetas generadas
            if dniCard == idPassenger:
                self.generatedCards.remove(card)
                print("Your card has been deleted successfully.")
                break
            else:
                bandera = False
                continue
        if bandera == False:
            print("Card not found.")

    def rechargeTaxiCard(self, idPassenger: int, money: float):
        bandera = True
        for card in self.generatedCards:
            dniCard = card["DNI"]
            # Busca la tarjeta correspondiente al pasajero y recarga dinero en ella
            if dniCard == idPassenger:
                card["Cash on card"] += money
                print("Your card has been recharged successfully.")
                print(f"New card value: ${card['Cash on card']}.")
                break
            else:
                bandera = False
                continue
        if bandera == False:
            print("Card not found.")

    def payCardTravel(self, idPassenger: int, value: float):
        bandera = True
        for card in self.generatedCards:
            dniCard = card["DNI"]
            # Busca la tarjeta correspondiente al pasajero y verifica si hay suficiente dinero para pagar el viaje
            if dniCard == idPassenger:
                cash = card["Cash on card"]
                if cash - value < 0:
                    print("Insufficient cash, recharge card.")
                    break
                else:
                    card["Cash on card"] -= value
                    print("Paid travel.")
                    print(f"Your card value: ${card['Cash on card']}.")
                    break
            else:
                bandera = False
                continue
        if bandera == False:
            print("Card not found.")

    def printall(self):
        return self.generatedCards


if __name__ == '__main__':
    root = tk.Tk()
    MainGUI(root)
    root.mainloop()
