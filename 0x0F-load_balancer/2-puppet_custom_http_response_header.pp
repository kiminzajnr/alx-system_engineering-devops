# automate task of creating a custom HTTP header response with puppet

exec { 'create custom':
  command  => 'INDEX_COPY="Holberton School for the win!" && ERROR_COPY="Ceci n\'est pas une page - 404" && sudo apt-get -y update && sudo apt-get -y install nginx && echo "$INDEX_COPY" | sudo tee /var/www/html/index.nginx-debian.html > /dev/null && echo "$ERROR_COPY" | sudo tee /var/www/html/custom_404.html > /dev/null && sudo sed -i \'/^\sserver_name.*/a \        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\' /etc/nginx/sites-available/default && sudo sed -i \'/^\slocation.*/i \        error_page 404 /custom_404.html;\' /etc/nginx/sites-available/default && sudo sed -i \'/^\slocation.*/i \        add_header X-Served-By $hostname;\' /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell,
}
