#Increases the number of file limits on holberton user

exec { 'hard_limits':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 3000/g" /etc/security/limits.conf',
  path    => '/bin/:/usr/bin/',
}
exec { 'soft_limits':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 3000/g" /etc/security/limits.conf',
  path    => '/bin/:/usr/bin/',
}
