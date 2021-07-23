from os import wait, waitstatus_to_exitcode
import signal
from subprocess import run
from sys import stdout
from time import sleep
from traceback import print_stack

processes = []

def chld_handler(_signum, _frame):
    global processes
    pid, _ = wait()
    processes.append(pid)

if __name__ == "__main__":
    signal.signal(signal.SIGCHLD, chld_handler)
    result = run(["python", "multi.py"], capture_output=True)
    print(result.stdout.decode('utf-8'), flush=True)
    sleep(2) # Sometimes the second process exits a little later
    print(f"Reaped {len(processes)} processes: {processes}")
    print("Process list in container:")
    result = run(["ps", "-ef", "--forest"], capture_output=True)
    print(result.stdout.decode('utf-8'), flush=True)
