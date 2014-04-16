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
1) vagrant init precise32
2) vagrant box add precise32 http://files.vagrantup.com/precise32.box
3) vagrant up
4) vagrant ssh
* by default, vagrant will share the folder with the vagrantfile 

install dependecies:
1) sudo apt-get install python-pip
2) sudo pip install ipython
3) sudo pip install Django
4) sudo pip install selenium
run headless firefox(http://www.installationpage.com/selenium/how-to-run-selenium-headless-firefox-in-ubuntu/):
5) sudo apt-get install xvfb
6) sudo apt-get install firefox

after installs run commands in different concurrent sessions:
launch display:
1) sudo Xvfb :10 -ac

launch firefox:
1) export DISPLAY=:10
2) firefox

now can run programs!


