# Kill process with puppet
exec { 'restart_process':
  command  => 'pkill -f killmenow',
  provider => 'shell',
}
