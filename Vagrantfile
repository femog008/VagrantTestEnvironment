# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

VAR_DOMAIN = "femog008.internal"
VAR_ROPOSITORY = "D:/VM/Shared/"

all_nodes = [
	{ :host => "svr-1", :ip => "172.168.1.10", :box => "bento/ubuntu-20.04", :ram => 1024, :cpu => 2, :gui => false },
	{ :host => "svr-2", :ip => "172.168.1.11", :box => "bento/ubuntu-20.04", :ram => 2048, :cpu => 2, :gui => false },
	{ :host => "svr-3", :ip => "172.168.1.12", :box => "bento/centos-7.2", :ram => 2048, :cpu => 2, :gui => false },
	{ :host => "client-1", :ip => "172.168.1.13", :box => "bento/ubuntu-20.04", :ram => 1048, :cpu => 1, :gui => true },
	{ :host => "client-2", :ip => "172.168.1.14", :box => "bento/centos-7.2", :ram => 1048, :cpu => 1, :gui => true }
]


# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.manage_guest = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true


  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.

	all_nodes.each do |new_node|

		config.vm.define new_node[:host] do |new_node_config|

			new_node_config.vm.box = new_node[:box]
			#new_node_config.vm.box_version = "2.0.14"
			
			new_node_config.vm.network "private_network", ip: new_node[:ip], :netmask => "255.255.255.0"
			new_node_config.vm.hostname = "#{new_node[:host]}.#{VAR_DOMAIN}"
			# new_node_config.vm.hostname = new_node[:host] + "." + VAR_DOMAIN

		    new_node_config.hostmanager.aliases = "#{new_node[:host]}"

			new_node_config.vm.provider :virtualbox do |v|
				v.name = new_node[:host].to_s
				v.gui = new_node[:gui]

				v.customize ["modifyvm", :id, "--memory", new_node[:ram].to_s ]
				v.customize ["modifyvm", :id, "--cpus", new_node[:cpu].to_s ]
			end # end provider

			new_node_config.vm.synced_folder VAR_ROPOSITORY, "/repository", 
				id: "repository",
				owner: "vagrant",
				group: "vagrant"

		  # new_node_config.vm.provision :shell, :path => "java/provision_for_java.sh"

		end # end config
	end # end cluster
end
