PostMortem
Nginx issue leading to Bad Gateway error (HTTP 502)
![Postmortem humour](https://github.com/abkalkaled/alx-system_engineering-devops/blob/master/0x19-postmortem/postmortem.jpg?raw=true)

Issue Summary

For a duration of 1 hour and 16 minutes on May 12, 2024 between 08:03 UTC and 09:19 UTC, our web server was down due to Nginx configuration issue resulting in a downtime affection and impacting 100% of users

Timeline

08:03 UTC: HTTP 502 (Bad Gateway) error was detected from a monitoring alert received by the staff on call
08:05 UTC: alert was escalated to the engineer by the staff on call of investigation
08:11 UTC: Initial assumption was a possible content delivery network (CDN)  issue, proper caching was ensured and CDN server status confirmed okay
08:42 UTC: a further investigation shows server software issue in the apache2.conf configuration file
09:19 UTC: issue resolved by correcting the bogus addition in the configuration file and service was restored

Root Cause and Resolution

The cause of the 502 error is a conflict in the .htaccess files and apache2.conf
The apache configuration was tested by checking error logs to fix conflict with .htaccess files

Corrective and Preventive measures

Regular configuration review of .htaccess and apache2.conf files for conflicts and syntax error
Test and verify configuration to verify functionality
Use of version control to monitor changes
