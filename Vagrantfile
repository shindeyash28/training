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
  apt-get install -y curl git
  echo "Provisioning complete"
 SHELL

end
