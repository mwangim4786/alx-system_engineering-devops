# Script to make it  possible to login with the holberton user and open a file without any error message.

# Increase hard file limit for holberton user.
exec { 'increase hard limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for holberton user.
exec { 'increase soft limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
