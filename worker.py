from Thread import Thread
import time

class Worker(Thread):
    def __init__(self, manager, id):
        """
        Initializes the Worker instance with a reference to the manager and a unique identifier.
        """
        super().__init__(id)
        self.name = id
        self.m_manager = manager
        
    def run(self):
        """
        you always have to make run function in the worker class it will automatically start when you start the worker class from manager
        """
        if self.name == "style_predictor":
            while self.isWait():
                result = self.m_manager.getJob(self.name)
                if result: #if manager assigned job to worker
                    try:
                        ###
                        # here you will process the job the task like detection,segmentation,classification or any another AI/Ml or non AI/ML jobs over here
                        ###
                        response_dict = {
                            "success": True,
                            "message":"any response from worker task whcih you have to submit to manager"
                        }
                        self.m_manager.submitJob(self.name, response_dict)
                    except Exception as e:
                        # Submit failure to manager so it can handle retry logic
                        response_dict = {
                            "success": False,
                            "message":"any response from worker task whcih you have to submit to manager"
                        }
                        self.m_manager.submitJob(self.name, response_dict)
                else: # there is no job available for worker
                    print("no item is available for process")
                    time.sleep(1)
        else:
            while self.isRunning():
                time.sleep(1)