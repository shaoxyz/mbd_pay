# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/18 17:15
@Author  : github.com/shaoxyz
"""
from mbd_pay import Client

c = Client(app_id="**", app_key="**")

print("openid_redirect_url: \n", c.get_openid_redirect_url(target_url="baidu.com"))
print(f"\n{'-'*20}")

print(
    "wx jsapi: \n",
    c.wx_jsapi(
        openid="123", description="321", amount_total=100, callback_url="baidu.com"
    ),
)
print(f"\n{'-'*20}")

print("wx h5: \n", c.wx_h5(description="321", amount_total=100))
print(f"\n{'-'*20}")

print("alipay: \n", c.alipay(url="baidu.com", description="321", amount_total=100))
print(f"\n{'-'*20}")

print("refund: \n", c.refund(order_id="123"))
print(f"\n{'-'*20}")

print("search order: \n", c.search_order(out_trade_no="123"))
