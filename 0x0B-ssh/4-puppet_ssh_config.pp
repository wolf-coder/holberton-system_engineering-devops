#Configuration with pupppet
exec { 'Turn off passwd auth':
  command => 'sed -i \'s/PasswordAuthentication no/PasswordAuthentication yes/g\' /etc/ssh/ssh_config',
  path    => '/bin/'
}
exec { 'Declare identity file':
  command =>'echo -e "\tIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  path    => '/bin/'
}