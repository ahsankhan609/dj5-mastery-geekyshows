# dj5-mastery-geekyshows

Django 5 Mastery Course from Beginners to Advance course is designed by GeekyShows(Youtube Channel).

---

## Course Resources

- [Django 5 Mastery - GeekyShows](https://www.youtube.com/playlist?list=PLbGui_ZYuhigUfO47FLx4ocfmo1071hlc)
- [UV Integration with Django | Streamline dependency management for Django projects](https://www.youtube.com/watch?v=66KWHSjNnA0)
- [Working with UV in Django Project](https://www.youtube.com/watch?v=EMLpt1SmpU0)

---

### Inititae Project with uv

```bash
# Initialize django project with specific python version
uv init django_project_name --python=3.12
```

```bash
# Initialize django project with general and development dependencies only
# if we have .venv already, then delete it, and then create new with this command
uv sync --non-group dev --group prod
```

```bash
#add django package to uv
uv add django==5.2
uv add Pillow
```

```bash
# create django project with uv
uv run django-admin startproject main .
```

```bash
# add django app with uv
uv run manage.py startapp myapp
```

```bash
# run django server with uv on specific port, if we did'nt specify port it will run on default port 8000
uv run manage.py runserver 5500
```

```bash
# run default migrations
uv run manage.py migrate
```

```bash
# run django model migrations
uv run manage.py makemigrations
```

```bash
# create superuser for django admin pannel
uv run manage.py createsuperuser
```

```bash
# adding dependencies list to uv. 
# By-default toml file have general dependency list. 
# But we can add specific dependencies list for development and production.

uv add psycopg2-binary # general dependency
uv add --dev colorama # development dependency
uv add --group prod gunicorn # production dependency
```
