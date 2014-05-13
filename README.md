SciDrive Python Client
==================

A Python module that provides the tools you need to authenticate with, and use the SciDrive's Dropbox API.

Getting started 
---------------
To set up the SciDrive module and install dependencies:

* Run the setup script:

        $ pip install -e git://github.com/dimm0/scidrive-python-client.git#egg=scidrive-python-client
(will make link to sources)
or
        
        $ pip install http://github.com/dimm0/scidrive-python-client/tarball/master
(will extract the project into site-packages)
or

        $ git clone git://github.com/dimm0/scidrive-python-client.git
        
        $ cd scidrive-python-client
        
        $ pip install -e .
(to have a local checked out project folder)

* There are two options to specify user's credentials:

On command line

        -u USER -k KEYSTONE_URL -p PASSWORD

As system variables (.bash_profile file in linux, .profile in mac OS):

        export SS_USER=user
        export SS_KEY=password
        export KEYSTONE_URL=http://login.sciserver.org/keystone/v3

* Query the user info: 

        $ sdrv info
The user account info will be displayed.

* To query the root folder contents, run:

        $ sdrv ls /

There is more information on configuring the script in [Wiki](https://github.com/dimm0/scidrive-python-client/wiki)
