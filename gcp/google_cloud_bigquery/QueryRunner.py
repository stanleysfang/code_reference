
from google.cloud import bigquery
# from google.api_core import exceptions as GoogleExceptions

class QueryRunner:
    """
    Runs queries on BigQuery.
    
    Attributes:
        run_project: the project that queries will be billed to
        client: BigQuery client
        job_history: a list of handlers to query jobs ran
    """
    def __init__(self, run_project="stanleysfang"):
        self.run_project = run_project
        self.client = bigquery.Client(project=self.run_project)
        self.job_history=[]
    
    def config_job(self, destination_table=None, overwrite=True, time_partitioning=False, partition_field=None, dry_run=False):
        job_config = bigquery.QueryJobConfig()
        
        job_config.use_legacy_sql = False
        job_config.destination = destination_table
        job_config.dry_run = dry_run
        
        if overwrite:
            job_config.write_disposition = 'WRITE_TRUNCATE'
        else:
            job_config.write_disposition = 'WRITE_APPEND'
        
        if destination_table and time_partitioning:
            job_config.time_partitioning = bigquery.table.TimePartitioning(field=partition_field)
        
        return job_config
    
    def run_query(self, query_str, destination_table=None, overwrite=True, time_partitioning=False, partition_field=None, dry_run=False):
        """
        Executes a query and returns a handler to the job.
        
        Args:
            query_str: query string
            destination_table: the table that the query will write to (e.g. 'project_id.dataset_id.table_id') (for time partition tables, 'project_id.dataset_id.table_id$YYYYMMDD')
            overwrite: a boolean where True will overwrite destination table and False will append to it
            time_partitioning: a boolean where True will write the query to a partition table
            partition_field: the column to partition the table on (column can be TIMESTAMP or DATE data type)
            dry_run: a boolean indicating whether the query should be a dry run
        
        Returns:
            google.cloud.bigquery.job.QueryJob: a handler to the query job
        """
        job_config = self.config_job(destination_table, overwrite, time_partitioning, partition_field, dry_run)
        query_job = self.client.query(query_str, job_config=job_config)
        self.job_history.append(query_job)
        
        return query_job
