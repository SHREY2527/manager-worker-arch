"""
You Don't have to change single line of code in thread class
"""
import threading
class Thread(object):
    condition_object = threading.Condition()
    def __init__(self, threadName):
        self.m_isRunning = False
        self.m_isThreadWaiting = False
        self.m_name = threadName
        self.thr = None
        self.condition_object = threading.Condition()
    def threadProc(self, obj):
        """
        Internal method to run the thread's target function.
        """
        obj.run()
    def start(self):
        """
        Starts the thread.
        Sets the running state to True and initializes the threading.Thread object.
        """
        self.m_isThreadWaiting = False
        self.m_isRunning = True
        self.thr = threading.Thread(target=self.threadProc, args=(self,))
        self.thr.start()
        return self.thr
    
    def isRunning(self):
        """
        Checks if the thread is currently running.
        Thread-safe access to the running state.
        """
        res = True
        self.condition_object.acquire()
        res = self.m_isRunning
        self.condition_object.release()
        return res

    def wait(self):
        """
        Puts the thread into a waiting state.
        """
        self.m_isThreadWaiting = True
        self.isWait()

    def nofity(self):
        """
        Notifies the thread to wake up from a waiting state.
        """
        if self.m_isThreadWaiting is True:
            self.condition_object.acquire()
            self.m_isThreadWaiting = False
            self.condition_object.notify()
            self.condition_object.release()

    def stop(self):
        """
        Stops the thread.
        Sets the running state to False and notifies the thread to ensure it exits.
        """
        self.condition_object.acquire()
        self.m_isRunning = False
        self.condition_object.release()
        self.nofity()


    def isWait(self):
        """
        Checks if the thread should wait or continue running.
        If the thread is in a waiting state, it blocks until notified.
        Returns True if the thread is running, False otherwise.
        """
        if self.m_isThreadWaiting is True:
            self.condition_object.acquire()
            self.condition_object.wait()
            self.condition_object.release()
        else:
            self.condition_object.acquire()
            result = self.m_isRunning
            self.condition_object.release()
            return result
        return True