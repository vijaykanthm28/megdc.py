#!/usr/bin/python
import os
import socket
import urllib2
import sys
import datetime
import getopt
import textwrap
from help_text import *

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])
def install_pkg():
     print "hello"

#to find local ip address
def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip
#to check internet connections
def internet_on():
    try:
        response=urllib2.urlopen('http://216.58.220.46',timeout=2)
        return True
    except urllib2.URLError as err: pass
    return False


ipaddr = get_lan_ip()

def install_repo() :
     os.system('sudo apt-get -y install software-properties-common python-software-properties')
     os.system('add-apt-repository "deb [arch=amd64] http://get.megam.io/0.9/ubuntu/14.04/ testing megam" ')
     os.system('apt-key adv --keyserver keyserver.ubuntu.com --recv B3E0C1B7')
     os.system('apt-get -y update')
     os.system('apt-get -y install megamcommon')
     return
"""
if internet_on() == True :
   print "network available"
else:
   print "Check your network connection"
"""
#to get hostname
def host_name():
 return socket.gethostname()
"""
#write into a file
f = open('v.txt','a+')

f.write(' hai India')
f.seek(0)
print f.read()
"""
def pre_install():
  log=open("/var/log/megam/megamcib/megam.log" ,'a+')

  if internet_on() == True :
     print "network available"
  else:
     date=datetime.datetime.now()
     log.write("\n" +date + "check your network connection. get.megam.io is down or not reachable!")

  hostname=socket.gethostname()
  log.write("\nAdding entries in /etc/hosts")

  #ADD /etc/hosts entries
  ipaddr=get_lan_ip()
  f2=open("/etc/hosts",'a+')
  f2.write("\n127.0.0.1 " +hostname + "localhost" )
  f2.write("\n"+ ipaddr +"  "+ hostname +" localhost") 
  log.write("\n/etc/hosts entries added")

  #For apt-add-repository command
  install_repo()
  return

def install_megam() :
     print " Installing all megam packagess...." 
     install_all_text = textwrap.dedent(__install_all__).strip()
     os.system(install_all_text)
     return

def install_snowflake():
     os.system('apt-get install snowflake') 	
     return
def install_common():
	os.system('apt-get install megamcommon') 
	return
def install_nilavu():
        os.system('apt-get install megamnilavu')
        return
	
def install_gulpd():
	os.system('apt-get install megamgulpd')
	return
	
def install_megamd():
	os.system('apt-get install megamd') 
	return
	
def install_gateway():
	os.system('apt-get install megamgateway') 
	return

def install_riak():
##################################################### Install and configure riak #########################################################

  os.system('apt-get -y install riak ') #>>$MEGAM_LOG
  log.write('apt-get -y install riak')

  os.system('sed -i "s/^[ \t]*storage_backend .*/storage_backend = leveldb/" /etc/riak/riak.conf')
  os.system('sed -i "s/^[ \t]*listener.http.internal =.*/listener.http.internal = $ipaddr:8098/" /etc/riak/riak.conf')
  os.system('sed -i "s/^[ \t]*listener.protobuf.internal =.*/listener.protobuf.internal = $ipaddr:8087/" /etc/riak/riak.conf')

  os.system('riak start ') #>>$MEGAM_LOG
  log.write('riak start')
  return
##################################################### MEGAMD PREINSTALL SCRIPT #########################################################
	
def megamd_preinstall() :
#Gem install
  os.system('gem install chef --no-ri --no-rdoc ') #>>$MEGAM_LOG
  log.write('gem install chef --no-ri --no-rdoc ')
  d1='/var/lib/megam/gems'
  if not os.path.exists(d1):
        os.makedirs(d1)  
  
  os.chdir(d1)

  os.system('wget https://s3-ap-southeast-1.amazonaws.com/megampub/gems/knife-opennebula-0.3.0.gem')

  os.system('gem install knife-opennebula-0.3.0.gem ') # >> $MEGAM_LOG
  log.write('gem install knife-opennebula-0.3.0.gem ')

##################################################### configure chef-server #########################################################
  d = os.path.dirname("/opt/chef-server" ) 
  if not os.path.exists(d):
      f.write("Chef-server reconfigure") # >> $MEGAM_LOG
      os.system('sudo chef-server-ctl reconfigure')# >> $MEGAM_LOG

  chefserver=open('//etc/chef-server/chef-server.rb','a+') 
   
  __nginx = '''
  nginx['url']="https://$ipaddr"
  nginx['server_name']="$ipaddr"
  nginx['non_ssl_port'] = 90
  '''
  nginx_text = textwrap.dedent(__ngnix).strip()
  chefserver.write(nginx_text)
  os.system('sudo chef-server-ctl reconfigure')# >> $MEGAM_LOG
  os.system('sudo chef-server-ctl restart')# >> $MEGAM_LOG
  log.write('sudo chef-server-ctl reconfigure')
  log.write('sudo chef-server-ctl restart')
#sudo rabbitmq-server -detached >> $MEGAM_LOG

  os.system('set -e')

  #chef_repo_dir=`find /var/lib/megam/megamd  -name chef-repo  | awk -F/ -vOFS=/ 'NF-=0' | sort -u`
  chef_repo_dir="/var/lib/megam/megamd/"
  os.system('apt-get install git-core') #>> $MEGAM_LOG
  log.write('apt-get install git-core')
  os.system('git clone https://github.com/megamsys/chef-repo.git $chef_repo_dir/chef-repo')# >> $MEGAM_LOG
  log.write('git clone https://github.com/megamsys/chef-repo.git $chef_repo_dir/chef-repo')
  shutil.copy2('/etc/chef-server/admin.pem',chef_repo_dir+'/chef-repo/.chef')
  shutil.copy2('/etc/chef-server/chef-validator.pem', chef_repo_dir+'/chef-repo/.chef')
  os.system('ipaddr='+ipaddr)
  os.system('sed -i "s@^[ \t]*chef_server_url.*@chef_server_url \'https://$ipaddr\'@" $chef_repo_dir/chef-repo/.chef/knife.rb')
  
  os.makedir(chef_repo_dir+'/chef-repo/.chef/trusted_certs') # || true 
 
  os.system('[ -f /var/opt/chef-server/nginx/ca/$ipaddr.crt ] && cp /var/opt/chef-server/nginx/ca/$ipaddr.crt $chef_repo_dir/chef-repo/.chef/trusted_certs')
  os.system('[ -f /var/opt/chef-server/nginx/ca/$host.crt ] && cp /var/opt/chef-server/nginx/ca/$host.crt $chef_repo_dir/chef-repo/.chef/trusted_certs')
  os.system('sudo echo 3 > /proc/sys/vm/drop_caches')
  os.system('sleep 5')
  #os.system('echo "Cookbook upload Start=====> " >> $MEGAM_LOG')
  f.write("Cookbook upload End=====> ")# >> $MEGAM_LOG
  os.system('knife cookbook upload --all -c $chef_repo_dir/chef-repo/.chef/knife.rb  ') #|| true >> $MEGAM_LOG'
  f.write("knife cookbook upload --all -c $chef_repo_dir/chef-repo/.chef/knife.rb ")
  return
 

##################################################### Change config and restart services #################################################
def service_restart():
#MEGAM_GATEWAY
  os.system('sed -i "s/^[ \t]*riak.url.*/riak.url=\"$ipaddr\"/" /usr/share/megam/megamgateway/conf/application-production.conf')
  os.system('sed -i "s/^[ \t]*sf.host.*/sf.host=\"localhost\"/" /usr/share/megam/megamgateway/conf/application-production.conf')
  os.system('stop megamgateway ') #>> $MEGAM_LOG
  os.system('start megamgateway') #>> $MEGAM_LOG

#MEGAMD
  os.system('sed -i "s/.*:8087.*/  url: $ipaddr:8087/" /usr/share/megam/megamd/conf/megamd.conf')
  os.system('stop megamd ') #|| true >> $MEGAM_LOG'
  os.system('start megamd ') #>> $MEGAM_LOG
  f.write("start megamd")
  return


def uninstall_megam() :
     print " Removing nilavu...." 
     os.system('apt-get remove megamnilavu')
     os.system('apt-get purge megamnilavu')
     uninstall_gateway()
     uninstall_snowflake()
     uninstall_gulpd()
     uninstall_common()
     uninstall_snowflake()
     return
def uninstall_snowflake():
     os.system('apt-get remove snowflake')
     os.system('apt-get purge snowflake') 	
     return
def uninstall_common():
     os.system('apt-get remove megamcommon')
     os.system('apt-get purge megamcommon')
     return
	
def uninstall_gulpd():
	os.system('apt-get remove megamgulpd')
        os.system('apt-get purge megamgulpd')
	return
	
def uninstall_megamd():
	os.system('apt-get remove megamd')
        os.system('apt-get purge megamd') 
	return
	
def uninstall_gateway():
        os.system('apt-get remove megamgateway')
        os.system('apt-get purge megamgateway')
	return


