from worker import Worker
from database import DBOperations
import uuid
import threading
import time

class Manager():
    def __init__(self):
        self.database_obj = DBOperations() #here we will initialize data source it is either databse,or any api or anything else
        self.manager_lock = threading.Lock() #lock for thread safty
        Worker_detail_dict = {"worker_name": 1} #you can add multiple workers and also directly manage total number of worker from here
        self.workers = [] 
        for worker_name, total_workers in Worker_detail_dict.items():
            for i in range(total_workers):
                # Pass self (manager) to worker
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
                # get the job from databse
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
                    # update the job in database
                    self.database_obj.submit_job_result(generated_response)
                else:
                    # update the job in database
                    self.database_obj.submit_job_for_failure(generated_response)
            finally:
                self.manager_lock.release()
        else:
            pass


if __name__ == "__main__":
    manager_obj = Manager()
    while True:
        time.sleep(1)
    
    
                
    

                        
            
        


            
            