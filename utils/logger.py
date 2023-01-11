from termcolor import colored


@staticmethod
def verbose(msg):
    # 打印verbose日志
    TermWarpper.warpper_white(msg)


@staticmethod
def debug(msg):
    # 打印debug日志
    TermWarpper.warpper_blue(msg)


@staticmethod
def info(msg):
    # 打印info日志
    TermWarpper.warpper_green(msg)


@staticmethod
def warn(msg):
    # 打印warn日志
    TermWarpper.warpper_yellow(msg)


@staticmethod
def error(msg):
    # 打印error日志
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
    pass