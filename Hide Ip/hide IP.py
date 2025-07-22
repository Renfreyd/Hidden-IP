from stem import Signal
from stem.control import Controller
import time
import requests

def get_ip():
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return requests.get('http://httpbin.org/ip', proxies=proxies).text

def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  # cookie-based auth
        controller.signal(Signal.NEWNYM)

print("[*] Запуск Tor и смена IP каждые 10 секунд")
while True:
    print("[IP]:", get_ip())
    change_ip()
    time.sleep(10)
