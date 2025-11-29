from worker import Worker
from database import DBOperations
import uuid
import threading
import time

class Manager():
    def __init__(self):
        self.database_obj = DBOperations() # Initialize the data source (Database, API, etc.)
        self.manager_lock = threading.Lock() # Lock for thread safety
        Worker_detail_dict = {"worker_name": 1} # Define worker types and their counts here
        self.workers = [] 
        for worker_name, total_workers in Worker_detail_dict.items():
            for i in range(total_workers):
                # Initialize the worker with a reference to the manager
                worker_thread = Worker(self, worker_name)
                worker_thread.start()
                self.workers.append(worker_thread)

    def getJob(self, worker_name):
        """
        Retrieves a job for the specified worker type.
        """
        if worker_name == "worker_name":
            self.manager_lock.acquire()
            try:
                # Retrieve a job from the database
                result = self.database_obj.get_job_for_worker()
            finally:
                self.manager_lock.release()
            
            if result:
                return result
            return None
        else:
            return None

    def submitJob(self, worker_name, generated_response):
        """
        Submits the generated response from a worker back to the database.
        """
        if worker_name == "worker_name":  
            self.manager_lock.acquire()
            try:             
                if generated_response:
                    # Update the job success status in the database
                    self.database_obj.submit_job_result(generated_response)
                else:
                    # Update the job failure status in the database
                    self.database_obj.submit_job_for_failure(generated_response)
            finally:
                self.manager_lock.release()
        else:
            pass


if __name__ == "__main__":
    manager_obj = Manager()
    while True:
        time.sleep(1)
    
    
                
    

                        
            
        


            
            