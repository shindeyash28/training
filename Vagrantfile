Vagrant.configure("2") do |config|

	config.vm.box = "bento/ubuntu-22.04"
 	config.vm.hostname = "devops-platform"

 	config.vm.network "forwarded_port", guest: 30080, host: 8080

 	config.vm.provider "virtualbox" do |vb|
  		vb.memory = 2048
  		vb.cpus = 2
  		vb.name = "devops-platform-vm"
 	end
 
 	config.vm.provision "shell", inline: <<-SHELL
  		apt-get update -y
  		apt-get install -y curl git docker.io
  
  		systemctl enable docker
  		systemctl start docker
  		usermod -aG docker vagrant
  
  		curl -sfL https://get.k3s.io | sh -
  		sleep 20
  
  		if [ -f /etc/rancher/k3s/k3s.yaml ]; then
  			mkdir -p /home/vagrant/.kube
  			cp /etc/rancher/k3s/k3s.yaml /home/vagrant/.kube/config
  			chown vagrant:vagrant /home/vagrant/.kube/config
  			chmod 600 /home/vagrant/.kube/config
  			echo 'export KUBECONFIG=/home/vagrant/.kube/config' >> /home/vagrant/.bashrc
  			echo "k3s setup complete"
  		else
  			echo "k3s yaml not found, waiting longer"
  			sleep 30
  			cp /etc/rancher/k3s/k3s.yaml /home/vagrant/.kube/config
			chown vagrant:vagrant /home/vagrant/.kube/config
  			chmod 600 /home/vagrant/.kube/config
  		fi
  
  		echo "Provisioning complete"
 	SHELL

end
