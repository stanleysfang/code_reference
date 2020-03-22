
#########################
#    conda reference    #
#########################

#### create env ####
conda create -y --name query python=3.7.0 pip

#### remove env ####
conda remove -y --name query --all

#### list env ####
conda env list

#### activate env ####
source activate query
