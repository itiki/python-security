# -*- coding: utf-8 -*-

import time
import threading
# import traceback
# from thread import error as threadError

def runThreads(numThreads, threadFunction):
    threads = []

    try:
        if numThreads > 1:
            # if startThreadMsg:
            infoMsg = "starting %d threads" % numThreads
            print (infoMsg)
                # logger.log(CUSTOM_LOGGING.SYSINFO, infoMsg)

        else:
            threadFunction()
            return

        for numThread in range(numThreads):
            thread = threading.Thread(target=exceptionHandledFunction, name=str(numThread), args=[threadFunction])

            # setDaemon(thread)
            thread.setDaemon(True)

            try:
                thread.start()
            except Exception as errMsg:
                errMsg = "error occurred while starting new thread ('%s')" % errMsg
                print (errMsg)
                # logger.log(CUSTOM_LOGGING.ERROR, errMsg)
                break

            threads.append(thread)

        # And wait for them to all finish
        alive = True
        while alive:
            alive = False
            for thread in threads:
                if thread.isAlive():
                    alive = True
                    time.sleep(0.1)

    except KeyboardInterrupt:
        # print
        # kb.threadContinue = False
        # kb.threadException = True

        if numThreads > 1:
            print ("waiting for threads to finish (Ctrl+C was pressed)")
            # logger.log(CUSTOM_LOGGING.SYSINFO, "waiting for threads to finish (Ctrl+C was pressed)")
        try:
            while (threading.activeCount() > 1):
                pass

        except KeyboardInterrupt:
            print ("user aborted (Ctrl+C was pressed multiple times")
            # raise PocsuiteThreadException("user aborted (Ctrl+C was pressed multiple times)")

        # if forwardException:
            # raise

    
# def setDaemon(thread):
    # Reference: http://stackoverflow.com/questions/190010/daemon-threads-explanation
    # if PYVERSION >= "2.6":
        # thread.daemon = True
    # else:


def exceptionHandledFunction(threadFunction):
    try:
        threadFunction()
    except KeyboardInterrupt:
        # kb.threadContinue = False
        # kb.threadException = True
        raise
    except Exception as errMsg:
        # thread is just going to be silently killed
        # logger.log(CUSTOM_LOGGING.ERROR, "thread %s: %s" % (threading.currentThread().getName(), errMsg))
        print ("thread %s: %s" % (threading.currentThread().getName(), errMsg))
