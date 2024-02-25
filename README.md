To use this program you need to create and activate virtual enveiroment

$ python3 -m venv venv
$ source ./venv/bin/activate

Then, you need to instal the packages:

$ pip install -r requirements.txt

After this, just run the file named "main.py"

$ (venv)- main.py

In linux is need this package for PyAudio to work

$ sudo apt-get install portaudio19-dev
$ sudo apt-get install python3-pyaudio
