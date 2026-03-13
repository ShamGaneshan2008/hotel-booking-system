import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_secure = pandas.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book the hotel by changing availability"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        return availability == "yes"


class ReservationTicket:
    def __init__(self, hotel_object, customer_name):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank You for your reservation!
        Here are the booking details:

        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "holder": holder,
            "cvc": cvc
        }

        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_pass):
        password_series = df_card_secure.loc[
            df_card_secure["number"] == self.number, "password"
        ]

        if password_series.empty:
            return False

        password = password_series.iloc[0]
        return password == given_pass


print(df)

hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():

    credit_card = SecureCreditCard(number="7394826150938472")

    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):

        if credit_card.authenticate(given_pass="abc1234"):

            hotel.book()

            name = input("Enter your name: ")

            reservation_ticket = ReservationTicket(
                customer_name=name,
                hotel_object=hotel
            )

            print(reservation_ticket.generate())

        else:
            print("Credit Card authentication failed!")

    else:
        print("There is an error in your payment. Try again.")

else:
    print("The hotel is not available")