# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/18 16:26
@Author  : github.com/shaoxyz
"""
import config
from types import (
    SearchOrderReq,
    AliPayRes,
    AliPayReq,
    WeChatH5Req,
    WeChatH5Res,
    WeChatJSApiRes,
    WeChatJSAPIReq,
    GetOpenIdReq,
    SearchOrderRes,
    RefundReq,
    RefundRes,
)


class Client:
    """
    面包多支付客户端
    """

    def __init__(self, app_id: str, app_key: str, domain="https://api.mianbaoduo.com/"):

        self.app_id = app_id
        self.app_key = app_key

    def sign(self, req):
        pass

    def get_openid(self, req: GetOpenIdReq, *args, **kwargs) -> str:
        """
        返回用以获取用户openid的完整链接
        :param req:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def jsapi(self, req: WeChatJSAPIReq, *args, **kwargs) -> WeChatJSApiRes:
        pass

    def h5(self, req: WeChatH5Req, *args, **kwargs) -> WeChatH5Res:
        pass

    def alipay(self, req: AliPayReq, *args, **kwargs) -> AliPayRes:
        pass

    def refund(self, req: RefundReq, *args, **kwargs) -> RefundRes:
        pass

    def search_order(self, req: SearchOrderReq, *args, **kwargs) -> SearchOrderRes:
        """
        查询订单
        """
        pass
