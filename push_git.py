import base64
import hashlib
import hmac
import json
from datetime import datetime

import requests

WEBHOOK_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/e773edda-d19d-47bd-a647-b4c2d8f64622"
WEBHOOK_SECRET = "TUPJ3qpcWTFntZNDw8nbOd"
timestamp = int(datetime.now().timestamp())

def gen_sign(secret):
    # 拼接时间戳以及签名校验
    string_to_sign = '{}\n{}'.format(timestamp, secret)

    # 使用 HMAC-SHA256 进行加密
    hmac_code = hmac.new(
        string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
    ).digest()

    # 对结果进行 base64 编码
    sign = base64.b64encode(hmac_code).decode('utf-8')

    return sign

def main():
    sign = gen_sign(WEBHOOK_SECRET)
    card = json.dumps({
  "config": {
    "wide_screen_mode": True
  },
  "elements": [
    {
      "tag": "img",
      "img_key": "img_v2_b9b84c17-5ce8-4e18-b189-b40036492a5g",
      "alt": {
        "tag": "plain_text",
        "content": ""
      },
      "mode": "fit_horizontal",
      "preview": True
    },
    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "grey",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": "**🌟🌟🌟  本月实销总计：<font color='red'>6461</font>**",
              "text_align": "left"
            },
            {
              "tag": "markdown",
              "content": "**🌟🌟🌟  本日实销总计：<font color='red'>284</font>**",
              "text_align": "left"
            }
          ]
        }
      ]
    },
    {
      "tag": "img",
      "img_key": "img_v2_e3a2447c-5a1c-4ab4-a354-49cb1df35a4g",
      "alt": {
        "tag": "plain_text",
        "content": ""
      },
      "mode": "fit_horizontal",
      "preview": True
    },
    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "grey",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": "**本月小蚂蚁实销\n<font color='red'> 1767</font>**",
              "text_align": "center"
            },
            {
              "tag": "img",
              "img_key": "img_v2_cd04b366-86e4-43ae-9a84-8e71b161e06g",
              "alt": {
                "tag": "plain_text",
                "content": ""
              },
              "mode": "fit_horizontal",
              "preview": "true"
            }
          ]
        }
      ]
    },
    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "grey",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": "**本月QQ冰淇凌实销\n<font color='red'> 4512</font>**",
              "text_align": "center"
            },
            {
              "tag": "img",
              "img_key": "img_v2_63f062ca-140a-43b7-8076-7390b4a83f8g",
              "alt": {
                "tag": "plain_text",
                "content": ""
              },
              "mode": "fit_horizontal",
              "preview": True
            }
          ]
        }
      ]
    },
    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "grey",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": "**本月无界Pro实销\\n<font color='red'> 104</font>**",
              "text_align": "center"
            },
            {
              "tag": "img",
              "img_key": "img_v2_8c87978c-c419-4955-967f-d2a3798ec47g",
              "alt": {
                "tag": "plain_text",
                "content": ""
              },
              "mode": "fit_horizontal",
              "preview": True
            }
          ]
        }
      ]
    },
    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "grey",
      "columns": [
        {
          "tag": "column",
          "width": "weighted",
          "weight": 1,
          "vertical_align": "top",
          "elements": [
            {
              "tag": "markdown",
              "content": "**本月eQ7实销\n<font color='red'> 78</font>**",
              "text_align": "center"
            },
            {
              "tag": "img",
              "img_key": "img_v2_a2bbc6e0-3a7b-4b9a-8aa0-59b3c2a579fg",
              "alt": {
                "tag": "plain_text",
                "content": ""
              },
              "mode": "fit_horizontal",
              "preview": True
            }
          ]
        }
      ]
    },
    {
      "tag": "note",
      "elements": [
        {
          "tag": "plain_text",
          "content": "💡 [机密] 请注意信息安全，严禁外传"
        }
      ]
    },
    {
      "tag": "column_set",
      "flex_mode": "none",
      "background_style": "default",
      "columns": []
    }
  ],
  "header": {
    "template": "red",
    "title": {
      "content": "🔥🔥🔥每日销量快报！！！",
      "tag": "plain_text"
    }
  }
})
    params = {
        "timestamp": timestamp,
        "sign": sign,
        "msg_type": "interactive",
        "card": card,
    }
    headers = {"Content-Type": "application/json"}

    resp = requests.post(WEBHOOK_URL, json=params,headers=headers)
    resp.raise_for_status()
    result = resp.json()
    if result.get("code") and result.get("code") != 0:
        print(f"发送失败：{result['msg']}")
        return
    print("消息发送成功")

if __name__ == '__main__':
    main()