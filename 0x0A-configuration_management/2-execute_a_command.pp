# Kill process with puppet
exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
}
