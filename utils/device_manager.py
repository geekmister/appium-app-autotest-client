import subprocess

from utils import logger


class AndroidManager:

    @staticmethod
    def fetch_device_list():
        """
        :desc: fetch android device list
        :return: []
        """

        logger.info("Fetch android device list...")

        buffers = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # 将buffer转成list结构，并删除0和-1下标元素
        buffer_list = buffers.stdout.readlines()
        del buffer_list[0]
        del buffer_list[-1]
        # 将bytes进行utf-8编码，并生成android device list
        device_list = []
        for item in buffer_list:
            trans_item = item.decode("utf-8")
            items = trans_item.split("\t")
            android_entity = AndroidEntity()
            android_entity.set_sn(items[0])
            android_entity.set_name(items[1])
            device_list.append(android_entity)

        return device_list


class AndroidEntity:
    __sn = ""
    __name = ""

    def __int__(self, sn, name):
        self.__sn = sn
        self.__name = name

    def set_sn(self, sn):
        self.__sn = sn

    def get_sn(self):
        return self.__sn

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class IOSManager:
    """
    iOS device manager
    """

    @staticmethod
    def fetch_device_list():
        """
        :desc: fetch iOS device list
        :return: json
        """

        logger.info("Fetch iOS device list...")

        popen = subprocess.Popen("tidevice list --json", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        device_list = []
        bytes_data = popen.stdout.readlines()
        for bytes_item in bytes_data:
            trans_item = bytes_item.decode("utf-8").replace("\n", "").replace("\r", "")
            logger.debug(trans_item)
            device_list.append(trans_item)

        return device_list


if __name__ == "__main__":
    android_device_list = AndroidManager.fetch_device_list()
    IOSManager.fetch_device_list()
