# honeyswarm_wordpress
Wordpress honeypot with HPFeeds for honeyswarm


- Uses Alpine with Apache PHP
- Configured for SQLite not MYSQL to keep the container small and lightwight. 


### wp-config.php

Any changes to the wordpress installation must ensure the following is set

```
/* This is to automatically update the IP and Port for any deployment */
define('WP_SITEURL', 'http://' . $_SERVER['HTTP_HOST']);
define('WP_HOME', 'http://' . $_SERVER['HTTP_HOST']);
```