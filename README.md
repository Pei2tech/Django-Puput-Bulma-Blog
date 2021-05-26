Introduction
===========
This demo program is based on [puput](https://github.com/APSL/puput "puput"), a Django app,  to handle the blog. It also uses the [bulma](https://bulma.io/ "bulma") and Vanilla Javascript to replace the bootstrap4 and jquery that puput used for frondend. In order to support markdown, the package, [wagtail-markdown](https://github.com/torchbox/wagtail-markdown "wagtail-markdown"), should be installed.   

Technical background
=================
- Bulma :  The modern CSS framework.
- Puput :  The blog app which is based on Wagtail CMS.
- Overwritting the templates, html and css of Puput to make a simple and clean blog.

The new in the Wagtail CMS admin page
==========
- Easily configure the color of  label, head and  body without modiying code.
- Support background image
- Support markdown in the body. 

Installation
========
**Clone this repository and make a virtual environment**
```
$ git clone  https://github.com/Pei2tech/Django-Puput-Bulma-Demo.git myproject
$ cd myproject
$ python -m venv .venv
$source ./.venv/bin/activate
(.venv)...$
```
**Install dependence packages**
```
(.venv)...$pip install -r requirements.txt
```
**After packages installed, please upgrade the Markdown package**
```
(.venv)...$pip install markdown --upgrade
```
**You may get some incompatible messages, please ignore them.**

Configure Database
=========
```
(.venv)...$cd Myblog
(.venv)...Myblog$python manage.py makemigrations
(.venv)...Myblog$python manage.py migrate
(.venv)...Myblog$python manage.py createsuperuser
```

**please input the user name, email address and password.**

Run on local
=========
```
(.venv)...Myblog$python manage.py runserver
```
Now you can check on the admin page to configure the blog. Just open your browser at  [http://127.0.0.1:8000/cms](http://127.0.0.1:8000/cms).

You may visit [Wagtail Editor’s guide](https://docs.wagtail.io/en/v2.0/editor_manual/index.html "Wagtail Editor’s guide") for the details about how to use Wagtail editor’s dashboard.

Screenshot
=========

![](./stuff/screenshot.png)
