# create a file in /tmp:

$str = 'I love Puppet'

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => www-data,
  content => $str,
}

