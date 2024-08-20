# Changes `.phpp` extensions to `.php` in 'wp-settings.php`.

exec { '500-error-fix':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin'],
  unless  => 'grep -q "php" /var/www/html/wp-settings.php',
}

