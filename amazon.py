import requests
from bs4 import BeautifulSoup
import smtplip

#URL = 'https://www.amazon.com/AmazonBasics-High-Speed-HDMI-Cable-1-Pack/dp/B014I8SSD0/ref=sr_1_1?dchild=1&qid=1618171078&s=electronics&sr=1-1'

#URL = 'https://www.amazon.com/AmazonBasics-Puresoft-PU-Padded-Mid-Back-Computer/dp/B081H3Y5NW/ref=sr_1_2?dchild=1&keywords=amazonbasics&pd_rd_r=d8ea53fc-6e47-4a0f-acc9-258165ac137a&pd_rd_w=j6cRy&pd_rd_wg=U7QrV&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=K3M36WQ7436GPE0TTD0C&qid=1618184375&sr=8-2'

URL = 'https://www.amazon.com/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=sr_1_1?dchild=1&fst=as%3Aoff&pf_rd_i=16225009011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=82d03e2f-30e3-48bf-a811-d3d2a6628949&pf_rd_r=3DRGRPCGR8VE60KR37DP&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1618212335&refinements=p_n_shipping_option-bin%3A3242350011&rnid=493964&s=electronics&sr=1-1'

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'  }

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")

    title = soup.find(id="titleSection")

    print("soup", soup)

    print("tit", title)

    price = soup.find(id"shsija)
    converted_price = float(price[0:5])
    if (converted_price < 1.1700):
        send_mail()

def send_mail():
    server = smtplip.SMTP('smtp.gmail.com', password)
    subject = 'price fell'
    body = 'check url'
    msg = f"subjct: {subject}\n\n{body}"

    server.sendmail(
        'sender mail',
        'reciever mail',
        msg
    )

    server.quit()