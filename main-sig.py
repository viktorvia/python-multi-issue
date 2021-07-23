from os import wait
import signal
from subprocess import run
from time import sleep

def chld_handler(_signum, _frame):
    wait()

signal.signal(signal.SIGCHLD, chld_handler)

while True:
    result = run(["python", "multi.py"], capture_output=True)
    print(result.stdout.decode('utf-8'))
    result = run(["ps", "-ef", "--forest"], capture_output=True)
    print(result.stdout.decode('utf-8'), flush=True)
    sleep(1)
