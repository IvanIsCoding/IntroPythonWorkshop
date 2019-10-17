# -*- coding: utf-8 -*-
import unittest
from qscu import QSCU


class TestQSCU(unittest.TestCase):
    def setup_test(self):
        """Instantiate a databse in memory for the test."""
        self.shop = QSCU(":memory:")
        self.shop.setup_db()

    def test_no_sold_items(self):
        """Test if the quantity of items is set to zero before any item is sold"""
        self.setup_test()

        rows = self.shop.cursor.execute(
            """
            SELECT name, sold
            FROM sales
        """
        )

        for name, sold in rows:
            self.assertEqual(sold, 0)

    def test_sell_item(self):
        """Test if the sell item function correctly updates the database"""
        self.setup_test()

        expected_result = {1: 4, 2: 5}

        self.shop.sell_item(1, 1)
        self.shop.sell_item(2, 2)
        self.shop.sell_item(1, 3)
        self.shop.sell_item(2, 3)

        rows = self.shop.cursor.execute(
            """
            SELECT product_id, sold
            FROM sales
        """
        )

        for product_id, sold in rows:
            if product_id in expected_result:
                self.assertEqual(sold, expected_result[product_id])
            else:
                self.assertEqual(sold, 0)

    def test_most_sold(self):
        """Test if the get_most_sold functions returns the most sold item"""
        self.setup_test()

        # Case when no item has been sold: it's ok if we return any, but it must tell sold 0 times
        self.assertEqual(self.shop.get_most_sold()[1], 0)

        # Another case: every item has been sold one time
        self.shop.sell_item(1, 3)
        self.shop.sell_item(2, 5)
        self.shop.sell_item(3, 2)

        self.assertEqual(self.shop.get_most_sold(), ("Macchiato", 5))

        # More elaborate case: does our function work when update values again?
        self.shop.sell_item(1, 5)
        self.shop.sell_item(2, 2)
        self.assertEqual(self.shop.get_most_sold(), ("Espresso", 8))


if __name__ == "__main__":
    unittest.main()
