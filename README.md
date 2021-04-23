# mbd-pay


[面包多Pay文档](https://doc.mbd.pub/)
- 封装签名、请求参数与返回值，具体结构参考 [types.py](https://github.com/shaoxyz/mbd_pay/blob/dev/mbd_pay/types.py)
- 支持所有[requests](https://docs.python-requests.org/en/master/)库执行请求时支持的参数，比如 `timeout`


## Quickstart

Install using `pip`:

```shell
$ pip install mbd-pay
```
## Example
```python
from mbd_pay import Client

c = Client(app_id="**", app_key="**")

# 生成获取openid的链接
print("openid_redirect_url: \n", c.get_openid_redirect_url(target_url="baidu.com"))

print(
    "wx jsapi: \n",
    c.wx_jsapi(
        openid="123", description="321", amount_total=100, callback_url="baidu.com"，
    ),
)

print("wx h5: \n", c.wx_h5(description="321", amount_total=100))

print("alipay: \n", c.alipay(url="baidu.com", description="321", amount_total=100))

print("refund: \n", c.refund(order_id="123"))

print("search order: \n", c.search_order(out_trade_no="123"))

```

## Reference
```python
def _handle_req(self, req) -> dict:
    """
    `req` Model to dict, and add sign | 过滤空值、签名、构建请求体
    """
    req = req.dict(exclude_none=True)
    req.update(app_id=self.app_id)
    req.update(sign=sign(req, self.app_key))
    return req
        
def _post(self, _url: str, req, **kwargs):
    """
    build request body for POST, split out requests' kwargs
    :param url: url
    :param req: see ***Req in types.py
    :param kwargs: req + `requests.post`'s kwargs, e.g. timeout=5
    :return:
    """
    body = self._handle_req(req)

    # split out requests' kwargs | 抽离出所有面包多Pay以外的参数，并传递给requests执行实际请求
    other_kwargs = {
        i: kwargs[i] for i in kwargs.keys() if i not in req.__fields_set__
    }

    return requests.post(_url, json=body, **other_kwargs).json()
        
def wx_jsapi(self, **kwargs) -> WeChatJSApiRes:
    """
    see：https://doc.mbd.pub/api/wei-xin-zhi-fu
    :param kwargs: WeChatJSApiReq required fields
        and optional `requests.post`'s kwargs, e.g. timeout=5
    :return: WeChatJSApiRes
    """
    req = WeChatJSApiReq(**kwargs)  # 用kwarg实例化一个WeChatJSApiReq对象
    api = f"{self.domain}/release/wx/prepay"
    res = self._post(api, req, **kwargs)

    return WeChatJSApiRes(**res)  # 用返回值实例化一个WeChatJSApiRes对象
```

## Thanks
  - [Requests](https://docs.python-requests.org/en/master/)
  - [Pydantic](https://pydantic-docs.helpmanual.io/)

## Todos

 - WebHooks

License
----

MIT


**Hell Yeah!**

