PostMortem
Deployment leads to error 404.
![Postmortem image](https://github.com/mwangim4786/alx-system_engineering-devops/blob/master/0x19-postmortem/755014.png?raw=true)

Issue Summary
On May 10, 2024 between 14:00 hrs EAT and 15:30 hrs EAT, our sales and marketing departments experienced 404 errors on their portals. These accounted for 25% of the staff in the company that got these errors once logged on to their portals. These failures were triggered by a newly completed deployment on the servers. The staff from these departments reported the incident minutes after the deployment was concluded.

Timeline
At 13:50 hrs EAT on May 10 2024, new changes were introduced to the Nginx server hosting the company's website. At 14:00 hrs EAT the technical department was alerted about 404 errors experienced by sales and marketing departments.
The engineers attributed these errors to the changes made to the system. The system was restored to the previous working state by restoring the backup and investigations into the matter was launched.

Root Cause and Resolution
The cause of the 404 errors was a typo error on the clients directory that points the url to the clients files. These typos were carried forward to the servers after deployment.
Necessary changes were made locally to reflect the correct paths for the urls and deployment was redone.

Corrective and preventative measures
Scripts were drawn and tested to always determine consistency of the naming of folders and files both locally and remotely. 

