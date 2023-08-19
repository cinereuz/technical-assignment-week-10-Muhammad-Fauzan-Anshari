import time
import requests
import math
import random

TOKEN = "BBFF-TGQVzqiDL7zGpZ3umuh3oGPV9XESkh"  # Put your TOKEN here
DEVICE_LABEL = "sic4-kage"  # Put your device label here 
VARIABLE_LABEL_1 = "suhu"  # Put your first variable label here
VARIABLE_LABEL_2 = "kelembapan"  # Put your second variable label here
VARIABLE_LABEL_3 = "baterai"  # Put your second variable label here


def build_payload(variable_1, variable_2, variable_3):
    # Creates two random values for sending data
    suhu = random.randint(0, 100)
    kelembapan = random.randint(0, 85)
    baterai = int(80)

    # Sample lat long
    payload = {
    variable_1: suhu,
    variable_2: kelembapan,
    variable_3: baterai
    }


    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)