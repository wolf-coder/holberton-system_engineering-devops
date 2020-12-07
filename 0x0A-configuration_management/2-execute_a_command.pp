#exec a command : killing a process
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}


# ------------------------------------------------------->
# (insert-image (create-image "/home/cuore-pc/Programming/Holberton/Projects/holberton-system_engineering-devops/0x0A-configuration_management/Testing/Revise/Pictures/03.png"))
