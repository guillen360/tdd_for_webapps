from pycon 2014:
http://pyvideo.org/video/2580/tdd-for-web-applications-from-scratch

building a todo lists app using tdd
using django


dependencies:
python2.7
django 1.5
selenium

building vm using vagrant:
https://docs.vagrantup.com/v2/getting-started/boxes.html
1) vagrant box add hashicorp/precise32
2) mod vagrantfile:
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise32"
end

3) vagrant up
4) vagrant ssh

* by default, vagrant will share the folder with the vagrantfile 



