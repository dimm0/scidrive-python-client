SciDrive Python Client
==================

A Python module that provides the tools you need to authenticate with, and use the SciDrive's Dropbox API.

Getting started 
---------------
To set up the SciDrive module and install dependencies:

1.  Run the setup script:

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

2.  Start by querying the user info: 

        $ sdrv info
This will create a `~/.scidrive/scidrive_config.cfg` config file and request the user to authorize in VO SSO either
using the browser or by opening the URL. When the authorization is done, the user account info will be displayed.

3. To query the current folder contents (/vosync by default), run:

        $ sdrv ls /

There is more information on configuring the script in [Wiki](https://github.com/dimm0/scidrive-python-client/wiki)
