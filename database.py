class DBOperations():
    def __init__(self):
        pass

    def getJobForWorker(self):
        """
        Retrieves an unprocessed job from the database.
        Implement the logic to fetch the next available job.
        
        Note : you have to update the job status to inprogress so same job is taken by another worker
        """
        pass

    def submitJobResult(self, generated_response):
        """
        Updates the job result in the database upon successful completion.
        Implement the logic to save the generated response.
        """
        pass
    
    def submitJobForFailure(self):
        """
        Updates the job status in the database upon failure.
        Implement the logic to handle job failure (e.g., retry count, error logging).
        
        Note : you have to update the job status to failed so same job is taken by another worker
        """
        pass
        