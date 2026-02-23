"""
Testing script for reservation_system.py
"""

import unittest
from unittest.mock import MagicMock
from reservation_system import ReservationManager, \
                               CustomerManager, \
                               HotelManager


class TestReservationManager(unittest.TestCase):
    """
    Test suite for reservation manager
    """
    def setUp(self):
        self.manager = ReservationManager()
        self.manager.file_manager = MagicMock()

        # Sample fake data
        self.hotels = {
            "1": {"name": "Hilton", "rooms": 10, "available_rooms": 5}
        }

        self.customers = {
            "1": {"name": "David", "cellphone": "1234567890"}
        }

        self.reservations = {}

    def test_create_reservation_success(self):
        """
        Test case: Reservation creation success
        """
        self.manager.file_manager.read_file.side_effect = [
            self.hotels,
            self.customers,
            self.reservations
        ]

        self.manager.create_reservation("Hilton", "David")

        # available_rooms should decrease
        self.assertEqual(self.hotels["1"]["available_rooms"], 4)

        # update should be called twice
        self.assertEqual(self.manager.file_manager.update.call_count, 2)

    def test_create_reservation_no_rooms(self):
        """
        Test case: No reservation, no rooms available
        """
        self.hotels["1"]["available_rooms"] = 0

        self.manager.file_manager.read_file.side_effect = [
            self.hotels,
            self.customers
        ]

        self.manager.create_reservation("Hilton", "David")
        self.assertEqual(self.manager.file_manager.update.call_count, 0)

    def test_create_reservation_invalid_hotel(self):
        """
        Test case: Reservation creation,
        hotel not found in system
        """
        self.manager.file_manager.read_file.side_effect = [
            self.hotels,
            self.customers
        ]

        self.manager.create_reservation("Marriot", "David")
        self.assertEqual(self.manager.file_manager.update.call_count, 0)

    def test_create_reservation_invalid_customer(self):
        """
        Test case: Reservation creation,
        customer not found in system
        """
        self.manager.file_manager.read_file.side_effect = [
            self.hotels,
            {}
        ]

        self.manager.create_reservation("Hilton", "Ale")
        self.assertEqual(self.manager.file_manager.update.call_count, 0)

    def test_cancel_reservation_success(self):
        """
        Test case: Reservation cancelation success
        """
        reservations = {
            "1": {"hotel_id": "1", "customer_id": "1"}
        }

        self.manager.file_manager.read_file.side_effect = [
            reservations,
            self.hotels
        ]

        self.manager.cancel_reservation("1")

        # room should increase
        self.assertEqual(self.hotels["1"]["available_rooms"], 6)
        self.assertEqual(self.manager.file_manager.update.call_count, 2)

    def test_cancel_reservation_not_found(self):
        """
        Test case: Cancel reservation,
        reservation not found
        """
        self.manager.file_manager.read_file.side_effect = [
            {},
            self.hotels
        ]

        self.manager.cancel_reservation("99")
        self.assertEqual(self.manager.file_manager.update.call_count, 0)

    def test_search_reservation_found(self):
        """
        Test case: Reservation retrieval success
        """
        reservations = {
            "1": {"hotel_id": "1", "customer_id": "1"}
        }

        self.manager.file_manager.read_file.return_value = reservations
        result = self.manager.search_reservation("1")
        self.assertIsNotNone(result)
        self.assertEqual(result["hotel_id"], "1")

    def test_search_reservation_not_found(self):
        """
        Test case: Reservation retrieval,
        reservation not found
        """
        self.manager.file_manager.read_file.return_value = {}
        result = self.manager.search_reservation("99")
        self.assertIsNone(result)


class TestHotelManager(unittest.TestCase):
    """
    Test suite for hotel manager
    """
    def setUp(self):
        self.manager = HotelManager()
        self.manager.file_manager = MagicMock()

        self.hotels = {
            "1": {"name": "Hilton", "rooms": 10, "available_rooms": 5}
        }

    def test_create_hotel_success_existing_file(self):
        """
        Test case: Hotel creation success
        """
        self.manager.file_manager.read_file.return_value = self.hotels
        self.manager.create_hotel("Marriot", 20, 10)
        self.manager.file_manager.update.assert_called_once()

    def test_delete_hotel_success(self):
        """
        Test case: Hotel deletion success
        """
        self.manager.file_manager.read_file.return_value = self.hotels
        self.manager.delete_hotel("1")
        self.manager.file_manager.update.assert_called_once()

    def test_delete_hotel_not_found(self):
        """
        Test case: Hotel deletion, hotel
        not found
        """
        self.manager.file_manager.read_file.return_value = self.hotels
        self.manager.delete_hotel("99")
        self.manager.file_manager.update.assert_not_called()

    def test_modify_hotel_success(self):
        """
        Test case: Hotel modification success
        """
        self.manager.file_manager.read_file.return_value = self.hotels
        self.manager.modify_hotel({"1": {"name": "Updated",
                                         "rooms": 10,
                                         "available_rooms": 5}})
        self.manager.file_manager.update.assert_called_once()

    def test_get_info_found(self):
        """
        Test case: Hotel info retrieval success
        """
        self.manager.file_manager.read_file.return_value = self.hotels
        result = self.manager.get_info("Hilton")
        self.assertEqual(result, "1")

    def test_get_info_not_found(self):
        """
        Test case: Hotel info retrieval,
        information not found
        """
        self.manager.file_manager.read_file.return_value = self.hotels
        result = self.manager.get_info("Unknown")
        self.assertIsNone(result)


class TestCustomerManager(unittest.TestCase):
    """
    Test suite for customer manager
    """
    def setUp(self):
        self.manager = CustomerManager()
        self.manager.file_manager = MagicMock()

        self.customers = {
            "1": {"name": "David", "cellphone": "123456"}
        }

    def test_create_customer_success_existing_file(self):
        """
        Test case: Customer creation success
        """
        self.manager.file_manager.read_file.return_value = self.customers
        self.manager.create_customer("Ale", "999999")
        self.manager.file_manager.update.assert_called_once()

    def test_delete_customer_success(self):
        """
        Test case: Customer deletion success
        """
        self.manager.file_manager.read_file.return_value = self.customers
        self.manager.delete_customer("1")
        self.manager.file_manager.update.assert_called_once()

    def test_delete_customer_not_found(self):
        """
        Test case: Customer deletion, customer
        not found
        """
        self.manager.file_manager.read_file.return_value = self.customers
        self.manager.delete_customer("99")
        self.manager.file_manager.update.assert_not_called()

    def test_modify_customer_success(self):
        """
        Test case: Customer modification success
        """
        self.manager.file_manager.read_file.return_value = self.customers
        self.manager.modify_customer({"1": {"name": "Updated",
                                            "cellphone": "000"}})
        self.manager.file_manager.update.assert_called_once()

    def test_get_info_found(self):
        """
        Test case: Customer retrieval success
        """
        self.manager.file_manager.read_file.return_value = self.customers
        result = self.manager.get_info("David")
        self.assertEqual(result, "1")

    def test_get_info_not_found(self):
        """
        Test case: Customer retrieval,
        customer not found
        """
        self.manager.file_manager.read_file.return_value = self.customers
        result = self.manager.get_info("Unknown")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
