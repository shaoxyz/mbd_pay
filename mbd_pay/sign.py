# -*- coding: utf-8 -*-
"""
面包多Pay签名算法实现
Doc: https://doc.mbd.pub/api/qian-ming-suan-fa
"""

from hashlib import md5


def sign(attributes: dict, payjs_key: str) -> str:
    attributes_new = {k: attributes[k] for k in sorted(attributes.keys())}
    sign_str = "&".join(
        [f"{key}={attributes_new[key]}" for key in attributes_new.keys()]
    )
    return md5((sign_str + "&key=" + payjs_key).encode(encoding="utf-8")).hexdigest()


if __name__ == "__main__":
    # 用法示例
    data = {"app_id": "194024590982810", "amount_total": 100,"channel": "h5","description": "312"}

    # 面包多支付 app_key
    key = "920ee68b4e16df01d0cd6b2ca161195d"

    signed = sign(data, key)
    print(signed)
    # assert signed == "8544787ca7f93235a3e6c63b3c14eced"
    print("ok")
