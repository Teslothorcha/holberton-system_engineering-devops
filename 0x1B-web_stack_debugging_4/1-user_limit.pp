# incremetn limit fle opening
exec { 'increment fd limit':
path     => '/usr/bin:/usr/sbin:/bin',
provider => 'shell',
command  => 'sed -i "/nofile/c\nofile   1000" /etc/security/limits.conf',
}
