# User authentication of Open edX using Auth0

This package is available for Auth0 service to authenticate users for edX.


## Install

`sudo su - edxapp -s /bin/bash`

`cd ~/`

`. edxapp_env`

`git clone https://github.com/ngi644/openedx_auth0`

`pip install -e openedx_auth0/`


## Add parameters

In `lms.env.json`  file:

- `"ADDL_INSTALLED_APPS": ["openedx_auth0"]` to the root node.

- `"THIRD_PARTY_AUTH_BACKENDS": ["openedx_auth0.auth0.Auth0OAuth2"]` to the root node.

- `"AUTH0_DOMAIN": "your.auth0.domain"` to the list of `FEATURES`.

- `"ENABLE_THIRD_PARTY_AUTH": true` in the list of `FEATURES`.


## Migrate DB

```
~$ cd /edx/app/edxapp/edx-platform
```

```
~/edx-platform$ python /edx/app/edxapp/edx-platform/manage.py lms syncdb --migrate --settings=aws
```


## Restart edxapp

`sudo /edx/bin/supervisorctl restart edxapp:`


## Django's management page, set for third-party authentication backend.

Open URL `/admin` on Browser.
 
 

