import os
import signal
import time
import subprocess


# Join :- @rzrdevil # Set the path to the script you want to restart
script_to_restart = "new.py"

def restart_script():
    # Join :- @rzrdevil # Run the script
    print("chal raha hai bc.....")
    process = subprocess.Popen(["python3", script_to_restart], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def main():
    process = restart_script()
    while True:
        time.sleep(480)  # Join :- @rzrdevil # Sleep for 30 seconds
        # Join :- @rzrdevil # Send Ctrl+C signal to the process
        process.send_signal(signal.SIGINT)
        # Join :- @rzrdevil # Wait for the process to terminate
        process.wait()
        # Join :- @rzrdevil # Restart the script
        process = restart_script()

if __name__ == "__main__":
    main()