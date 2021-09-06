
env_nm="general"
conda create -y --name $env_nm python=3.6.13 pip # Anaconda repo doesn't have Python 3.6.14
source activate $env_nm

pip install pandas
pip install matplotlib

# pip install google-api-python-client
pip install google-cloud-bigquery
pip install pyarrow

pip install requests
pip install tabulate
pip install "colorama>=0.3.8"
pip install future

pip uninstall -y h2o
pip install http://h2o-release.s3.amazonaws.com/h2o/rel-zipf/7/Python/h2o-3.32.1.7-py2.py3-none-any.whl

pip install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/master/tested_requirements/requirements_36.reqs
pip install snowflake-connector-python==2.6.0

pip install ipykernel
python -m ipykernel install --name $env_nm --display-name "Python 3.6.13 ($env_nm)" --user
