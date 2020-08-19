exec{ 'apt-get update':
  command => '/usr/bin/apt-get update',
}
package{ 'nginx':
  ensure => 'installed',
  require => Exec['apt-get update'],
}
exec { 'add_header':
  provider    => shell,
  command     => 'sed -i "44i  add_header X-Served-By  ""$HOSTNAME"";" /etc/nginx/sites-available/default',
  before      => Exec['Nginx Restaring'],
}
exec { 'Nginx Restaring':
  provider => shell,
  command  => 'sudo service nginx restart',
}
