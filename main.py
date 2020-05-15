import platform
import subprocess
import sched
import time
s = sched.scheduler(time.monotonic, time.sleep)


def checkConnection(host):
    option = '-c'
    if platform.system().lower() == 'windows':
        option = '-n'
    process = subprocess.run(
        ['ping', option, '1', host], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if process.returncode == 0:
        print(f"{host} is Up")
        sendNotification(host, 'Up')
    else:
        print(f"{host} is Down")
        sendNotification(host, 'Down')


def sendNotification(host, state):
    subprocess.Popen(['notify-send', f"{host} is {state}"])
    return


def program():
    sites = []
    with open("list.txt") as file:
        for line in file:
            host = line.strip()
            checkConnection(host)
    s.enter(10, 1, program)


if __name__ == '__main__':
    s.enter(10, 1, program)
    s.run()
