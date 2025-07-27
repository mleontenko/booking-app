import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel():
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id        

    def book(self):
        """
        Book the hotel if available by changin availability to no
        """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """
        Check if the hotel is available for booking.
        """
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket():
    def __init__(self, customer_name, hotel_object):
        pass

    def generate(self):
        content= f"Name of the customer: hotel:"
        print(content)


print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")