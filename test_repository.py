from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from app.database import initialize_database
from app.repository import (
    create_order,
    dashboard_summary,
    get_order,
    list_categories,
    list_products,
    update_order_status,
)


class RepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._old_db_path = os.environ.get("MAXWAY_DB_PATH")
        self._tmpdir = tempfile.TemporaryDirectory()
        os.environ["MAXWAY_DB_PATH"] = str(Path(self._tmpdir.name) / "maxway-test.sqlite3")
        initialize_database()

    def tearDown(self) -> None:
        if self._old_db_path is None:
            os.environ.pop("MAXWAY_DB_PATH", None)
        else:
            os.environ["MAXWAY_DB_PATH"] = self._old_db_path
        self._tmpdir.cleanup()

    def test_seed_data_is_available(self) -> None:
        categories = list_categories()
        products = list_products()

        self.assertGreaterEqual(len(categories), 6)
        self.assertGreaterEqual(len(products), 10)
        self.assertTrue(any(product["is_popular"] for product in products))

    def test_order_flow_calculates_totals_and_updates_status(self) -> None:
        products = list_products()
        first_product = products[0]

        order = create_order(
            {
                "customer_name": "Ali Valiyev",
                "phone": "+998 90 123 45 67",
                "address": "Toshkent, Chilonzor 7",
                "payment_method": "cash",
                "delivery_type": "delivery",
                "items": [{"product_id": first_product["id"], "quantity": 2}],
            }
        )

        self.assertEqual(order["status"], "new")
        self.assertEqual(order["subtotal"], first_product["price"] * 2)
        self.assertEqual(order["delivery_fee"], 15000)
        self.assertEqual(len(order["items"]), 1)

        updated_order = update_order_status(order["id"], {"status": "preparing"})
        self.assertEqual(updated_order["status"], "preparing")

        loaded_order = get_order(order["id"])
        self.assertEqual(loaded_order["status"], "preparing")
        self.assertGreaterEqual(len(loaded_order["history"]), 2)

        dashboard = dashboard_summary()
        self.assertEqual(dashboard["orders_count"], 1)
        self.assertGreater(dashboard["revenue"], 0)


if __name__ == "__main__":
    unittest.main()
