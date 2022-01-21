from keep_alive import keep_alive
import time

keep_alive()

time.sleep(10)

x = 1

while x < 2:
  time.sleep(1800)
  keep_alive()
