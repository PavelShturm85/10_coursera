# Coursera Dump

**The module get courses url from xml, then finds course info  and write course info in file.**

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

*Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.*

```bash
pip install -r requirements.txt # alternatively try pip3
```
# Quickstart
**Ways to use:**
- Have to use  module `coursera.py` after `python3`.
   - You get info about 5 courses in courses_info.xmls by default.
   - You may use argument `--amount` and `--output`, to change the number of courses and the file to save.

Example of script launch on Linux, Python 3.5:


```bash
$ python3 coursera.py -h
usage: coursera.py [-h] [-am AMOUNT] [-out OUTPUT]

Module get courses info.

optional arguments:
  -h, --help            show this help message and exit
  -am AMOUNT, --amount AMOUNT
                        How many courses chek for info.
  -out OUTPUT, --output OUTPUT
                        Where to put the file.

```


```bash
$ python3 coursera.py

```
courses_info.xmls

Course name:	                                           Grade:	    Language:	   Start date:	   Amount week:
Gamification	                                           0 stars	  English	    Starts Dec 04	     6
Dealing With Missing Data	                               3.8 stars	English	    Started Nov 27	   4
Vital Signs: Understanding What the Body Is Telling Us	 0 stars	  English	    Started Nov 27	   6
Modern Art & Ideas	                                     4.6 stars	English	    Started Nov 27	   5
The Evolving Universe	                                   4.6 stars	English	    Starts Dec 18	     5



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
