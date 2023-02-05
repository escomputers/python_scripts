cd /tmp/
wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
tar xzf Python-3.11.0.tgz
cd Python-3.11.0

sudo ./configure --prefix=/opt/python/3.11.0/ --enable-optimizations
sudo make -j "$(nproc)"
sudo make altinstall
sudo rm /tmp/Python-3.11.0.tgz
