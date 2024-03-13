import subprocess
import threading
import os
import fcntl
import select
from colorama import init
from termcolor import colored

def set_nonblocking(fd):
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

def run_command(command, app_name, color):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    set_nonblocking(process.stdout.fileno())
    set_nonblocking(process.stderr.fileno())
    while True:
        reads, _, _ = select.select([process.stdout, process.stderr], [], [])
        for fd in reads:
            output = fd.readline().decode().strip()
            if output:
                print(colored(f"[{app_name}]", color), output)
        if process.poll() is not None:
            break
    return process.returncode

def run_server():
    app_name = "webserver"
    command = "cd src && DEBUG=1 python server.py"
    return run_command(command, app_name, "green")

def run_client():
    app_name = "client"
    command = "cd examples && sleep 1 && python client.py"
    return run_command(command, app_name, "blue")

# Runs each service as a seperate thread
thread_names = [run_server, run_client]
threads = [threading.Thread(target=thread) for thread in thread_names]
init()
[thread.start() for thread in threads]
[thread.join() for thread in threads]