#!/usr/bin/env bash
# setup web server to deploy web static

if [ ! -e /var/run/nginx.pid ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

sudo echo "
<!DOCTYPE html>
<html>
<head>
</head>
<body>
Holberton School
</body>
</html>
" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '38 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

if [ ! -e /var/run/nginx.pid ]; then
    sudo service nginx restart
fi
