# Kills a process named killmenow

exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
