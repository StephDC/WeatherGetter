#! /usr/bin/env python3
import main
import random
def run():
    delayTime = random.randrange(300)
    main.time.sleep(delayTime)
    try:
        main.main()
    except:
        print('unknown.jpg')
if __name__ == '__main__':
    run()
