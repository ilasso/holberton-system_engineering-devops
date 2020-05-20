# fix ".phpp" to ".php" class-wp-locale
exec { 'fixer':
    command  => 'sed -i "s|class-wp-locale.phpp|class-wp-locale.php|g" /var/www/html/wp-settings.php',
    provider => shell,
}
