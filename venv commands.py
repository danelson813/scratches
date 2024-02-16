pip install virtualenv

python -m venv venv # while in project folder

# to activate:
source venv/bin/activate

# Then start installing

# in the tree of venv
|--bin
|  |--activate
|  |--activate.csh 
|  |--activate.fish 
|  |--easy install 
|  |--pip 
|  |--pip3
|  |--pip3.7 
|  |--python -> python3
|  |--python -> /usr/local/bin/python3
|--include
|--lib
|  |--python3.7
|  |--lib
|     |--site-packages
|--pyvenv.cfg
