class DBOperations():
    def __init__(self):
        pass

    def get_job_for_worker(self):
        """
        here you will find the unprocessed job from the database
        """
        pass

    def submit_job_result(self, generated_response):
        """
        here you will update the job result in the database
        """
        pass
    
    def submit_job_for_failure(self):
        """
        here you will update failure job result in the database
        """
        pass
        