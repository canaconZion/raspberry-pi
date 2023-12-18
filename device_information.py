import uuid
import socket
import time
import psutil
import sys

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:].upper()
    return "-".join([mac[e:e+2] for e in range(0,11,2)])

def get_computer_name():
    name = socket.getfqdn(socket.gethostname())
    return name

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return None

def get_time():
    local_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    weekday_number = local_time.tm_wday
    weekday_mapping = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_string = weekday_mapping[weekday_number]
    return formatted_time,weekday_string

def get_cpu_memory_usage():
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_percent = psutil.virtual_memory().percent

            output_string = f"CPU: {cpu_percent:.2f}% | Memory: {memory_percent:.2f}%"
            sys.stdout.write("\r" + output_string)
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序已终止.")

if __name__ == '__main__':
    mac = get_mac_address()
    name = get_computer_name()
    ip = get_local_ip()
    local_time,weekday_string = get_time()
    print("COMPUTER_NAME: ",name)
    print("IP: ",ip)
    print("MAC: ",mac)
    print("TIME: ",local_time,weekday_string)
    get_cpu_memory_usage()