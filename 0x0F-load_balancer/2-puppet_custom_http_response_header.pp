exec{ 'Updating Repostories':
  provider => shell,
  command => 'sudo apt-get -y update',
  before => Exec['Installing nginx'],
}
exec{ 'Installing nginx':
  provider => shell,
  command => 'sudo apt-get -y install nginx',
  before => Exec['add_header'],
}
exec { 'add_header':
  provider    => shell,
  environment => ["HOSTNAME=${hostname}"],
    command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf',
  before      => Exec['Nginx Restaring'],
}
exec { 'Nginx Restaring':
  provider => shell,
  command  => 'sudo service nginx restart',
}
