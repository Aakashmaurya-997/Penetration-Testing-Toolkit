
import socket
import threading

def port_scanner(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open.")
        sock.close()

def password_bruteforce(username, password_list, login_function):
    for password in password_list:
        if login_function(username, password):
            print(f"[SUCCESS] Password found: {password}")
            return
    print("[FAILED] No password matched.")

def dummy_login(username, password):
    # Replace this function with actual login code
    return password == "admin123"

if __name__ == "__main__":
    print("1. Port Scanner")
    print("2. Password Brute Forcer")
    choice = input("Choose a module: ")

    if choice == "1":
        target_ip = input("Enter target IP: ")
        ports_to_scan = range(20, 1025)
        port_scanner(target_ip, ports_to_scan)
    elif choice == "2":
        user = input("Enter username: ")
        passwords = ["123456", "password", "admin123", "letmein"]
        password_bruteforce(user, passwords, dummy_login)
    else:
        print("Invalid choice.")
