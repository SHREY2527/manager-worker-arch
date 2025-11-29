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
        The run method is the entry point for the worker thread.
        It is automatically invoked when the worker thread is started by the manager.
        """
        if self.name == "style_predictor":
            while self.isWait():
                result = self.m_manager.getJob(self.name)
                if result: # Check if the manager assigned a job to the worker
                    try:
                        ###
                        # Process the assigned job here.
                        # This could involve tasks like detection, segmentation, classification,
                        # or any other AI/ML or non-AI/ML processing.
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
                else: # No job available for the worker
                    print("no item is available for process")
                    time.sleep(1)
        else:
            while self.isRunning():
                time.sleep(1)