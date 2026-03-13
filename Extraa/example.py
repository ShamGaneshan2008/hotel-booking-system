# Import pandas to read data from CSV files
import pandas

# Import FPDF to create PDF files (receipt)
from fpdf import FPDF

# Read the CSV file that contains article information
# dtype={"id": str} ensures the article ID is treated as a string
df = pandas.read_csv("articles.csv", dtype={"id": str})


# ---------------- ORDER CLASS ----------------
# This class represents an order made by the user
class Order:
    def __init__(self, article_id):
        """
        This constructor runs automatically when an Order object is created.
        It initializes the object with article details.
        """

        # Store the article ID entered by the user
        self.article_id = article_id

        # Get the article name from the CSV file using the article ID
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()

        # Get the article price from the CSV file using the article ID
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def available(self):
        """
        This method checks whether the selected article is available in stock.
        It returns True if stock is greater than 0, otherwise False.
        """

        # Get stock count from the CSV file
        stock = df.loc[df["id"] == self.article_id, "in stock"].squeeze()

        # Return True if stock is available, else False
        return stock > 0


# ---------------- RECEIPT CLASS ----------------
# This class is responsible for generating the PDF receipt
class Receipt:
    def __init__(self, article):
        """
        This constructor receives an Order object and stores it.
        """
        self.article = article  # Store Order object

    def generate(self):
        """
        This method creates a PDF receipt for the ordered article.
        """

        # Create a PDF document (Portrait, millimeters, A4 size)
        pdf = FPDF(orientation="P", unit="mm", format="A4")

        # Add a new page to the PDF
        pdf.add_page()

        # Set font for receipt title
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=0, h=10, txt=f"Receipt No: {self.article.article_id}", ln=1)

        # Set font for article details
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=0, h=10, txt=f"Article Name: {self.article.name}", ln=1)

        # Print article price
        pdf.cell(w=0, h=10, txt=f"Price: {self.article.price}", ln=1)

        # Save the PDF file
        pdf.output("receipt.pdf")


# ---------------- MAIN PROGRAM ----------------

# Print all article data (just to verify data is loaded correctly)
print(df)

# Ask user to enter the article ID they want to buy
article_id = input("Enter the article ID to buy: ")

# Create an Order object using the entered article ID
article = Order(article_id)

# Check if the article is available in stock
if article.available():
    # Create Receipt object using the Order object
    receipt = Receipt(article)

    # Generate the PDF receipt
    receipt.generate()

    print("Receipt generated successfully!")

else:
    # Print message if the article is not available
    print("There is no such article in stock.")
