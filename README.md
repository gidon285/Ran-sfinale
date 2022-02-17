
hello and welcome to our sniff and surff project! this part will be completed by a 
Machine learning other part that will take the data
and make predictions!

to start the project please read the instructions!

instructions:

first make sure you have the following installed:

python 3, nodejs, wireshark

now go to this github repo and donwload chromedriver for your system.

https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.102/

(make sure you have chrome version 98 installed)

sudo cp chromedriver /usr/local/bin (use this command in therminal in the driver location)

this will copy said chromedriver to the given location.

now we need to set up nodejs and npm,

sudo apt install nodejs

sudo apt install npm

now we need to clear the dependencies. first create a folder and open the therminal, insert

npm init (this will set up npm for you)

then:

npm i selenium-webdriver

npm i selenium-chrome-clear-cache

run the next command:

sudo python3 gen.py

this will start wireshark and the sniffing process and save a file named save.pcap!

now run node main.js and wait(this may take some time - 10 minutes or more.) this will send a lot of get requests!

selenium will visit the 100 most visited websites in the US for reference.

next naviagte to /tmp/ and enter the next command.

sudo cp save.pcap <'dest folder'> where dest folder is our main folder for this project.

close the sniff.py therminal.

and run toJSON.py by typing python3 toJSON.py.(you will need to enter password for tshark operation)

now you have the data.json file, and you are ready to go.


