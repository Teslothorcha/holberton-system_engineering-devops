# fix line 137 on file, unnecesaryp on phpp
exec { 'prueba':
path     => '/usr/bin:/usr/sbin:/bin',
command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.\
php',
provider => 'shell',
}
