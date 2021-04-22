# -*- coding: utf-8 -*-
"""
@Time    : 2021/4/18 13:16
@Author  : github.com/shaoxyz
"""

from enum import IntEnum, Enum
from typing import TypeVar, Optional, Union
from pydantic import BaseModel

T = TypeVar("T")
Error = Optional[str]


class PayWayEnum(IntEnum):
    WeChat = 1  # 微信支付
    AliPay = 2  # 支付宝支付


class OrderStateEnum(IntEnum):
    unpaid = 0  # 未支付
    paid = 1  # 已支付
    settled = 2  # 已结算
    in_complain = 3  # 投诉中
    complain_finished = 4  # 投诉完结
    complain_timeout = 5  # 投诉超时
    in_complain_handling = 6  # 商家处理中


class WebHookTypeEnum(Enum):
    ChargeSucceeded = "charge_succeeded"  # 支付成功的回调类型
    Complaint = "complaint"  # 投诉的回调类型


class RefundStateEnum(IntEnum):
    none = 0  # 无退款
    partial = 1  # 部分退款
    full = 2  # 全额退款


class WeChatJSApiReq(BaseModel):
    """
    微信JSAPI支付请求参数
    """

    # app_id: str
    openid: str
    description: str
    amount_total: int
    out_trade_no: Optional[str]
    callback_url: str
    # sign: str


class WeChatJSApiRes(BaseModel):
    """
    微信JSAPI支付返回参数
    """

    appId: Optional[str]
    timeStamp: Optional[str]
    nonceStr: Optional[str]
    package: Optional[str]
    signType: Optional[str]
    paySign: Optional[str]
    code: Optional[str]
    message: Optional[str]
    error: Error


class WeChatH5Req(BaseModel):
    """
    微信H5支付请求参数
    """

    # app_id: str
    channel: str = "h5"
    description: str
    amount_total: int
    out_trade_no: Optional[str]
    # sign: str


class WeChatH5Res(BaseModel):
    """
    微信H5支付返回参数
    """

    h5_url: Optional[str]
    error: Error


class AliPayReq(BaseModel):
    """
    支付宝支付请求参数
    """

    # app_id: str
    url: str
    description: str
    amount_total: int
    out_trade_no: Optional[str]
    callback_url: Optional[str]
    # sign: str


class AliPayRes(BaseModel):
    """
    支付宝支付返回参数
    """

    body: Optional[str]
    error: Error


class RefundReq(BaseModel):
    """
    退款请求参数
    """

    # app_id: str
    order_id: str
    # sign: str


class RefundRes(BaseModel):
    """
    退款返回参数
    """

    code: Optional[int]
    info: Optional[str]
    message: Optional[str]
    error: Error


class SearchOrderReq(BaseModel):
    """
    查询订单请求参数
    """

    # app_id: str
    out_trade_no: str
    # sign: str


class SearchOrderRes(BaseModel):
    """
    查询订单返回参数
    """

    order_id: Optional[str]
    charge_id: Optional[str]
    description: Optional[str]
    share_id: Optional[str]
    share_state: Optional[int]
    amount: Optional[int]
    state: Optional[OrderStateEnum]
    create_time: Optional[int]
    payway: Optional[PayWayEnum]
    refund_state: Optional[RefundStateEnum]
    plusinfo: Optional[str]
    error: Error


class WebHookChargeSucceeded(BaseModel):
    """
    当 type 为 charge_succeeded 时，WebHook的data结构
    """

    openid: str
    charge_id: str
    description: str
    out_trade_no: str
    amount: int
    payway: PayWayEnum


class WebHookComplaint(BaseModel):
    """
    当 type 为 complaint 时，WebHook的data结构
    """

    out_trade_no: str
    complaint_detail: str
    amount: int
    payer_phone: str


class WebHookRet(BaseModel):
    """
    响应WebHook
    """

    type: WebHookTypeEnum
    data: Union[WebHookChargeSucceeded, WebHookComplaint]


class GetOpenIdReq(BaseModel):
    """
    获取用户openid请求参数
    """

    # app_id: str
    target_url: str
