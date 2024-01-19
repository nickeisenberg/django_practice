import time

class ListAppender:
    """
    Pretend this class exists outside this file
    """

    def __init__(self, m):
        self.m = m

    def appender(self, ls, updater=None):
        
        then = time.time()
        for i, l in enumerate(ls):
    
            self.m.append(l)
            
            if updater:
                now = time.time()
                if i == 0 or i == len(ls) - 1:
                    time.sleep(.1)
                    then = now
                    updater(i, len(ls))
                elif now - then > 1:
                    then = now
                    updater(i, len(ls))

