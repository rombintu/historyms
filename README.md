# INSTALL
```
git clone https://github.com/rombintu/hystoryms.git
cd hystoryms
cp .secrets.yaml.bak .secrets.yaml
cp settings.yaml.bak settings.yaml
vim .secrets.yaml
vim settings.yaml
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations main
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Links 
[Mssql-docker](https://hub.docker.com/_/microsoft-mssql-server)  
[Dynaconf](https://www.dynaconf.com/#using-django)