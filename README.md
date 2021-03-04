# User authentication of Open edX using Auth0

This package is available for Auth0 service to authenticate users for edX.


## Install

`sudo su - edxapp -s /bin/bash`

`cd`

`source edxapp_env`

`git clone https://github.com/kratik-perpetualny/openedx_auth0`

`pip install -e openedx_auth0/`


## Add parameters

### For latest KOA Release

Edit your lms.yml (**Path** - _/edx/etc/lms.yml_ ) file in following format -

| KEY  | VALUE | FIELD_TYPE | YAML_FIELD_LOCATION |
| ------------- | ------------- | ------------- | ------------- |
|  ADDL_INSTALLED_APPS | auth0  | LIST  | ROOT_NODE  |
|  THIRD_PARTY_AUTH_BACKENDS | auth0.auth0.Auth0OAuth2  | LIST  | ROOT_NODE  |
|  AUTH0_DOMAIN | **CopyThisFromYourAuth0Console**  | Key-Value Pair  | in **FEATURES**  |
|  ENABLE_THIRD_PARTY_AUTH |  true | Boolean  | in **FEATURES**  |

*I had to create ADDL_INSTALLED_APPS key as it was not existing before

*Also Keep your ClientID & ClientSecret ready.

### For Older Releases

In `lms.env.json`  file:

- `"ADDL_INSTALLED_APPS": ["openedx_auth0"]` to the root node.

- `"THIRD_PARTY_AUTH_BACKENDS": ["openedx_auth0.auth0.Auth0OAuth2"]` to the root node.

- `"AUTH0_DOMAIN": "your.auth0.domain"` to the list of `FEATURES`.

- `"ENABLE_THIRD_PARTY_AUTH": true` in the list of `FEATURES`.


## Migrate DB

### For Native Koa Releases

Keep your Shell ready first
```
sudo su - edxapp -s /bin/bash
cd
source edxapp_env
```
Then makemigrations command
```
python /edx/app/edxapp/edx-platform/manage.py lms makemigrations --settings=production
```
and finally run migrations
```
~/edx-platform$ python /edx/app/edxapp/edx-platform/manage.py lms migrate --migrate --settings=production
```

### For Others (Not Tried)

```
~$ cd /edx/app/edxapp/edx-platform
```

```
~/edx-platform$ python /edx/app/edxapp/edx-platform/manage.py lms syncdb --migrate --settings=aws
```


## Restart edxapp

### Koa
```
sudo /edx/bin/supervisorctl restart lms cms
```
### Older Versions
`sudo /edx/bin/supervisorctl restart edxapp:`


## Configuration from Django's Admin Panel (for third-party authentication backend)

Go to `Your_LMS_URL/admin/third_party_auth/oauth2providerconfig/`

### OR 

Open URL `/admin` on Browser.

Go to `Home › Third_Party_Auth › Provider Configuration (OAuth)` and click Add Provider Configuration

Make sure `Enabled` checkbox is checked

Make sure `Visible` checkbox is checked

Add a name in the `Name` input, ie. Auth0

Check off `Skip Email Verification` checkbox

Choose `Backend Name`: oa2-auth0

Input your `Client ID` and `Client Secret`

In `Other Settings`, paste this: ```{"SCOPE": ["email openid profile"]}``` this makes sure we can fetch the whole profile from
Auth0 and your email address and other info will be properly populated in registration form


## Inspiration
I think somewhere it is inspired by https://auth0.com/docs/quickstart/webapp/django/01-login#configure-auth0
Good to have a look at this.