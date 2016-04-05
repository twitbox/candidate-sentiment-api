# Using Python v3.4.3
apt-get install -y python3-pip
sudo pip3 install virtualenv

echo "alias python=python3" >> /home/vagrant/.bashrc
echo "alias pip=pip3" >> /home/vagrant/.bashrc
echo "cd ~/app" >> /home/vagrant/.bashrc
echo "virtualenv venv" >> /home/vagrant/.bashrc
echo "source venv/bin/activate" >> /home/vagrant/.bashrc