#Configuring with puppet

exec{ 'Updating Repostories':
  provider => shell,
  command  => 'sudo apt-get -y update',
}
package{ 'nginx':
  ensure   => 'installed',
  require => Exec['Updating Repostories'],
  before   => Exec['add_header'],
}
exec { 'add_header':
  provider    => shell,
  environment => ["HOSTNAME=${hostname}"],
  command     => 'sed -i "44i  add_header X-Served-By \"$HOSTNAME\";" /etc/nginx/sites-available/default',
  before      => Exec['Nginx Restaring'],
}
exec { 'Nginx Restaring':
  provider => shell,
  command  => 'sudo service nginx restart',
}
