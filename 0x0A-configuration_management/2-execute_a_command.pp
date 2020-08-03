#exec a command : killing a process
exec {'kill':
  command  => 'pkill killmenow',
  path     => '/usr/bin/',
}
