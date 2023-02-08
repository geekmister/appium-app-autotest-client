"""
The module created by Geemkmister, at 2023-02-05 PM 15:32

This is a tool that real-time print and record logs.

Features:
1. class TermWarpper is styled terminal out text, you can custom color or extend by termcolor.
2. class Recorder is write temporary to local file.
3. function verbose(msg) is print to terminal window verbose log with white color.
4. function debug(msg) is print to terminal window debug log with blue color.
5. function info(msg) is print to terminal window debug log with green color.
6. function warn(msg) is print to terminal window warn log with yellow color.
7. function error(msg) is print to terminal window error log with red color.

Todo:
1. class Recorder is write temporary to local file.
"""

import time

from termcolor import colored


def verbose(msg):
    # print verbose log
    msg = "  [VERBOSE]  " + str(time.time()) + ":  " + str(msg)
    TermWarpper.warpper_white(msg)


def debug(msg):
    # print debug log
    msg = "  [DEBUG]  " + str(time.time()) + ":  " + str(msg)
    TermWarpper.warpper_blue(msg)


def info(msg):
    # print info log
    msg = "  [INFO]  " + str(time.time()) + ":  " + str(msg)
    TermWarpper.warpper_green(msg)


def warn(msg):
    # print warn log
    msg = "  [WARN]  " + str(time.time()) + ":  " + str(msg)
    TermWarpper.warpper_yellow(msg)


def error(msg):
    # print error log
    msg = "  [ERROR]  " + str(time.time()) + ":  " + str(msg)
    TermWarpper.warpper_red(msg)


class TermWarpper:
    """
    Terminal输出内容样式包装器
    """

    @staticmethod
    def warpper_white(msg):
        print(colored(msg, 'white'))

    @staticmethod
    def warpper_blue(msg):
        print(colored(msg, 'blue'))

    @staticmethod
    def warpper_green(msg):
        print(colored(msg, 'green'))

    @staticmethod
    def warpper_yellow(msg):
        print(colored(msg, 'yellow'))

    @staticmethod
    def warpper_red(msg):
        print(colored(msg, 'red'))


if __name__ == '__main__':
    debug("test")