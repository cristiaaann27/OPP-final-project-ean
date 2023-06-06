from random import randint


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


class Main():
    def __init__(self):
        print("Welcome to the Taxi Management Software.")
        self.run()

    def run(self):
        print("Create a new user: ")
        while True:
            try:
                passenger_name = input("Enter your name: ")
                passenger_age = int(input("Enter your age: "))
                passenger_gender = input("Enter your gender: ")
                passenger_dni = int(input("Enter your DNI: "))
                passenger_id = randint(1, 1000)
                passenger_created = Passenger(
                    passenger_name, passenger_age, passenger_gender, passenger_dni, passenger_id)
                passenger_created.set_TaxiCard(passenger_created)

                break
            except ValueError:
                print("Typing error, enter again.")
        while True:
            print("What do you want to do?")
            print("""
            1. Generate Taxi Card.
            2. Recharge Taxi Card.
            3. Delete Taxi Card
            4. Pay travel.
            5. View all Taxi Cards.
            6. Exit.
            """)
            try:
                option = int(input("Enter a number option: "))
                if option == 1:

                    passenger_created.generateCard()
                elif option == 2:
                    passenger_created.rechargeCard()
                elif option == 3:
                    passenger_created.deleteCard()
                elif option == 4:
                    passenger_created.payTravel()

                elif option == 5:
                    passenger_created.printAll()
                elif option == 6:
                    print("Thank you for using the software, good day")
                    break
                else:
                    print("Option not available. Please enter a valid option.")
            except ValueError:
                print("Invalid value, enter it again.")


if __name__ == '__main__':
    Main()
