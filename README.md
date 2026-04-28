# dj5-mastery-geekyshows

Django 5 Mastery Course from Beginners to Advance course is designed by GeekyShows(Youtube Channel).

---

## Course Resources

- [Django 5 Mastery - GeekyShows](https://www.youtube.com/playlist?list=PLbGui_ZYuhigUfO47FLx4ocfmo1071hlc)
- [Working with UV in Django Project](https://www.youtube.com/watch?v=EMLpt1SmpU0)

---

### Inititae Project with uv

```bash
#add django package to uv
uv add django==5.2
uv add Pillow
```

```bash
# create django project with uv
uv run django-admin startproject myproject .
```

```bash
# run django server with uv on specific port
uv run manage.py runserver 5500
```

```bash
# add django app with uv
uv run manage.py startapp myapp
```
