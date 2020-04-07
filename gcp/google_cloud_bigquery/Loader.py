
from google.cloud import bigquery
# from google.api_core import exceptions as GoogleExceptions

class Loader:
    """
    Loads tables to BigQuery.
    
    Attributes:
        client: BigQuery client
        run_project: the project that the job will run on behalf of
        job_history: a list of handlers to load jobs ran
    """
    def __init__(self, client=None, run_project="stanleysfang"):
        if client:
            self.client = client
        else:
            self.client = bigquery.Client(project=run_project)
        
        self.run_project = self.client.project
        self.job_history=[]
    
    def config_job(self, schema, overwrite=True, time_partitioning=False, partition_field=None):
        job_config = bigquery.LoadJobConfig()
        
        job_config.schema = [bigquery.SchemaField(name, field_type) for name, field_type in schema]
        
        if overwrite:
            job_config.write_disposition = 'WRITE_TRUNCATE'
        else:
            job_config.write_disposition = 'WRITE_APPEND'
        
        # The only supported partition type is "DAY" which is the default.
        if time_partitioning:
            job_config.time_partitioning = bigquery.table.TimePartitioning(field=partition_field)
        
        return job_config
    
    def load_df(self, df, destination_table, schema, overwrite=True, time_partitioning=False, partition_field=None):
        """
        Loads a pandas dataframe to BigQuery and returns a handler to the job.
        
        Args:
            df: pandas dataframe
            destination_table: the table that the job will write to (e.g. 'project_id.dataset_id.table_id') (for time partition tables, 'project_id.dataset_id.table_id$YYYYMMDD')
            schema: a list of tuples that contains name and field_type
            overwrite: a boolean where True will overwrite destination table and False will append to it
            time_partitioning: a boolean where True will load a partition table
            partition_field: the column to partition the table on (column can be TIMESTAMP or DATE data type)
        
        Returns:
            google.cloud.bigquery.job.LoadJob: a handler to the load job
        """
        job_config = self.config_job(schema, overwrite, time_partitioning, partition_field)
        load_job = self.client.load_table_from_dataframe(df, destination_table, job_config=job_config)
        self.job_history.append(load_job)
        
        return load_job
