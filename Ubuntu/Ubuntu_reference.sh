
#### Key Management ####
sudo apt-key list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 # Michael Rutter's key
sudo add-apt-repository -y ppa:marutter/rrutter
sudo apt-key del E084DAB9
