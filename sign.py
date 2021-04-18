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
    data = {"app_id": "12345", "amount_total": 1, "out_trade_no": "123123123123"}

    # 面包多支付 app_key
    key = "xxxxxxxxxxx"

    signed = sign(data, key)
    assert signed == "8544787ca7f93235a3e6c63b3c14eced"
    print("ok")
