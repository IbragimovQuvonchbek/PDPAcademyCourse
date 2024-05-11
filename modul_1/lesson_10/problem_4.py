from datetime import datetime
from time import sleep

if __name__ == '__main__':
    try:
        while True:
            now = datetime.now()
            print(now.strftime("%X"))
            sleep(2)
    except KeyboardInterrupt:
        print("stopped")
