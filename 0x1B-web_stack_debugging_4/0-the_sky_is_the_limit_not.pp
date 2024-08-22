#Increases the number of file requests

exec{ 'change_ulimits':
        command => 'sed -i "s/-n 15/-n 3000/g" /etc/default/nginx',
        path    => '/bin/:/usr/bin/',
        before  => Exec['restart_nginx'],
}
exec{ 'restart_nginx':
        command => 'sudo service nginx restart',
        path    => '/bin/:/usr/bin',
}
