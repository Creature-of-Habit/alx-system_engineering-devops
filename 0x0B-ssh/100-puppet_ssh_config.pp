# Sets up client SSH configuration file to connect without password

exec { 'modify_id_file':
  command => 'echo "IdentityFile ~/.ssh/school" >> etc/ssh/ssh_config',
  path    => '/bin/:/usr/bin',
}
exec { 'modify_pssw_auth':
  command => 'sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/g" etc/ssh/ssh_config',
  path    => '/bin/:/usr/bin',
}
