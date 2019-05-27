

# ns3 App Store

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4c56f14285e3439abb7f53a3c6cb6be2)](https://app.codacy.com/app/mishal23/ns-3-AppStore?utm_source=github.com&utm_medium=referral&utm_content=mishal23/ns-3-AppStore&utm_campaign=Badge_Grade_Dashboard)

ns3 App Store is a is a web application for a module database in ns-3. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* accounts (handles user accounts - Sign In, Sign Up etc.)
* profiles (handles user profiles)
* appstore (handles core details of the web app)
* help (handles static pages like about, contact us)
* search (handles free text searching)
* apps (handles navigation of apps)
* backend (handles upload and bake integration of apps)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv appstore`
    2. `$ . appstore/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the wiki/docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
