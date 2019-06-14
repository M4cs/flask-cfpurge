# flask-cfpurge

Automate Purging Your File Cache On Cloudflare To Easily Update Your Webpages

# Usage

Example in flask app's __init__.py:
```
from flask_cfpurge import Purger
from flask import Flask

app = Flask(__name__)

app.cf_auth_key = os.environ.get('CF_AUTH_KEY')
app.cf_email_key = os.environ.get('CF_AUTH_EMAIL')
app.cf_zone = os.environ.get('CF_ZONE')

purger = Purger(app)
purger.purge_all(app.cf_zone)
```

This will run everytime you restart your flask server.