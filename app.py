#!/usr/bin/env python3
import json
import random
import time


def get_temp():
    return random.randint(0, 50)


if __name__ == '__main__':
    while True:
        data = { 'temperature': get_temp() } 
        print(json.dumps(data))
        time.sleep(60)
