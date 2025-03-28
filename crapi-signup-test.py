import requests
import random
import string
import time
import ipaddress

# API endpoint
url = "https://demo.mycrapiapp.com/identity/api/auth/signup"

# Domains for email
domains = ["frootcompany.com", "gmail.ai", "apple.ru", "me.com", "gmail.com", "hotmail.com", "yahoomail.com"]

# User-Agent list
user_agents = [
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
]

# First and last names lists
first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah", "Ian", "Julia", "Kevin", "Laura", "Michael", "Nancy", "Oliver", "Paula", "Quincy", "Rachel", "Steve", "Tina", "Ursula", "Victor", "Wendy", "Xander", "Yvonne", "Zach"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White", "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall"]

# Generate a random 10-digit phone number
def generate_phone_number():
    return "".join(random.choices(string.digits, k=10))

# Generate a random password (8-16 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char)
def generate_password():
    length = random.randint(8, 16)
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()")
    others = "".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=length - 4))
    password = upper + lower + digit + special + others
    return "".join(random.sample(password, len(password)))  # Shuffle password

# Generate a random name
def generate_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return first, last

# Generate unique emails
used_emails = set()
def generate_unique_email():
    while True:
        first, last = generate_name()
        email = f"{first.lower()}.{last.lower()}@{random.choice(domains)}"
        if email not in used_emails:
            used_emails.add(email)
            return first, last, email

# Generate a random IP address
def generate_random_ip():
    if random.choice([True, False]):
        return str(ipaddress.IPv4Address(random.randint(0, (1 << 32) - 1)))
    else:
        return str(ipaddress.IPv6Address(random.getrandbits(128)))

# Generate a random user data
def generate_user():
    first, last, email = generate_unique_email()
    return {
        "name": f"{first} {last}",
        "email": email,
        "number": generate_phone_number(),
        "password": generate_password()
    }

# Send POST request
def send_request():
    user_data = generate_user()
    user_agent = random.choice(user_agents)
    x_forwarded_for = generate_random_ip()
    headers = {
        "Cookie": "traceable-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ewogICJzaXRlS2V5IjogIlQtODc4NDcyOSIsCiAgInZpc2l0b3IiOiAiOTc2MGY2YjQtY2U3Mi00ZWViLWFhYmMtY2JmZGExODhlNjBjIiwKICAic3RhdGUiOiAiSU5WSVNJQkxFX1BBU1MiLAogICJmbG93cyI6IFsibG9naW4iXSwKICAicmlza3MiOiBbIk9USEVSIiwgIlNDUkVFTiIsICJFTlZJUk9OTUVOVCIsICJJTlRFUkFDVElPTlMiXQp9.Q4tEycxjnRdDIBsqI5eqSnYZLfdiZvvKuI7BbwqxsI4",
        "User-Agent": user_agent,
        "X-Forwarded-For": x_forwarded_for
    }
    response = requests.post(url, json=user_data, headers=headers)
    print(f"Sent Request: Email: {user_data['email']}, Phone: {user_data['number']}, Password: {user_data['password']}, User-Agent: {user_agent}, X-Forwarded-For: {x_forwarded_for}")
    print(f"Response: {response.status_code}, {response.text}")

# Run the script
if __name__ == "__main__":
    for _ in range(1337):
        send_request()
        time.sleep(0.337)

