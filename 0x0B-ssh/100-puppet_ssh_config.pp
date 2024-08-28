# Sets up client SSH configuration file to connect without password

exec { 'modify_ssh_config_file':
  command => 'echo -e "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> etc/ssh/ssh_config',
  path    => '/bin/:/usr/bin',
  return  => [0,1],
}
