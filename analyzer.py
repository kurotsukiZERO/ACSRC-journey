# A dictionary to count failures and successes per IP
failures = {}
successes = {}

# Open the log file and go through it one line at a time
with open("auth.log") as file:
    for line in file:
        # Get the IP from the last word on the line
        ip = line.strip().split()[-1]

        # Count failed attempts
        if "FAILED" in line:
            failures[ip] = failures.get(ip, 0) + 1

        # Count successful attempts
        if "SUCCESS" in line:
            successes[ip] = successes.get(ip, 0) + 1

# Report anyone with 3 or more failed attempts
for ip, count in failures.items():
    if count >= 3:
        print(ip)
        print("Failed attempts:", count)
        print("Successful attempts:", successes.get(ip, 0))
        print("Status: SUSPICIOUS")

# Optional: report successful users as well
for ip, count in successes.items():
    if count >= 3:
        print(ip)
        print("Successful attempts:", count)
        print("Status: CLEAR")
