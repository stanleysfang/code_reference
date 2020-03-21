
# h2o env
conda create -y --name h2o python=3.6.5 pip
source activate h2o

pip install pandas
pip install matplotlib

pip install requests
pip install tabulate
pip install "colorama>=0.3.8"
pip install future
pip uninstall -y h2o
pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
# pip install http://h2o-release.s3.amazonaws.com/h2o/rel-wolpert/11/Python/h2o-3.18.0.11-py2.py3-none-any.whl --trusted-host h2o-release.s3.amazonaws.com

pip install ipykernel
python -m ipykernel install --name h2o --display-name "Python 3.6.5 (h2o)" --user
