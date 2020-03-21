
# query env
conda create -y --name query python=3.7.0 pip
source activate query

pip install google-api-python-client
pip install google-cloud-bigquery
pip install pandas
pip install pyarrow

pip install ipykernel
python -m ipykernel install --name query --display-name "Python 3.7.0 (query)" --user
