"""
Main Script for reservation system
"""
import json
from models import Hotel, Customer, Reservation


class ReservationManager:
    """
    User Interaction for create, cancel and
    search a reservation
    """
    def __init__(self):
        self.rsv_id = 0
        self.reservation_filename = r"data\reservations.json"
        self.hotel_filename = r"data\hotels.json"
        self.customer_filename = r"data\customers.json"
        self.file_manager = FileManager()

    def create_reservation(self, hotel_name: str, customer_name: str):
        """
        Creates a new reservation in the system

        :param hotel_name: Name of the hotel
        :type hotel_name: str
        :param customer_name: Customer name
        :type customer_name: str
        """

        try:
            hotels = self.file_manager.read_file(self.hotel_filename)
            customers = self.file_manager.read_file(self.customer_filename)
        except json.JSONDecodeError:
            print("Information not found")
            return

        hotel_id = None
        for h_id in hotels.keys():
            if hotel_name == hotels[h_id]["name"]:
                hotel_id = h_id
                break

        if not hotel_id:
            print(f"Hotel {hotel_name} not found")
            return

        if hotels[hotel_id]["available_rooms"] <= 0:
            print("No rooms available")
            return

        customer_id = None
        for c_id in customers:
            if customer_name == customers[c_id]["name"]:
                customer_id = c_id
                break

        if not customer_id:
            print(f"Customer {customer_name} not found")
            return

        self.rsv_id += 1
        new_rsv = Reservation(rsv_id=self.rsv_id, hotel_id=hotel_id,
                              customer_id=customer_id)

        try:
            reservations = self.file_manager.read_file(
                self.reservation_filename)
            reservations.update(new_rsv.asdict())
        except json.JSONDecodeError:
            reservations = new_rsv.asdict()

        hotels[hotel_id]["available_rooms"] -= 1

        self.file_manager.update(self.reservation_filename, reservations)
        self.file_manager.update(self.hotel_filename, hotels)

        print(f"Reservation {self.rsv_id} successfully created")

    def cancel_reservation(self, reservation_id: str):
        """
        Cancels an existing reservation

        :param reservation_id: ID to cancel
        :type reservation_id: str
        """
        try:
            reservations = self.file_manager.read_file(
                self.reservation_filename)
            hotels = self.file_manager.read_file(self.hotel_filename)
        except json.JSONDecodeError:
            print("No reservation data found")
            return

        if reservation_id not in reservations:
            print(f"Reservation with id {reservation_id} not found")
            return

        hotel_id = reservations[reservation_id]["hotel_id"]
        del reservations[reservation_id]
        hotels[hotel_id]["available_rooms"] += 1

        self.file_manager.update(self.reservation_filename, reservations)
        self.file_manager.update(self.hotel_filename, hotels)

        print(f"Reservation with ID: {reservation_id} successfully cancelled")

    def search_reservation(self, reservation_id: str):
        """
        Search in the system for a reservation

        :param reservation_id: ID to search
        :type reservation_id: str
        """
        try:
            reservations = self.file_manager.read_file(
                self.reservation_filename)
        except json.JSONDecodeError:
            print("No reservation data found")
            return None
        if reservation_id in reservations:
            print(f"Reservation ID: {reservation_id}"
                  f"Hotel ID:"
                  f"Customer ID: \n")
            return reservations[reservation_id]

        print(f"Reservation with ID: {reservation_id} not found")
        return None


class HotelManager:
    """
    User Interaction for creating, deleting, modifying
    and retrieving hotel information
    """
    def __init__(self):
        self.id = 0
        self.hotel_filename = r"data\hotels.json"
        self.file_manager = FileManager()

    def create_hotel(self, h_name: str, h_rooms: int, h_available: int):
        """
        Docstring for create_hotel

        :param h_name: Hotel name
        :type h_name: str
        :param h_rooms: Quantity of rooms
        :type h_rooms: int
        :param h_available: Quantity of rooms available
        :type h_available: int
        """
        self.id += 1
        new_hotel = Hotel(hotel_id=self.id, name=h_name,
                          rooms=h_rooms, available_rooms=h_available)

        try:
            hotel_info = self.file_manager.read_file(self.hotel_filename)
            hotel_info.update(new_hotel.asdict())
            self.file_manager.update(self.hotel_filename, hotel_info)

        except json.JSONDecodeError:
            print(f"{self.hotel_filename} is empty, saving new data")
            self.file_manager.update(self.hotel_filename, new_hotel.asdict())

        print(f"Hotel with id {self.id} successfully created")

    def delete_hotel(self, h_id: str):
        """
        Delete an hotel from the system

        :param h_id: Hotel ID
        """
        try:
            hotel_info = self.file_manager.read_file(self.hotel_filename)
            del hotel_info[h_id]
            self.file_manager.update(self.hotel_filename, hotel_info)
            print(f"Hotel with id {h_id} successfully removed")

        except KeyError:
            print(f"Hotel with id {h_id} not found")

    def modify_hotel(self, char_dict: dict):
        """
        Modifies the information from an existing hotel

        :param char_dict: Information to modify
        :type char_dict: dict
        """
        try:
            hotel_info = self.file_manager.read_file(self.hotel_filename)
            hotel_info.update(char_dict)
            self.file_manager.update(self.hotel_filename, hotel_info)
        except json.JSONDecodeError:
            print("No information found")

    def get_info(self, h_name: str) -> str:
        """
        Get information from an hotel

        :param h_name: Hotel name
        :type h_name: str
        :return: Hotel ID
        :rtype: str
        """
        try:
            hotel_info = self.file_manager.read_file(self.hotel_filename)
            for hotel_id in hotel_info.keys():
                if h_name in hotel_info[hotel_id].values():
                    print(f"\nHotel: {h_name} \n Hotel_ID: {hotel_id} \n"
                          f" Rooms: {hotel_info[hotel_id]['rooms']} \n"
                          f" Available Rooms: "
                          f"{hotel_info[hotel_id]['available_rooms']}\n")
                    return hotel_id
            print(f"Hotel {h_name} not found")
            return None

        except json.JSONDecodeError:
            print("No information found")
            return None


class CustomerManager:
    """
    User Interaction for creating, deleting,
    and modifying customer information
    """
    def __init__(self):
        self.id = 0
        self.customer_filename = r"data\customers.json"
        self.file_manager = FileManager()

    def create_customer(self, c_name: str, c_cellphone: str):
        """
        Create new customer in system

        :param c_name: Customer name
        :type c_name: str
        :param c_cellphone: Customer cellphone
        :type c_cellphone: str
        """
        self.id += 1
        new_customer = Customer(cust_id=str(self.id), name=c_name,
                                cellphone=c_cellphone)

        try:
            customer_info = self.file_manager.read_file(self.customer_filename)
            customer_info.update(new_customer.asdict())
            self.file_manager.update(self.customer_filename, customer_info)

        except json.JSONDecodeError:
            print(f"{self.customer_filename} is empty, saving new data")
            self.file_manager.update(self.customer_filename,
                                     new_customer.asdict())

        print(f"Customer with id {new_customer.id} successfully created")

    def delete_customer(self, c_id: str):
        """
        Delete customer from system

        :param c_id: Customer ID
        :type c_id: str
        """
        try:
            customer_info = self.file_manager.read_file(self.customer_filename)
            del customer_info[c_id]
            self.file_manager.update(self.customer_filename, customer_info)
            print(f"Customer with id {c_id} successfully removed")

        except KeyError:
            print(f"Customer with id {c_id} not found")

    def modify_customer(self, char_dict: dict):
        """
        Modifies the information from an existing customer

        :param char_dict: Information to modify
        :type char_dict: dict
        """
        try:
            customer_info = self.file_manager.read_file(self.customer_filename)
            customer_info.update(char_dict)
            self.file_manager.update(self.customer_filename, customer_info)
            print("Customer updated")

        except json.JSONDecodeError:
            print("No information found")

    def get_info(self, c_name: str) -> str:
        """
        Get information from a customer

        :param c_name: Customer name
        :type c_name: str
        :return: Customer ID
        :rtype: str
        """
        try:
            customer_info = self.file_manager.read_file(self.customer_filename)
            for cust_id in customer_info.keys():
                if c_name in customer_info[cust_id].values():
                    print(f"\nCustomer: {c_name} \n Customer ID: {cust_id} \n"
                          f"Cellphone: {customer_info[cust_id]['cellphone']}")
                    return cust_id
            print(f"Customer {c_name} not found")
            return None

        except json.JSONDecodeError:
            print("No information found")
            return None


class FileManager:
    """
    Class that manages access to the reservation system files
    """
    def read_file(self, input_filepath: str) -> dict:
        """
        Read specific system file

        :param self: Description
        :param input_filepath: Description
        :type input_filepath: str
        :return: Description
        :rtype: dict
        """
        with open(input_filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def update(self, input_filepath: str, input_dict: dict):
        """
        Update an specific system file

        :param self: Description
        :param input_filepath: Description
        :type input_filepath: str
        :param input_dict: Description
        :type input_dict: dict
        """
        with open(input_filepath, "w", encoding="utf-8") as file:
            json.dump(input_dict, file)


if __name__ == "__main__":

    # Initialize system managers
    rsv_manager = ReservationManager()
    hotel_manager = HotelManager()
    cs_manager = CustomerManager()

    # Create new customers
    cs_manager.create_customer("David", "3339663016")
    cs_manager.create_customer("Citlali", "2496874512")

    # Get info from existing customer
    cs_manager.get_info("David")

    # Delete non-existing customer
    cs_manager.delete_customer(c_id="5")

    # Modify existing customer ID
    cs_manager.modify_customer({"1": {"name": "Ale",
                                      "cellphone": "7896321563"}})

    # Create new hotels
    hotel_manager.create_hotel("Hilton", 25, 25)
    hotel_manager.create_hotel("Marriot", 100, 5)

    # Delete existing hotel
    hotel_manager.delete_hotel(h_id="2")

    # Delete non-existing hotel
    hotel_manager.delete_hotel(h_id="32")

    # Get info from existing hotel
    hotel_manager.get_info("Hilton")

    # Get info from an non-existing hotel
    hotel_manager.get_info("Barcelo")

    # Create new reservation
    rsv_manager.create_reservation(hotel_name="Hilton",
                                   customer_name="Citlali")

    rsv_manager.create_reservation(hotel_name="Hilton",
                                   customer_name="Ale")

    # Non-existing hotel
    rsv_manager.create_reservation("Marriot", "David")

    # Non-existing reservation
    rsv_manager.search_reservation("123")

    print("Successful")
