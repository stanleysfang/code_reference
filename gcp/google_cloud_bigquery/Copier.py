
from google.cloud import bigquery
# from google.api_core import exceptions as GoogleExceptions

class Copier:
    """
    Copies BigQuery tables.
    
    Attributes:
        client: BigQuery client
        run_project: the project that the job will run on behalf of
        job_history: a list of handlers to copy jobs ran
    """
    def __init__(self, client=None, run_project="stanleysfang"):
        if client:
            self.client = client
        else:
            self.client = bigquery.Client(project=run_project)
        
        self.run_project = self.client.project
        self.job_history=[]
    
    def config_job(self, overwrite=True):
        job_config = bigquery.CopyJobConfig()
        
        if overwrite:
            job_config.write_disposition = 'WRITE_TRUNCATE'
        else:
            job_config.write_disposition = 'WRITE_APPEND'
        
        return job_config
    
    def copy(self, source_table, destination_table, overwrite=True):
        """
        Copies a BigQuery table and returns a handler to the job.
        
        Args:
            source_table: the source table to copy from (e.g. 'project_id.dataset_id.table_id')
            destination_table: the destination table to copy to (e.g. 'project_id.dataset_id.table_id') (for time partition tables, 'project_id.dataset_id.table_id$YYYYMMDD')
            overwrite: a boolean where True will overwrite destination table and False will append to it
        
        Returns:
            google.cloud.bigquery.job.CopyJob: a handler to the copy job
        """
        job_config = self.config_job(overwrite)
        copy_job = self.client.copy_table(source_table, destination_table, job_config=job_config)
        self.job_history.append(copy_job)
        
        return copy_job
