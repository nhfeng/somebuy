from out_url import out_url
from alert_result import alert_result
from out_connect import out_connect

def main():
    murl = out_url()
    url = murl.get_url()
    print("订单url: " + url)

main()