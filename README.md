VOBox Python Client
==================

A Python module that provides the tools you need to authenticate with, and use the VOBox's Dropbox API.

Getting started 
---------------
To set up the VOBox module and install dependencies:

1.  Run the setup script:

        $ pip install -e git://github.com/dimm0/vobox-python-client.git#egg=vobox-python-client
(will make link to sources)
or
        
        $ pip install http://github.com/dimm0/vobox-python-client/tarball/master
(will extract the project into site-packages)
2.  Start by querying the user info: 

        $ vobox info
This will create a ~/.vobox/vobox_config.cfg config file and request the user to authorize in VO SSO either
using the browser or by opening the URL. When the authorization is done, the user account info will be displayed.

3. To query the root folder contents, run:

        $ vobox metadata /

There is more information on configuring the script in [Wiki](https://github.com/dimm0/vobox-python-client/wiki)
