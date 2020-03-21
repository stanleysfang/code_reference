#!/bin/bash

start_time=$(date)
echo -e "\n================================\nScript          ${0##/*/} $*\nStart Time      ${start_time}\n"

#### Startup ####
cd $HOME

## Install dpkg-dev, gcc, g++, libc6-dev, make
# sudo apt update && sudo apt upgrade && sudo apt install -y build-essential

## Install Java 8
sudo apt update && sudo apt install -y openjdk-8-jre

## Install R
sudo add-apt-repository -y ppa:marutter/rrutter
sudo apt-get update && sudo apt-get install -y r-base r-base-dev
# Uncomment R_LIBS path in /etc/R/Renviron.site
mkdir -p $HOME/R/library

## Install Anaconda
wget "https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh"
bash $HOME/Anaconda3-5.3.1-Linux-x86_64.sh -b
echo -e "\n# added by Anaconda3 installer\nexport PATH=\"$HOME/anaconda3/bin:\$PATH\"" >> $HOME/.bashrc # this doesn't work with airflow
rm $HOME/Anaconda3-5.3.1-Linux-x86_64.sh
export PATH="$HOME/anaconda3/bin:$PATH"

## Create Conda Environments
# query env
conda create -y --name query python=3.7.0 pip
source activate query

pip install google-api-python-client
pip install google-cloud-bigquery
pip install pandas
pip install pyarrow

pip install ipykernel
python -m ipykernel install --name query --display-name "Python 3.7.0 (query)" --user

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

#### Run Time ####
end_time=$(date)
start=$(date -d "${start_time}" +%s)
end=$(date -d "${end_time}" +%s)
secs=$(($end-$start))

echo -e "\nScript          ${0##/*/} $*\nStart Time      ${start_time}\nEnd Time        ${end_time}"
printf 'Run Time        %d day %d hr %d min %d sec\n================================\n' $(($secs/86400)) $(($secs%86400/3600)) $(($secs%3600/60)) $(($secs%60))
