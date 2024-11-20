import time
import psutil
from colored import fg 

red = fg('red')
green = fg('green')


def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars)) # Alt + 219(numpad) for the bar character 
    
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars)) # Alt + 219(numpad) for the bar character 

    print(red + f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end = "")
    print(green + f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end = "\r")



while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)

# print(psutil.cpu_percent())
# print(psutil.virtual_memory().percent)


