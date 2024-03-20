### Configure servers
#### Web-01 and Web-02
1. install nginx  
`sudo apt update && sudo apt install nginx`
2. ensure it running on port 80 using  `ss` command i.e. `sudo ss -tunlp | grep :80`
3. edit the default nginx html page at `/var/www/html/index.nginx-debian.html` and add below instead of the defaults, depending on whether its web-01 or web-02:
```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: linen;
}

h1 {
  color: maroon;
  text-align: center;
}
p {
  text-align: center;
}
</style>
</head>
<body>

<h1>This is web-01</h1>
<p>We are testing nginx for web-01.</p>

</body>
</html>
```

### Configure load balancer
1. install nginx
2. create a new configuration file: `/etc/nginx/sites-available/lb.conf` and add below content into it:
```
upstream mywebservers {
	server 18.207.112.169;
	server 35.175.65.7;
}

server {
	listen 80;
	location / {
		proxy_pass http://mywebservers;
	}
}
```
3. create a soft link for it to be available in sites-enabled  
`sudo ln -s /etc/nginx/sites-available/lb.conf /etc/nginx/sites-enabled/lb.conf`
4. remove the default nginx config file from sites-enabled - you will still have it in sites-available:
`sudo rm /etc/nginx/sites-enabled/default`
5. test for any errors using `sudo nginx -t`
6. reload nginx service `sudo systemctl reload nginx.service`
