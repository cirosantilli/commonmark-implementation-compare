# -*- mode: ruby -*-
# vi: set ft=ruby :

# WARNING: if you use more than one CPU on the guest
# enable hardware virtualization from your BIOS
cpus = '1'
memory = '1024'

# WARNING: if you are going to run a 64 bit guest inside a 32 bit host
# you must enable hardware virtualization from your BIOS
box = 'ubuntu/trusty64'
hostname = 'vagrant-commonmark-implementation-compare'

Vagrant.configure('2') do |config|
  config.vm.box = box
  config.vm.hostname = hostname
  config.vm.provider 'virtualbox' do |v|
    v.customize [
      'modifyvm', :id,
      '--cpus', cpus,
      '--memory', memory,
      '--name', hostname + '_vagrant'
    ]
    if cpus.to_i > 1
      v.customize ['modifyvm', :id, '--ioapic', 'on']
    end
  end
  config.vm.provision :shell, privileged: false, path: 'provision.sh'
end
