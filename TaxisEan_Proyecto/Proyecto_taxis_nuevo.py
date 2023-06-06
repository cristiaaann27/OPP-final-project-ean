from random import randint
import tkinter as tk
from tkinter import messagebox
import pickle
import os


class Person:
    def __init__(self, name: str, age: int, gender: str, dni: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.dni = dni

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

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

    def sign_up(self):
        pass


class Administrator(Person):
    def __init__(self, name: str, age: int, gender: str, dni: int, ):
        super().__init__(name, age, gender, dni)


class Passenger(Person):
    def __init__(self, name: str, age: int, gender: str, dni: int, ):
        super().__init__(name, age, gender, dni)
        self.taxicarddata = Data()
        self.TaxiCard_Passanger = None

    def set_TaxiCard(self, informationPassenger):
        self.TaxiCard_Passanger = TaxiCard(informationPassenger)
        self.taxicarddata.set_createdCards(self.TaxiCard_Passanger)

    def get_TaxiCard(self):
        return self.TaxiCard_Passanger

    def rechargeCard(self, taxiCard, cash: int):
        flag = False
        for card in self.taxicarddata.get_createdCards():
            print(card.get_dniPassenger(), taxiCard.get_dniPassenger())
            if card.get_dniPassenger() == taxiCard.get_dniPassenger():
                card.set_cashOnCard(card.get_cashOnCard() + cash)
                flag = True
                break
            else:
                continue
        if flag == False:
            print("Card not found.")
        else:
            print("You can now view your Cash on card.")

    def requestTaxi(self, taxiCard):
        if self.taxi_card is not None:
            # Logic for requesting a taxi
            print("Taxi requested")
        else:
            print("No taxi card found. Please generate a card first.")

    def cancelTaxi(self):
        if self.taxi_card is not None:
            # Logic for canceling a taxi
            print("Taxi canceled")
        else:
            print("No taxi card found. Please generate a card first.")

    def deleteCard(self, id):
        self.taxi_card = None
        print("Card deleted")

    def payTravel(self, taxiCard, amount: int):
        if self.taxi_card is not None:
            if self.taxi_card.get_cashOnCard() >= amount:
                # Logic for deducting the travel fare from the card balance
                self.taxi_card.set_cashOnCard(
                    self.taxi_card.get_cashOnCard() - amount)
                print(f"Travel fare of {amount} units deducted from the card")
            else:
                print("Insufficient balance on the card. Please recharge the card.")
        else:
            print("No taxi card found. Please generate a card first.")


class Driver(Person):
    def __init__(self, name: str, age: int, gender: str, dni: int, drivingLicense: str, ):
        super().__init__(name, age, gender, dni)
        self.drivingLicense = drivingLicense
        self.available = True

    def get_license(self):
        return self.drivingLicense

    def acceptPassenger(self):
        pass

    def cancelPassenger(self):
        pass

    def startTravel(self):
        pass

    def endTravel(self):
        pass


class TaxiCard:
    def __init__(self, dniPassenger: int):
        self.dniPassenger = dniPassenger
        self.cashOnCard = 0

    def get_dniPassenger(self):
        return self.dniPassenger

    def set_cashOnCard(self, cashOnCard: int):
        self.cashOnCard = cashOnCard

    def get_cashOnCard(self):
        return self.cashOnCard

    def __str__(self):
        return f"""
        DNI: {self.get_dniPassenger()}
        Cash on card: {self.get_cashOnCard()}
        """


class Data:
    def __init__(self):
        self.createdUsers = []
        self.createdCards = []
    # Users

    def set_createdUsers(self, person):
        self.createdUsers.append(person)

    def get_createdUsers(self):
        return self.createdUsers

    # Cards
    def set_createdCards(self, info):
        self.createdCards.append(info)

    def get_createdCards(self):
        return self.createdCards


class Main():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Taxi Management Software")
        self.root.geometry("1x1")
        self.data = self.load_created_users()
        self.registration_window = None  # Reference to the registration window
        self.person_window = None  # Reference to the person window
        self.create_registration_window()
        self.root.mainloop()

    def load_created_users(self):
        try:
            with open('users.dat', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return Data()

    def save_created_users(self):
        with open('users.dat', 'wb') as file:
            pickle.dump(self.data, file)

    def create_registration_window(self):
        if self.registration_window is None:
            self.registration_window = tk.Toplevel(self.root)
            self.registration_window.title("Registration")
            self.registration_window.geometry("250x250")

            # User Role Label and OptionMenu
            role_label = tk.Label(self.registration_window,
                                  text="Select User Role:")
            role_label.pack()

            role_var = tk.StringVar(self.registration_window)
            role_var.set("Passenger")  # Default value
            role_option_menu = tk.OptionMenu(
                self.registration_window, role_var, "Passenger", "Driver", "Administrator")
            role_option_menu.pack()

            # Register Button
            register_button = tk.Button(self.registration_window, text="Register",
                                        command=lambda: self.register(role_var.get()))
            register_button.pack()
            # Login Button
            login_button = tk.Button(
                self.registration_window, text="Login", command=self.login)
            login_button.pack()

        else:
            messagebox.showinfo(
                "Registration", "A registration window is already open.")

    def register(self, role):
        # Perform registration based on the selected role
        if role == "Passenger":
            self.register_passenger()
        elif role == "Driver":
            self.register_driver()
        elif role == "Administrator":
            self.register_administrator()

    def login(self):
        # Implement login form here
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Login")
        self.login_window.geometry("250x250")

        # ID Label and Entry
        dni_label = tk.Label(self.login_window, text="DNI:")
        dni_label.pack()

        dni_entry = tk.Entry(self.login_window)
        dni_entry.pack()

        # Password Label and Entry
        password_label = tk.Label(self.login_window, text="Password:")
        password_label.pack()

        password_entry = tk.Entry(self.login_window, show="*")
        password_entry.pack()

        # User Role Label and OptionMenu
        role_label = tk.Label(self.login_window, text="User Role:")
        role_label.pack()

        role_var = tk.StringVar(self.login_window)
        role_var.set("Passenger")  # Default value
        role_option_menu = tk.OptionMenu(
            self.login_window, role_var, "Passenger", "Driver", "Administrator")
        role_option_menu.pack()

        # Login Button
        login_button = tk.Button(self.login_window, text="Login", command=lambda: self.validate_login(
            dni_entry.get(), password_entry.get(), role_var.get()))
        login_button.pack()
        close_buttom = tk.Button(
            self.login_window, text="Close", command=lambda: self.login_window.destroy())
        close_buttom.pack()

    def validate_login(self, dni, password, role):
        # Perform validation based on the entered credentials
        flag = False
        for user in self.data.get_createdUsers():
            class_name = user.__class__.__name__
            if (user.get_dni() == int(dni)) and (user.get_password() == password) and (class_name.lower() == role.lower()):
                log = user
                flag = True
                self.show_login_message(log, class_name)
                self.login_window.destroy()
                self.registration_window.destroy()
                break

            else:
                flag = False
                continue
        if flag == False:
            self.show_error_message("Invalid credentials")

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

    def show_registration_success(self):
        success_window = tk.Toplevel(self.root)
        success_window.title("Registration Success")
        success_label = tk.Label(
            success_window, text=" Registration successful!")
        success_label.pack()
        close_buttom = tk.Button(success_window,
                                 text="Close", command=lambda: success_window.destroy())
        close_buttom.pack()

    def show_save_success(self):
        success_window = tk.Toplevel(self.root)
        success_window.title("Saved Success")
        success_label = tk.Label(
            success_window, text=" Saved changes successful!")
        success_label.pack()
        close_buttom = tk.Button(success_window,
                                 text="Close", command=lambda: success_window.destroy())
        close_buttom.pack()

    def show_login_message(self, log, role):
        success_window = tk.Toplevel(self.root)
        success_window.title("Login Success")
        success_label = tk.Label(success_window, text=f" Login successful!")
        success_label.pack()
        next_buttom = tk.Button(success_window,
                                text="Next", command=lambda: self.log_now(log, role))
        next_buttom.pack()
        close_buttom = tk.Button(success_window,
                                 text="Close", command=lambda: success_window.destroy())
        close_buttom.pack()

    def register_passenger(self):
        self.registration_passenger_window = tk.Toplevel(self.root)
        self.registration_passenger_window.title("Passenger Registration")
        self.registration_passenger_window.geometry("250x250")

        # Name
        name_label = tk.Label(self.registration_passenger_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(self.registration_passenger_window)
        name_entry.pack()

        # Age
        age_label = tk.Label(self.registration_passenger_window, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(self.registration_passenger_window)
        age_entry.pack()

        # Gender
        gender_label = tk.Label(
            self.registration_passenger_window, text="Gender:")
        gender_label.pack()
        gender_var = tk.StringVar(self.registration_passenger_window)
        gender_var.set("Male")  # Default value
        gender_option_menu = tk.OptionMenu(
            self.registration_passenger_window, gender_var, "Male", "Female", "Other")
        gender_option_menu.pack()

        # DNI
        dni_label = tk.Label(self.registration_passenger_window, text="DNI:")
        dni_label.pack()
        dni_entry = tk.Entry(self.registration_passenger_window)
        dni_entry.pack()

        # Password
        password_label = tk.Label(
            self.registration_passenger_window, text="Password:")
        password_label.pack()
        # Show * instead of actual characters
        password_entry = tk.Entry(self.registration_passenger_window, show="*")
        password_entry.pack()

        # Confirm Password
        confirm_password_label = tk.Label(
            self.registration_passenger_window, text="Confirm Password:")
        confirm_password_label.pack()
        confirm_password_entry = tk.Entry(
            self.registration_passenger_window, show="*")
        confirm_password_entry.pack()

        # Register Button
        register_button = tk.Button(self.registration_passenger_window, text="Register", command=lambda: self.process_passenger_registration(
            name_entry.get(), age_entry.get(), gender_var.get(), dni_entry.get(), password_entry.get(), confirm_password_entry.get()))
        register_button.pack()
        close_buttom = tk.Button(
            self.registration_passenger_window, text="Close", command=lambda: self.registration_passenger_window.destroy())
        close_buttom.pack()

    def process_passenger_registration(self, name, age, gender, dni, password, confirm_password):
        # Validate the input data and perform the registration logic
        if not name:
            self.show_error_message("Name is required.")
        elif not age.isdigit():
            self.show_error_message(
                "Invalid age. Please enter a valid number.")
        elif not 0 <= int(age) <= 120:
            self.show_error_message(
                "Invalid age. Age must be between 0 and 120.")
        elif gender not in ["Male", "Female", "Other"]:
            self.show_error_message(
                "Invalid gender. Please select a valid option.")
        elif not dni.isdigit():
            self.show_error_message(
                "Invalid DNI. Please enter a valid number.")
        elif not password:
            self.show_error_message("Password is required.")
        elif password != confirm_password:
            self.show_error_message(
                "Passwords do not match. Please enter the same password.")
        else:
            # Perform the passenger registration with the validated data
            self.perform_passenger_registration(
                name, int(age), gender, int(dni), password)

    def perform_passenger_registration(self, name, age, gender, dni, password):
        # TODO: Implement the passenger registration logic with the validated data
        self.show_registration_success()

        passenger_created = Passenger(name, age, gender, dni)
        passenger_created.set_password(password)

        self.data.set_createdUsers(passenger_created)
        self.save_created_users()

        # Close window
        self.registration_passenger_window.destroy()

    def register_driver(self):
        self.registration_driver_window = tk.Toplevel(self.root)
        self.registration_driver_window.title("Driver Registration")
        self.registration_driver_window.geometry("250x250")

        # Name
        name_label = tk.Label(self.registration_driver_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(self.registration_driver_window)
        name_entry.pack()

        # Age
        age_label = tk.Label(self.registration_driver_window, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(self.registration_driver_window)
        age_entry.pack()

        # Gender
        gender_label = tk.Label(
            self.registration_driver_window, text="Gender:")
        gender_label.pack()
        gender_var = tk.StringVar(self.registration_driver_window)
        gender_var.set("Male")  # Default value
        gender_option_menu = tk.OptionMenu(
            self.registration_driver_window, gender_var, "Male", "Female", "Other")
        gender_option_menu.pack()

        # DNI
        dni_label = tk.Label(self.registration_driver_window, text="DNI:")
        dni_label.pack()
        dni_entry = tk.Entry(self.registration_driver_window)
        dni_entry.pack()

        # Driver's License
        license_label = tk.Label(
            self.registration_driver_window, text="Driver's License:")
        license_label.pack()
        license_var = tk.StringVar(self.registration_driver_window)
        license_var.set("B1")  # Default value
        license_option_menu = tk.OptionMenu(
            self.registration_driver_window, license_var, "B1", "B2", "B3", "C1", "C2", "C3")
        license_option_menu.pack()

        # Password
        password_label = tk.Label(
            self.registration_driver_window, text="Password:")
        password_label.pack()
        # Show * instead of actual characters
        password_entry = tk.Entry(self.registration_driver_window, show="*")
        password_entry.pack()

        # Confirm Password
        confirm_password_label = tk.Label(
            self.registration_driver_window, text="Confirm Password:")
        confirm_password_label.pack()
        confirm_password_entry = tk.Entry(
            self.registration_driver_window, show="*")
        confirm_password_entry.pack()

        # Register Button
        register_button = tk.Button(self.registration_driver_window, text="Register",
                                    command=lambda: self.process_driver_registration(name_entry.get(),
                                                                                     age_entry.get(),
                                                                                     gender_var.get(),
                                                                                     dni_entry.get(),
                                                                                     license_var.get(), password_entry.get(), confirm_password_entry.get()))
        register_button.pack()
        close_buttom = tk.Button(
            self.registration_driver_window, text="Close", command=lambda: self.registration_driver_window.destroy())
        close_buttom.pack()

    def process_driver_registration(self, name, age, gender, dni, license_var, password, confirm_password):
        # Validate the input data and perform the registration logic
        if not name:
            self.show_error_message("Name is required.")
        elif not age.isdigit():
            self.show_error_message(
                "Invalid age. Please enter a valid number.")
        elif not 0 <= int(age) <= 120:
            self.show_error_message(
                "Invalid age. Age must be between 0 and 120.")
        elif gender not in ["Male", "Female", "Other"]:
            self.show_error_message(
                "Invalid gender. Please select a valid option.")
        elif not dni.isdigit():
            self.show_error_message(
                "Invalid DNI. Please enter a valid number.")
        elif license_var not in ["B1", "B2", "B3", "C1", "C2", "C3"]:
            self.show_error_message(
                "Invalid license. Please select a valid option.")
        elif not password:
            self.show_error_message("Password is required.")
        elif password != confirm_password:
            self.show_error_message(
                "Passwords do not match. Please enter the same password.")
        else:
            # Perform the passenger registration with the validated data
            self.perform_driver_registration(
                name, int(age), gender, int(dni), license_var, password)

    def perform_driver_registration(self, name, age, gender, dni, license_var, password):
        self.show_registration_success()
        # TODO: Implement the driver registration logic with the validated data
        driver_created = Driver(name, age, gender, dni, license_var)
        driver_created.set_password(password)
        self.data.set_createdUsers(driver_created)
        self.save_created_users()

        # Close window
        self.registration_driver_window.destroy()

    def register_administrator(self):
        self.registration_admin_window = tk.Toplevel(self.root)
        self.registration_admin_window.title("Passenger Registration")
        self.registration_admin_window.geometry("250x250")

        # Name
        name_label = tk.Label(self.registration_admin_window, text="Name:")
        name_label.pack()
        name_entry = tk.Entry(self.registration_admin_window)
        name_entry.pack()

        # Age
        age_label = tk.Label(self.registration_admin_window, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(self.registration_admin_window)
        age_entry.pack()

        # Gender
        gender_label = tk.Label(self.registration_admin_window, text="Gender:")
        gender_label.pack()
        gender_var = tk.StringVar(self.registration_admin_window)
        gender_var.set("Male")  # Default value
        gender_option_menu = tk.OptionMenu(
            self.registration_admin_window, gender_var, "Male", "Female", "Other")
        gender_option_menu.pack()

        # DNI
        dni_label = tk.Label(self.registration_admin_window, text="DNI:")
        dni_label.pack()
        dni_entry = tk.Entry(self.registration_admin_window)
        dni_entry.pack()

        # Password
        password_label = tk.Label(
            self.registration_admin_window, text="Password:")
        password_label.pack()
        # Show * instead of actual characters
        password_entry = tk.Entry(self.registration_admin_window, show="*")
        password_entry.pack()

        # Confirm Password
        confirm_password_label = tk.Label(
            self.registration_admin_window, text="Confirm Password:")
        confirm_password_label.pack()
        confirm_password_entry = tk.Entry(
            self.registration_admin_window, show="*")
        confirm_password_entry.pack()

        # Register Button
        register_button = tk.Button(self.registration_admin_window, text="Register", command=lambda: self.process_administrador_registration(
            name_entry.get(), age_entry.get(), gender_var.get(), dni_entry.get(), password_entry.get(), confirm_password_entry.get()))
        register_button.pack()
        close_buttom = tk.Button(
            self.registration_admin_window, text="Close", command=lambda: self.registration_admin_window.destroy())
        close_buttom.pack()

    def process_administrador_registration(self, name, age, gender, dni, password, confirm_password):
        # Validate the input data and perform the registration logic
        if not name:
            self.show_error_message("Name is required.")
        elif not age.isdigit():
            self.show_error_message(
                "Invalid age. Please enter a valid number.")
        elif not 0 <= int(age) <= 120:
            self.show_error_message(
                "Invalid age. Age must be between 0 and 120.")
        elif gender not in ["Male", "Female", "Other"]:
            self.show_error_message(
                "Invalid gender. Please select a valid option.")
        elif not dni.isdigit():
            self.show_error_message(
                "Invalid DNI. Please enter a valid number.")
        elif not password:
            self.show_error_message("Password is required.")
        elif password != confirm_password:
            self.show_error_message(
                "Passwords do not match. Please enter the same password.")
        else:
            # Perform the administrador registration with the validated data
            self.perform_administrador_registration(
                name, int(age), gender, int(dni), password)

    def perform_administrador_registration(self, name, age, gender, dni, password):
        # TODO: Implement the administrador registration logic with the validated data
        self.show_registration_success()
        admin_created = Administrator(name, age, gender, dni)
        admin_created.set_password(password)
        self.data.set_createdUsers(admin_created)
        self.save_created_users()

        # Close window
        self.registration_admin_window.destroy()

    def log_now(self, log, role):
        self.person = log
        self.role = role
        if self.person_window is None:
            self.person_window = tk.Toplevel(self.root)
            self.person_window.title("Passenger Information")
            self.person_window.geometry("500x500")

            # Name label
            name_label = tk.Label(self.person_window,
                                  text="Name: " + self.person.get_name())
            name_label.pack()

            # Age label
            age_label = tk.Label(self.person_window, text="Age: " +
                                 str(self.person.get_age()))
            age_label.pack()

            # Gender label
            gender_label = tk.Label(
                self.person_window, text="Gender: " + self.person.get_gender())
            gender_label.pack()

            # DNI label
            dni_label = tk.Label(self.person_window, text="DNI: " +
                                 str(self.person.get_dni()))
            dni_label.pack()
        else:
            messagebox.showinfo(
                "Registration", "A registration window is already open.")

        if self.role.lower() == "passenger":
            # Generate Card

            # Name label
            opcionLabel = tk.Label(self.person_window,
                                   text="""
1. Generate Taxi Card.
2. Recharge Taxi Card.
3. Delete Taxi Card.
4. Pay travel.
5. View You Taxi Card.
6. Exit.
""")
            opcionLabel.pack()

            opcion_entry = tk.Entry(self.person_window)
            opcion_entry.pack()

            def handle_selection():
                opcion = opcion_entry.get()
                passengercard = TaxiCard(self.person.get_dni())

                if opcion == '1':
                    # Assuming 'get_dni()' method is defined in the 'Person' class

                    # Assuming 'show_save_success()' is a method to display a success message
                    self.show_save_success()

                    self.person.set_TaxiCard(passengercard)
                    self.save_created_users()

                elif opcion == '2':
                    cash_window = tk.Toplevel(self.root)
                    cash_window.title("Cash on card")
                    cashLabel = tk.Label(
                        cash_window, text="Enter money for charge: ")
                    cashLabel.pack()
                    cash_entry = tk.Entry(cash_window)
                    cash_entry.pack()
                    enter_button = tk.Button(
                        cash_window, text="Enter", command=self.person.rechargeCard(passengercard, cash_entry.get()))
                    enter_button.pack()

                    self.save_created_users()

                    # Perform recharge functionality
                elif opcion == '3':
                    pass
                    # Perform delete functionality
                elif opcion == '4':
                    pass
                    # Perform payment functionality
                elif opcion == '5':
                    view_window = tk.Toplevel(self.root)
                    view_window.title("Taxi Card Information")

                    # Retrieve the passenger's taxi card
                    passengercard = self.person.get_TaxiCard()

                    # Check if the passenger has a taxi card
                    if passengercard is not None:
                        infoLabel = tk.Label(
                            view_window, text=passengercard.__str__())
                        infoLabel.pack()
                    else:
                        infoLabel = tk.Label(
                            view_window, text="No taxi card found for the passenger.")
                        infoLabel.pack()
                    # Perform view functionality
                elif opcion == '6':
                    self.person_window.destroy()
                else:
                    print("Invalid option selected.")

            enter_button = tk.Button(
                self.person_window, text="Enter", command=handle_selection)
            enter_button.pack()

        elif self.role.lower() == "administrator":
            # Add Taxi
            addTaxi_buttom = tk.Button(
                self.person_window, text="Add Taxi", command="")
            addTaxi_buttom.pack()
            # Delete Taxi
            deleteTaxi_buttom = tk.Button(
                self.person_window, text="Delete Taxi", command="")
            deleteTaxi_buttom.pack()
            # Update Taxi
            updateTaxi_buttom = tk.Button(
                self.person_window, text="Update Taxi", command="")
            updateTaxi_buttom.pack()
            # Add Taxi Driver
            addTaxiDriver_buttom = tk.Button(
                self.person_window, text="Add Taxi Driver", command="")
            addTaxiDriver_buttom.pack()
            # Delete Taxi Driver
            deleteTaxiDriver_buttom = tk.Button(
                self.person_window, text="Delete Taxi Driver", command="")
            deleteTaxiDriver_buttom.pack()
            # Update Taxi Driver
            updateTaxiDriver_buttom = tk.Button(
                self.person_window, text="Update Taxi Driver", command="")
            updateTaxiDriver_buttom.pack()
            # Add Passenger
            addPassenger_buttom = tk.Button(
                self.person_window, text="Add Passenger", command="")
            addPassenger_buttom.pack()
            # Delete Passenger
            deletePassenger_buttom = tk.Button(
                self.person_window, text="Delete Passenger", command="")
            deletePassenger_buttom.pack()
            # Update Passenger
            updatePassenger_buttom = tk.Button(
                self.person_window, text="Update Passenger", command="")
            updatePassenger_buttom.pack()

            close_buttom = tk.Button(
                self.person_window, text="Close", command=lambda: self.person_window.destroy())
            close_buttom.pack()
        elif self.role.lower() == "driver":
            # license label
            license_label = tk.Label(self.person_window, text="License: " +
                                     str(self.person.get_license()))
            license_label.pack()
            # Accept Travel
            acceptTravel_buttom = tk.Button(
                self.person_window, text="Aceppt Travel", command="")
            acceptTravel_buttom.pack()
            # Cancel Travel
            cancelTravel_buttom = tk.Button(
                self.person_window, text="Cancel Travel", command="")
            cancelTravel_buttom.pack()
            # Start Travel
            startTravel_buttom = tk.Button(
                self.person_window, text="Start Travel", command="")
            startTravel_buttom.pack()
            # End Travel
            EndTravel_buttom = tk.Button(
                self.person_window, text="End Travel", command="")
            EndTravel_buttom.pack()
            # Update Taxi
            close_buttom = tk.Button(
                self.person_window, text="Close", command=lambda: self.person_window.destroy())
            close_buttom.pack()


if __name__ == '__main__':
    Main()
