# Facial Expression Recognition Experiment

A cognitive experiment build with Flask that runs in the browser.
Participants see a masked face which is progressively unmasked. As soon as they recognize the expression, they hit a button and then decide between multiple possible answers (basic expressions of emotion).

The current version is very crude and should be considered early work-in-progress. However, it is stable and running and we already successfully used it in a controlled lab setting to acquire data from a handful of pilot participants. We aim to develop a more mature back-end for creating different kinds of behavioral experiments in the near future.

## Getting it to run

### Basic Prerequisites
For the following instructions, I am assuming that you are running a Debian or Ubuntu OS. For example, [Ubuntu Server 14.04](http://www.ubuntu.com/server) might be a reasonable choice.
To get started, you will need Python 2.7, [pip](https://pip.pypa.io/en/latest/installing.html) and [virtualenv](https://virtualenv.pypa.io/en/latest/).

### Creating a Virtual Environment
The experiment is programmed in Python using [Flask](http://flask.pocoo.org). You will need to create a virtual environment like so:

```shell
virtualenv flask
```

You should then be able to run:

```shell
flask/bin/pip install -r requirements.txt
```

This should take care of installing all required modules.
Alternatively, you can install all needed libraries by hand, like so:

```shell
flask/bin/pip install flask
flask/bin/pip install numpy
...
```

The most important modules for Web Development are:
- Flask
- Jinja
- Werkzeug
- Tornado

The most important modules for data analysis are:
- Numpy
- Pandas
- Matplotlib
- Seaborn
- pillow/PIL

I think numpy will require some non-python libriaries so you might have to do things like these beforehand (i.e. on Ubuntu Server):

```shell
apt-get install build-essential python-dev
apt-get install libatlas-base-dev gfortran
apt-get install libpng-dev
apt-get install pkg-config
apt-get install libfreetype6-dev
```


### Deployment on your own Server

Getting the site live works by using [Tornado](http://www.tornadoweb.org/en/stable/) which is called in runserver.py. The script for doing this is taken from [this](http://stackoverflow.com/a/8247457) StackOverflow post.

Hence, you should be able to get the site running by typing

```shell
./runserver.py
```

Maybe you will first need to make the file executable

```shell
chmod a+x runserver.py
```

Now, if you type thisismyip:8888 into your browser window (from an client computer of your choice), you should see the site live.
You can find out the IP of your server by typing

```shell
ifconfig
```


## Basic Structure

The logfiles of all participants can be easily downloaded to your local machine by typing:

```shell
scp username@IP:/.../app/static/logfiles/* ./
```
