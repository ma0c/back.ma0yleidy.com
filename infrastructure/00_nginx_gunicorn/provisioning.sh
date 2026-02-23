#!/usr/bin/env bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y \
  python3 \
  python3.12-venv \
  git \
  postgresql-client-common \
  libpq-dev \
  postgresql-client-16 \
  direnv \
  nginx \
  gunicorn
mkdir -p projects
cd projects
git clone https://github.com/ma0c/back.ma0yleidy.com.git
cd back.ma0yleidy.com/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure gunicorn
sudo su
touch /etc/systemd/system/gunicorn.socket
mkdir -p /etc/gunicorn

cat > /etc/gunicorn/back.ma0yleidy.com.conf <<EOL
# Replace the content of this file with the content on back.ma0yleidy.com.conf
EOL

cat > /etc/systemd/system/gunicorn.socket <<EOL
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
EOL

cat > /etc/systemd/system/gunicorn.service <<EOL
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
EnvironmentFile=/etc/gunicorn/back.ma0yleidy.com.conf
WorkingDirectory=/home/ubuntu/projects/back.ma0yleidy.com
ExecStart=/home/ubuntu/projects/back.ma0yleidy.com/venv/bin/gunicorn \
          --access-logfile - \
          --capture-output \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          ma0yleidy_back.wsgi:application

[Install]
WantedBy=multi-user.target
EOL
exit
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

sudo systemctl status gunicorn.socket

file /run/gunicorn.sock
sudo journalctl -u gunicorn.socket

# Reload gunicorn
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

cat > /etc/nginx/sites-available/back.ma0yleidy.com <<EOL
server {
    listen 80;
    server_name back.ma0yleidy.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/projects/back.ma0yleidy.com;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

    }
}
EOL

sudo ln -s /etc/nginx/sites-available/back.ma0yleidy.com /etc/nginx/sites-enabled/

sudo nginx -t
sudo systemctl restart nginx

sudo usermod -a -G ubuntu www-data
sudo chown -R :www-data /home/ubuntu/projects/back.ma0yleidy.com/static



# using https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu#step-7-creating-systemd-socket-and-service-files-for-gunicorn