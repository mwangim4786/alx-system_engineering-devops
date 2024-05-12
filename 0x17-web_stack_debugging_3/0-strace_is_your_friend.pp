# Change file ext. from phpp to php
exec { 'Change filename':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
