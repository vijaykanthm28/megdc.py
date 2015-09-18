#! /usr/bin/python

__install_all__='''

apt-get -y install megamnilavu >> $MEGAM_LOG

echo "export MEGAM_HOME=/var/lib/megam" >> /home/cibadmin/.bashrc
source /home/cibadmin/.bashrc

sudo apt-add-repository -y ppa:openjdk-r/ppa >> $MEGAM_LOG

sudo apt-get -y update >> $MEGAM_LOG

sudo apt-get -y install openjdk-8-jdk >> $MEGAM_LOG

sudo echo 3 > /proc/sys/vm/drop_caches

apt-get -y install megamgateway >> $MEGAM_LOG

apt-get -y install chef-server >> $MEGAM_LOG
sudo echo 3 > /proc/sys/vm/drop_caches
megamd_preinstall >> $MEGAM_LOG

apt-get -y install rabbitmq-server || true >> $MEGAM_LOG

cat > //etc/rabbitmq/rabbitmq-env.conf <<EOF
NODENAME=megamd
EOF

service rabbitmq-server restart >> $MEGAM_LOG
sudo echo 3 > /proc/sys/vm/drop_caches
apt-get -y install megamd >> $MEGAM_LOG

service_restart >> $MEGAM_LOG

apt-get -y install megamanalytics >> $MEGAM_LOG

export DEBIAN_FRONTEND=noninteractive

sudo echo 3 > /proc/sys/vm/drop_caches

apt-get -y install megammonitor >> $MEGAM_LOG

echo "`date`: Step1: megam installed successfully." >> $MEGAM_LOG
'''


