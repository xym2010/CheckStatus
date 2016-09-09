#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright © XYM
# CreateTime: 2016-09-09 16:34:46

import requests
from bs4 import BeautifulSoup
import sys
from pushbullet import Pushbullet
reload(sys)
sys.setdefaultencoding("utf-8")

NowStatus = "后台已收材料"

if __name__ == "__main__":
    pb = Pushbullet("xxxx")
    payload = {'keyword': 'xxxx', 'action': 'query'}
    r = requests.post("http://info.szhr.com:9001/public/agentProgQuery.jsp", data=payload)
    soup = BeautifulSoup(r.text, 'html.parser')
    status = soup.contents[7].string
    if str(NowStatus) != str(status):
        push = pb.push_note("户口审查状态改变", str(status))
