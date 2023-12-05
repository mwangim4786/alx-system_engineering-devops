#!/usr/bin/env puppet
# Add a custom HTTP header with Puppet

exec { 'sed':
  command  => 'sudo apt-get -y update && sed -i "s/server_name _;/server_name _;\n        add_header X-Served-By hostname;/" my_dir/default',
  path     => 'my_dir/default',
  provider => shell,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
