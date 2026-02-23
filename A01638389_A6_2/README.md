# Reservation system 

David Emmanuel Villanueva Martinez 

This project is intended to create a backend architectire for a reservation system, the system should allow: 

**Hotel functionalities**
- Create hotel 
- Delete hotel
- Display hotel information
- Modify hotel information

**Customer functionalities**
- Create customer
- Delete customer
- Display customer information
- Modify customer information

**Reservation functionalities**
- Create a reservation
- Cancel a reservation

It uses JSON files to save information, with the intention of mimic the behavior of a database NoSQL

## Usage 

### Initialize class managers

First of all you need to initialize all class managers, this allows the interaction for the reservation system functionalities

```python
rsv_manager = ReservationManager()
hotel_manager = HotelManager()
cs_manager = CustomerManager()
```

### Customer Interaction
#### Create new customer

```python
cs_manager.create_customer(name, cellphone)
```

#### Delete an existing customer

```python
cs_manager.delete_customer(customer_id)
```

#### Modify/Get customer information

```python
cs_manager.modify_customer(customer_info)
```

### Hotel Interaction
#### Create new hotel

```python
hotel_manager.create_hotel(name, total_rooms, available_rooms)
```

#### Delete an hotel

```python
hotel_manager.delete_hotel(hotel_id)
```

#### Modify/Get hotel information

```python
hotel_manager.get_info(hotel_name)
```

### Reservation Interaction
#### Create new reservation

```python
rsv_manager.create_reservation(hotel_name, customer_name)
```

#### Cancel a reservation

```python
rsv_manager.cancel_reservation(reservation_id)
```

#### Search for a reservation

```
rsv_manager.search_reservation(reservation_id)
```

## Testing 

This project uses unittest python module to validate the behavior of the structure developed, you can run tests with:  

```bash
uv run <test_file>
```

Available test files: 

- reservation_system_test.py
- models_test.py
