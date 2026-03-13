import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:

    watermark = "Real Estate Company"

    def __init__(self, hotel_id):

        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):

        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):

        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        return availability == "yes"

    @classmethod
    def get_hotel_count(cls, data):

        return len(data)

    def __eq__(self, other):

        return self.hotel_id == other.hotel_id


class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):

    def __init__(self, customer_name, hotel_object):

        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):

        content = f"""
        Thank you for your reservation!

        Name: {self.the_customer_name}
        Hotel Name: {self.hotel.name}
        """

        return content

    @property
    def the_customer_name(self):

        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):

        return amount * 2


class DigitalTicket(Ticket):

    def generate(self):

        return "Hello this is a digital ticket"

    def download(self):

        print("Downloading ticket...")