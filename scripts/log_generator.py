import random
import time
from datetime import datetime

actions = ["LOGIN", "LOGOUT", "ERROR", "INFO", "DOWNLOAD"]
users = ["alice", "bob", "charlie", "dave"]
ips = ["192.168.0.{}".format(i) for i in range(1, 5)]

while True:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user = random.choice(users)
    ip = random.choice(ips)
    action = random.choice(actions)

    log_entry = "{} - {} - {} - {}\n".format(timestamp, user, ip, action)

    # Write the log entry to the file
    with open("../logs/app.log", "a") as f:
        f.write(log_entry)

    # Print the log entry to the terminal
    print(log_entry, end='')  # 'end=""' prevents print() from adding an additional newline

    time.sleep(random.randint(1, 3))
