#!/usr/bin/env python3
import json
import random
import time


def get_temp():
    try:
        return int(open('/sys/class/thermal/thermal_zone0/temp').read())/1000.0
    except:
        return random.randint(0, 50)

if __name__ == '__main__':
    while True:
        data = { 'temperature': get_temp() }
        print(json.dumps(data))
        time.sleep(60)
