[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=finance_blog
Group=www-data
WorkingDirectory=/home/ubuntu/project/Django_Project
ExecStart=/home/ubuntu/project/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          finance_blog.wsgi:application

[Install]
WantedBy=multi-user.target