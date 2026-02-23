"""
Testing script for models.py
"""

import unittest
from models import Hotel, Reservation, Customer


class TestHotel(unittest.TestCase):
    """
    Test suite for Hotel class
    """
    def setUp(self):
        """
        Initialize Hotel class for test cases
        """
        self.hotel = Hotel("H1", "Hilton", 100, 80)

    def test_attributes(self):
        """
        Test correct attribute assignment
        """
        self.assertEqual(self.hotel.id, "H1")
        self.assertEqual(self.hotel.name, "Hilton")
        self.assertEqual(self.hotel.rooms, 100)
        self.assertEqual(self.hotel.available_rooms, 80)


    def test_dict_return(self):
        """
        Test correct returned dictionary
        """
        expected = {"H1": {"name": "Hilton", "rooms": 100,
                           "available_rooms": 80}}
        self.assertEqual(self.hotel.asdict(), expected)


class TestReservation(unittest.TestCase):
    """
    Test suite for Reservation class
    """
    def setUp(self):
        """
        Initialize Reservation object for test cases
        """
        self.reservation = Reservation(rsv_id="123", hotel_id="H1",
                                       customer_id="D1")

    def test_attributes(self):
        """
        Test correct attribute assignment
        """
        self.assertEqual(self.reservation.id, "123")
        self.assertEqual(self.reservation.hotel_id, "H1")
        self.assertEqual(self.reservation.customer_id, "D1")

    def test_dict_return(self):
        """
        Test returned dictionary
        """
        expected = {"123": {"hotel_id": "H1", "customer_id": "D1"}}
        self.assertEqual(self.reservation.asdict(), expected)


class TestCustomer(unittest.TestCase):
    """
    Test suite for Customer class
    """
    def setUp(self):
        """
        Initialize Customer object for test cases
        """
        self.customer = Customer(cust_id="D1", name="David Villanueva",
                                 cellphone="4526789512")

    def test_attributes(self):
        """
        Test correct attribute assignment
        """
        self.assertEqual(self.customer.id, "D1")
        self.assertEqual(self.customer.name, "David Villanueva")
        self.assertEqual(self.customer.cellphone, "4526789512")

    def test_dict_return(self):
        """
        Test returned dictionary
        """
        expected = {"D1": {"name": "David Villanueva",
                           "cellphone": "4526789512"}}
        self.assertEqual(self.customer.asdict(), expected)


if __name__ == "__main__":
    unittest.main()
