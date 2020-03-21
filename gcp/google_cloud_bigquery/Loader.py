
from google.cloud import bigquery
# from google.api_core import exceptions as GoogleExceptions

class Loader:
    """
    Loads tables to BigQuery.
    
    Attributes:
        run_project: the project that queries will be billed to
        client: BigQuery client
        job_history: a list of handlers to query jobs ran
    """
    def __init__(self, run_project="stanleysfang"):
        self.run_project = run_project
        self.client = bigquery.Client(project=self.run_project)
        self.job_history=[]
    
    def config_job(self, destination_table=None, overwrite=True, partition_field=None, dry_run=False):
        job_config = bigquery.QueryJobConfig()
        
        job_config.use_legacy_sql = False
        job_config.destination = destination_table
        job_config.dry_run = dry_run
        
        if overwrite:
            job_config.write_disposition = 'WRITE_TRUNCATE'
        else:
            job_config.write_disposition = 'WRITE_APPEND'
        
        if destination_table and partition_field:
            job_config.time_partitioning = bigquery.table.TimePartitioning(field=partition_field)
        
        return job_config
    
    def load_df(self, query_str, destination_table=None, overwrite=True, partition_field=None, dry_run=False):
        """
        Loads a pandas dataframe to BigQuery and returns a handler to the job.
        
        Args:
            query_str: query string
            destination_table: the table that the query will write to (e.g. 'project_id.dataset_id.table_id')
            overwrite: a boolean where True will overwrite destination table and False will append to it
            partition_field: the column to partition the table on (column can be TIMESTAMP or DATE data type)
            dry_run: a boolean indicating whether the query should be a dry run
        
        Returns:
            google.cloud.bigquery.job.QueryJob: a handler to the query job
        """
        job_config = self.config_job(destination_table, overwrite, partition_field, dry_run)
        query_job = self.client.query(query_str, job_config=job_config)
        self.job_history.append(query_job)
        
        return query_job

job_config = bigquery.LoadJobConfig()

job_config.write_disposition = 'WRITE_TRUNCATE'
job_config.schema = [
    bigquery.SchemaField('province_state', 'STRING'),
    bigquery.SchemaField('country_region', 'STRING'),
    bigquery.SchemaField('latitude', 'FLOAT64'),
    bigquery.SchemaField('longitude', 'FLOAT64')    
] + [bigquery.SchemaField(dt_col, 'INT64') for dt_col in dt_cols]

for df, metric in [(confirmed, 'confirmed'), (deaths, 'deaths'), (recovered, 'recovered')]:
    load_job = client.load_table_from_dataframe(
        df,
        destination='stanleysfang.surveillance_2019_ncov.ts_2019_ncov_{metric}_raw'.format(metric=metric),
        job_config=job_config
    )
    load_job.result()


