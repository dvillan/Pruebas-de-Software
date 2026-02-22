"""
Definitions for necessary classes of reservation system
"""
from dataclasses import dataclass


@dataclass
class Hotel:
    """
    Docstring for Hotel
    """
    def __init__(self, hotel_id: str, name: str, rooms: int,
                 available_rooms: int):
        self.id = hotel_id
        self.name = name
        self.rooms = rooms
        self.available_rooms = available_rooms

    def asdict(self) -> dict:
        """
        Docstring for asdict

        :return: Description
        :rtype: dict
        """
        return {self.id: {"name": self.name, "rooms": self.rooms,
                          "available_rooms": self.available_rooms}}


@dataclass
class Customer:
    """
    Docstring for Customer
    """
    def __init__(self, cust_id: str, name: str, cellphone: str):
        self.id = cust_id
        self.name = name
        self.cellphone = cellphone

    def asdict(self) -> dict:
        """
        Docstring for asdict

        :return: Description
        :rtype: dict
        """
        return {self.id: {"name": self.name, "cellphone": self.cellphone}}


@dataclass
class Reservation:
    """
    Docstring for Reservation
    """
    def __init__(self, rsv_id: str, hotel_id: str, customer_id: str):
        self.id = rsv_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id

    def asdict(self) -> dict:
        """
        Docstring for asdict

        :return: Description
        :rtype: dict
        """
        return {self.id: {"hotel_id": self.hotel_id,
                          "customer_id": self.customer_id}}
