web: python manage.py collectstatic --no-input && python manage.py migrate && gunicorn -b 0.0.0.0:$PORT meta_inventory_control.wsgi --log-level debug