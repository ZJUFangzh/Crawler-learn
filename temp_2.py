# amason

import requests


url = 'https://www.amazon.cn/dp/B00UURHLQO/ref=cngwdyfloorv2_recs_0?pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=E2Q83X1MBZEMZ8HTJFNW&pf_rd_r=E2Q83X1MBZEMZ8HTJFNW&pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061'
try:
    kv = {'user_agent': 'Mozilla/5.0'}

    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('error')
