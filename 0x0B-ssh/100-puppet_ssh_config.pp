#Configuration with pupppet
exec { 'Turn off passwd auth':
  command  => 'echo -e "\tPasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
exec { 'Declare identity file':
  command  =>'echo -e "\tIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
