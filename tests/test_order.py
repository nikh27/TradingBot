# # File: tests/test_orders.py
# import unittest
# from unittest.mock import MagicMock
from core.orders import place_order
# from binance.enums import SIDE_BUY, ORDER_TYPE_MARKET


# class TestOrderPlacement(unittest.TestCase):

#     def setUp(self):
#         # Create a mock client
#         self.mock_client = MagicMock()
#         self.mock_client.futures_create_order = MagicMock(return_value={"status": "FILLED"})

#     def test_market_order(self):
#         result = place_order(
#             client=self.mock_client,
#             symbol="BTCUSDT",
#             side="BUY",
#             order_type="MARKET",
#             quantity=0.01
#         )
#         self.assertEqual(result["status"], "FILLED")
#         self.mock_client.futures_create_order.assert_called_once_with(
#             symbol="BTCUSDT",
#             side=SIDE_BUY,
#             quantity=0.01,
#             type=ORDER_TYPE_MARKET
#         )

#     def test_invalid_order_type(self):
#         with self.assertRaises(ValueError):
#             place_order(
#                 client=self.mock_client,
#                 symbol="BTCUSDT",
#                 side="BUY",
#                 order_type="INVALID",
#                 quantity=0.01
#             )


# if __name__ == '__main__':
#     unittest.main()


from core import client, orders, utils
print('haaha done')