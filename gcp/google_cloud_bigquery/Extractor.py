
from google.cloud import bigquery
# from google.api_core import exceptions as GoogleExceptions

class Extractor:
    """
    Extracts BigQuery tables to Google Cloud Storage.
    
    Attributes:
        client: BigQuery client
        run_project: the project that the job will run on behalf of
        job_history: a list of handlers to extract jobs ran
    """
    def __init__(self, client=None, run_project="stanleysfang"):
        if client:
            self.client = client
        else:
            self.client = bigquery.Client(project=run_project)
        
        self.run_project = self.client.project
        self.job_history=[]
    
    def config_job(self, destination_format='CSV', field_delimiter=',', print_header=True):
        job_config = bigquery.ExtractJobConfig()
        
        job_config.destination_format = destination_format
        job_config.field_delimiter = field_delimiter
        job_config.print_header = print_header
        
        return job_config
    
    def extract(self, table, gs_path, destination_format='CSV', field_delimiter=',', print_header=True):
        """
        Extracts a BigQuery table to Google Cloud Storage and returns a handler to the job.
        
        Args:
            table: BigQuery table (e.g. 'project_id.dataset_id.table_id')
            gs_path: Google Cloud Storage path (e.g. 'gs://gs_bucket/table.csv')
            destination_format: exported file format
            field_delimiter: delimiter to use between fields in the exported data
            print_header: a boolean where True will print a header row in the exported data
        
        Returns:
            google.cloud.bigquery.job.ExtractJob: a handler to the extract job
        """
        job_config = self.config_job(destination_format, field_delimiter, print_header)
        extract_job = self.client.extract_table(table, gs_path, job_config=job_config)
        self.job_history.append(extract_job)
        
        return extract_job
