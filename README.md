# open-edx athentication with auth0


Now At Work


##Install open edx environment

`sudo su - edxapp -s /bin/bash`

`. edxapp_env`

`pip install -e git+https://github.com/ngi644/openedx_auth0`


##Add parameter

In `lms.env.json` and `cms.env.json`  file:

`"ADDL_INSTALLED_APPS": ["openedx_auth0"],`

 to the root node.


`"AUTH0_DOMAIN": "your.auth0.domain"`

 to the list of `FEATURES`.


##Restart edxapp

`sudo /edx/bin/supervisorctl restart edxapp:`