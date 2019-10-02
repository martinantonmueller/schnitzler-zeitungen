# schnitzler-zeitungen

a simple django project for interacting with the [Transkribus-API](https://transkribus.eu/wiki/index.php/REST_Interface) to search and read documents hosted and processed by [Transkribus](https://transkribus.eu/Transkribus/)

## install


1. clone the repo `git clone https://github.com/acdh-oeaw/schnitzler-zeitungen.git`
1. create a virtual environment
1. install the dependencies `pip install -r requirements.txt`[1]
1. provide the needed `TRANSKRIBUS` settings in you `{root}/schnitzler-zeitungen/settings/my_settings_file.py`
1. start the developement server `python manage.py runserver --settings=schnitzler-zeitungen.settings.{my_settings_file.py}`


## TRANSKRIBUS-Settings

Basically your user name and password and the ID of the collection you'd like to expose by the current application.

```python
TRANSKRIBUS = {
    "user": "mytranskribususer@whatever.com",
    "pw": "mytranskribuspassword",
    "col_id": "43497",
    "base_url": "https://transkribus.eu/TrpServer/rest"
}
```


[1] the transkribus specific code [acdh-django-transkribus](https://github.com/acdh-oeaw/acdh-django-transkribus.git) is not yet wrapped in a python package. Therefore it needs to be included manually, either by copy pasting or via symlink 
