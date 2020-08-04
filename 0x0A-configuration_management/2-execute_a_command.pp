#exec a command : killing a process
exec {'killmenow':
  command  => 'pkill killmenow',
  provider     => 'shell',
}
