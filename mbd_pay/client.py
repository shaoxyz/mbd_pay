# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/18 16:26
@Author  : github.com/shaoxyz
"""
import urllib.parse

import requests
from mbd_pay.sign import sign
from mbd_pay.types import (
    SearchOrderReq,
    AliPayRes,
    AliPayReq,
    WeChatH5Req,
    WeChatH5Res,
    WeChatJSApiRes,
    WeChatJSApiReq,
    GetOpenIdReq,
    SearchOrderRes,
    RefundReq,
    RefundRes,
)


class Client:
    """
    面包多支付客户端
    """

    def __init__(self, app_id: str, app_key: str, domain="https://api.mianbaoduo.com"):

        self.app_id = app_id
        self.app_key = app_key
        self.domain = domain

    def _handle_req(self, req) -> dict:
        """
        `req` Model to dict, and add sign
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

        # split out requests' kwargs
        other_kwargs = {
            i: kwargs[i] for i in kwargs.keys() if i not in req.__fields_set__
        }

        return requests.post(_url, json=body, **other_kwargs).json()

    def get_openid_redirect_url(self, **kwargs) -> str:
        """
        see：https://doc.mbd.pub/api/huo-qu-yong-hu-openid
        :param kwargs: GetOpenIdReq required fields
        :return: redirect_url
        """
        req = GetOpenIdReq(**kwargs)
        base_url = "https://mbd.pub/openid"
        params = self._handle_req(req)

        return f"{base_url}?{urllib.parse.urlencode(params)}"

    def wx_jsapi(self, **kwargs) -> WeChatJSApiRes:
        """
        see：https://doc.mbd.pub/api/wei-xin-zhi-fu
        :param kwargs: WeChatJSApiReq required fields
            and optional `requests.post`'s kwargs, e.g. timeout=5
        :return: WeChatJSApiRes
        """
        req = WeChatJSApiReq(**kwargs)
        api = f"{self.domain}/release/wx/prepay"
        res = self._post(api, req, **kwargs)

        return WeChatJSApiRes(**res)

    def wx_h5(self, **kwargs) -> WeChatH5Res:
        """
        see：https://doc.mbd.pub/api/wei-xin-h5-zhi-fu
        :param kwargs: WeChatH5Req required fields
            and optional `requests.post`'s kwargs, e.g. timeout=5
        :return: WeChatH5Res
        """
        req = WeChatH5Req(**kwargs)
        api = f"{self.domain}/release/wx/prepay"
        res = self._post(api, req, **kwargs)

        return WeChatH5Res(**res)

    def alipay(self, **kwargs) -> AliPayRes:
        """
        see：https://doc.mbd.pub/api/zhi-fu-bao-zhi-fu
        :param kwargs: AliPayReq required fields
            and optional `requests.post`'s kwargs, e.g. timeout=5
        :return: AliPayRes
        """
        req = AliPayReq(**kwargs)
        api = f"{self.domain}/release/alipay/pay"
        res = self._post(api, req, **kwargs)

        return AliPayRes(**res)

    def refund(self, **kwargs) -> RefundRes:
        """
        see: https://doc.mbd.pub/api/tui-kuan
        :param kwargs: RefundReq required fields
            and optional `requests.post`'s kwargs, e.g. timeout=5
        :return: RefundRes
        """
        req = RefundReq(**kwargs)
        api = f"{self.domain}/release/main/refund"
        res = self._post(api, req, **kwargs)
        return RefundRes(**res)

    def search_order(self, **kwargs) -> SearchOrderRes:
        """
        see: https://doc.mbd.pub/api/ding-dan-cha-xun
        :param kwargs: SearchOrderReq required fields
            and optional `requests.post`'s kwargs, e.g. timeout=5
        :return: SearchOrderRes
        """
        req = SearchOrderReq(**kwargs)
        api = f"{self.domain}/release/main/search_order"
        res = self._post(api, req, **kwargs)
        return SearchOrderRes(**res)