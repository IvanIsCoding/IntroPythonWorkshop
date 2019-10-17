# -*- coding: utf-8 -*-
import sqlite3


class QSCU:
    """Class representing the coffee shop, the interface to access the data."""

    def __init__(self, filename):
        """
        :param filename: the file that contains the SQLite DB.
        :type filename: string
        """

        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()
        self.closed = False

    def setup_db(self):
        """This function initializes the database. 
        It creates the sales tables and inserts the coffe types that are sold.
        
        The database consists of 1 table:
        - sales table: a table listing all the coffees, their prices and their sales
        """

        self.cursor.execute(
            """
        CREATE TABLE sales(
            name text,
            product_id int,
            price int,
            sold int
        ) 
        """
        )

        self.cursor.execute("""INSERT INTO sales VALUES ('Espresso', 1, 2, 0)""")
        self.cursor.execute("""INSERT INTO sales VALUES ('Macchiato', 2, 3, 0)""")
        self.cursor.execute("""INSERT INTO sales VALUES ('Regular Java', 3, 1, 0)""")

        self.conn.commit()

    def sell_item(self, product_id, quantity):
        """Tells the database that a product was sold.

        :param product_id: the identification of the product that was sold
        :type product_id: int
        :param quantity: how many items were sold
        :type quantity: int
        """

        self.cursor.execute(
            """
            UPDATE sales 
            SET sold = sold + $1
            WHERE product_id = $2
            """,
            [quantity, product_id],
        )

        self.conn.commit()

    def get_most_sold(self):
        """Retrieve the most sold item of the coffe shop.

        :returns: list[(string, int)]
        """

        most_sold_row = self.cursor.execute(
            """
            SELECT name, sold
            FROM sales
            ORDER BY sold DESC
            LIMIT 1
            """
        )

        return list(most_sold_row)[0]

    def close(self):
        """Close connection to database"""
        self.cursor.close()
        self.conn.close()
        self.closed = True
