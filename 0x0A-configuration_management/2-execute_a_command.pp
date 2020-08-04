#exec a command : killing a process
exec { 'kidllmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
