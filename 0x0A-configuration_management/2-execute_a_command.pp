#exec a command : killing a process
exec {'pkill':
  command  => 'pkill killmenow',
  path     => '/usr/bin/',
}
