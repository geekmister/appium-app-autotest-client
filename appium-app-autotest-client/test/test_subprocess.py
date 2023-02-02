import subprocess


def execute_cmd():
    nowtime = subprocess.Popen("date", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(nowtime.stdout.read())


if __name__ == "__main__":
    execute_cmd()