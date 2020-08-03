#exec a command : killing a process
exec {'killing a process':
  command => 'kill $(pgrep -f killmenow)',
  path     => '/usr/bin/',
}
