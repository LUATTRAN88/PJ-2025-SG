import threading
from time import sleep

x = 0

def start_secondary():
  y = 0
  while True:
    y += 1
    print("Secondary thread " + str(y))
    sleep(0.5)
def second_secondary():
  y = 0
  while True:
    y += 1
    print("HI Toan thread " + str(y))
    sleep(0.5)

secondary_thread = threading.Thread(target = start_secondary)
secondary_thread.start()
second_thread = threading.Thread(target = second_secondary)
second_thread.start()

while True:
  x += 1
  print("Main thread " + str(x))
  sleep(1)