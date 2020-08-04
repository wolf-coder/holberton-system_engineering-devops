#Configuration with pupppet
exec { 'Turn off passwd auth':
#  command => 'sed -i \'s/PasswordAuthentication no/PasswordAuthentication yes/g\' /tmp/sshd_config ;echo -e "\tIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  path    => '/bin/'
}
