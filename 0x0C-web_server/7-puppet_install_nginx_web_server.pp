#updating system
exec{ 'Updating Repostories':
  provider => shell,
  command  => 'sudo apt-get -y update',
}
#installing nginx
package{ 'nginx':
  ensure  => 'installed',
  require => Exec['Updating Repostories'],
}
# creating a file in /tmp
file { 'index.nginx-debian.html':
  path    => '/var/www/html/index.nginx-debian.html',
  owner   => root,
  content => 'Holberton School',
  require => Package['nginx'],
}
# creating defaul block with requirements
file { 'default':
  path    => '/etc/nginx/sites-available/default',
  owner   => root,
  content => 'server {
       listen 80 default_server;
       listen [::]:80 default_server;
       root /var/www/html ;
       index index.html index.htm index.nginx-debian.html;
       server_name _;
       location / {
       		try_files $uri $uri/ =301;
	}
}',
  require => File['index.nginx-debian.html'],
}
#restaring nginx
exec { 'Nginx Restaring':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => File['default'],
}
