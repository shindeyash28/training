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
  timedatectl set-ntp true
  sleep 10
  apt-get update -y

  apt-get install -y \
    curl \
    git \
    ca-certificates \
    gnupg \
    lsb-release

  install -m 0755 -d /etc/apt/keyrings

  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    gpg --dearmor -o /etc/apt/keyrings/docker.gpg

  chmod a+r /etc/apt/keyrings/docker.gpg

  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null

  apt-get update -y

  apt-get install -y docker-ce docker-ce-cli containerd.io

  systemctl enable docker
  systemctl start docker

  usermod -aG docker vagrant

  curl -sfL https://get.k3s.io | sh -

  sleep 30

  mkdir -p /home/vagrant/.kube

  cp /etc/rancher/k3s/k3s.yaml /home/vagrant/.kube/config

  chown -R vagrant:vagrant /home/vagrant/.kube

  chmod 600 /home/vagrant/.kube/config

  echo 'export KUBECONFIG=/home/vagrant/.kube/config' >> /home/vagrant/.bashrc

  echo "Provisioning complete"

SHELL

end
