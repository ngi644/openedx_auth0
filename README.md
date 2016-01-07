# User authentication of Open edX using Auth0

This package is available for Auth0 service to authenticate users for edX.


##Install open edx environment

`sudo su - edxapp -s /bin/bash`

`cd ~/`

`. edxapp_env`

`git clone https://github.com/ngi644/openedx_auth0`

`pip install -e openedx_auth0`


##Add parameter

In `lms.env.json` and `cms.env.json`  file:

`"ADDL_INSTALLED_APPS": ["openedx_auth0"],`

 to the root node.


`"AUTH0_DOMAIN": "your.auth0.domain"`

 to the list of `FEATURES`.


##Restart edxapp

`sudo /edx/bin/supervisorctl restart edxapp:`