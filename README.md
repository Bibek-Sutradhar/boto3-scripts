# boto3-scripts

1. python3 -m venv boto3-venv
2. source boto3-venv/bin/activate

pip install boto3


yum install gcc openssl-devel bzip2-devel libffi-devel
cd /usr/src
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
tar xzf Python-3.7.4.tgz
cd Python-3.7.4
./configure --enable-optimizations
make altinstall
cd /usr/local/bin/
./python3.7 --version
./pip3.7 --version
pwd
ln -s /usr/local/bin/python3.7 /bin/python3
python3 --versio
ln -s /usr/local/bin/pip3.7 /bin/pip3
pip3 --version
pip3 install boto3
