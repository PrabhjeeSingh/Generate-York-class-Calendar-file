import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1 - Count: {i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(1)
        print(f"Thread 2 - Letter: {letter}")

if __name__ == "__main__":
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Execution complete.")
