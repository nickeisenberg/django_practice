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
            now = time.time()
    
            self.m.append(l)
            
            if updater:
                if now - then > 1:
                    then = now
                    updater(i, len(ls))
