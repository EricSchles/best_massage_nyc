from pusher import run
import time
from sys import argv
while True:

    msg = argv[1]
    on_heroku = False
    try:
        msg = argv[2]
        on_heroku = True
    except:
        run(first=msg,second=on_heroku)
    run(first=msg,second=on_heroku)
    if not argv[1]:
        time.sleep(300) #sleep for five minutes
    else:
        time.sleep(int(argv[1]))
