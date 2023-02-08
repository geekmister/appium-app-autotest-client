"""
The module created by Geemkmister, at 2023-02-05 PM 14:50

Device manage module (saw Device manager)

Features:
    1. fetch all connected device list(contains iOS and android)
    iOS:
        1. fetch connected device list
    Android:
        1. fetch connected device list
"""


import subprocess
import json

from utils import logger


class AndroidDeviceManager:
    """
    Android device manager...
    Features:
        1. fetch_devices, fetch android device list
    """

    @staticmethod
    def fetch_devices():
        """
        Desc: fetch android current connected device list
        Params: None
        Return: []
        """

        logger.info("Fetch android current connected device list...")

        devices = []

        buffers = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # type buffer to list structure and del element of index 0 -1
        buffer_list = buffers.stdout.readlines()
        del buffer_list[0]
        del buffer_list[-1]
        # encode bytes with utf-8 and generate android device list
        for item in buffer_list:
            attributes = item.decode("utf-8").replace("\n", "").split("\t")
            device = {"sn": attributes[0], "name": attributes[1]}
            devices.append(device)

        return devices


class IOSDeviceManager:
    """
    iOS device manager...
    Features:
        1. fetch_devices, fetch iOS current connected device list
    """

    @staticmethod
    def fetch_devices():
        """
        Desc: fetch iOS current connected device list
        Params: None
        Return: []
        """

        logger.info("Fetch iOS current connected device list...")

        popen = subprocess.Popen("tidevice list --json", shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = popen.stdout.readlines()
        bytes_trans_str = ""
        for item in data:
            bytes_trans_str = bytes_trans_str + str(item, "utf-8").replace("\n", "").replace("\r", "").strip()

        return json.loads(bytes_trans_str)


def package_devices():
    """
    Desc: package android an iOS devices
    Parms: None
    Return: {}
    """

    logger.info("package devices...")

    devices = {"android": AndroidDeviceManager.fetch_devices(), "iOS": IOSDeviceManager.fetch_devices()}
    logger.info(devices)
    return devices


if __name__ == "__main__":
    package_devices()
