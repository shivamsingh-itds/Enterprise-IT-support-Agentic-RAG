# ShivTech IT Service Desk Runbook

## Email Troubleshooting
If a user cannot send or receive email, confirm whether the issue affects one user or many users. Check network connectivity and the service status dashboard. For a single user, sign out and back in, verify mailbox quota, and test the web client. For widespread incidents, do not ask each user to reinstall software; escalate the suspected service incident.

## Laptop Performance
For a slow laptop, first check CPU, memory, storage free space, startup applications, operating system updates, and endpoint security scan status. Do not disable security agents as a troubleshooting shortcut. Escalate when hardware diagnostics report failure or repeated shutdowns continue after software remediation.

## Ticket Priority
P1: Company-wide outage or critical security incident. P2: Major team blocked with no workaround. P3: Individual user blocked or degraded with limited workaround. P4: Standard request, information request, or low-impact issue.

## VPN Connection Issues
When a user cannot connect to the ShivTech VPN, verify internet connectivity and confirm that the VPN client is running. Check whether the user account is active and MFA authentication is successful. Ask the user to restart the VPN client and try an approved corporate gateway. If multiple employees report the same issue, check for a possible VPN service outage and escalate to the network team.

## Password and Account Lockout
When a user cannot log in, verify the username and check whether the account is locked or disabled. Guide the user through the self-service password reset portal. If the account remains locked after a password reset, escalate to the identity management team. Never request or record the user's password or MFA code.

## MFA Authentication Failure
If MFA authentication fails, confirm that the user is using the registered authentication method and that their device has internet connectivity. Check whether the authentication service is operational. If the user has changed or lost their phone, follow the approved identity verification and MFA re-registration process. Escalate repeated authentication failures to the identity management team.

## Microsoft Teams Issues
If Teams is not connecting or messages are not syncing, check the Microsoft 365 service status and network connectivity. Ask the user to sign out and sign back in, restart Teams, and verify that the application is updated. For audio or video issues, check device permissions and selected input/output devices. Escalate if multiple users experience the same issue.

## Software Installation Requests
When an employee requests software installation, verify the application name, business justification, and manager approval. Confirm whether the software is available in the approved ShivTech Software Portal. If administrative permissions or licensing are required, route the request to the appropriate team. Do not install unauthorized or unlicensed software.

## Wi-Fi and Network Issues
When a user reports network connectivity problems, identify whether the issue affects one device, one department, or the entire office. Check network status, Wi-Fi connectivity, and device configuration. Ask the user to reconnect to the approved corporate network. If several users are affected, escalate to the network operations team instead of troubleshooting each device separately.

## Printer and Scanner Issues
If a printer is not working, check its power status, network connection, paper supply, and error indicators. Verify that the user selected the correct printer and that the print queue is not stuck. Restart the print spooler only according to approved procedures. Escalate recurring hardware or network-related printer failures to the hardware support team.

## Hardware Failure
For hardware issues such as laptop overheating, battery failure, damaged screens, or unexpected shutdowns, collect the device asset ID and issue details. Run approved hardware diagnostics and review the results. If diagnostics indicate hardware failure, assign the ticket to the hardware support team. Do not ask users to open or repair company devices.

## Security Incident Handling
For suspected malware, phishing, unauthorized access, or data leakage, classify the issue as a security incident and follow the incident response procedure. Record the reported symptoms, affected device, user, and time of discovery. Escalate immediately to the IT Security Team. Do not delete suspicious files or attempt independent malware removal unless instructed by the security team.

## Ticket Assignment and Escalation
Assign tickets based on the issue category and the responsible support team. Route network issues to Network Operations, account and MFA issues to Identity Management, hardware issues to Hardware Support, and security incidents to IT Security. Include troubleshooting steps already performed, error messages, screenshots, and relevant timestamps before escalation.

## Ticket Documentation
Every ticket must contain a clear issue summary, affected user, device or application, business impact, troubleshooting steps, and current status. Record all communication and actions taken during troubleshooting. Never include passwords, MFA codes, API keys, or other confidential credentials in ticket notes.

## SLA and Response Management
Monitor tickets according to their assigned priority and the organization's service-level agreements. P1 incidents require immediate attention and escalation. P2 issues should be prioritized because they affect multiple users or important business operations. Keep users informed about progress, delays, and expected next steps. Do not close tickets until the issue is resolved or the user has been informed of the resolution process.

## Incident Communication
For major service disruptions, provide clear updates to affected employees through approved communication channels. Include the affected service, known impact, current status, available workaround, and next update time. Avoid sharing unverified root causes or sensitive technical details. Send a resolution update once the service is restored.

## Ticket Closure
Before closing a ticket, confirm that the issue has been resolved or the requested service has been delivered. Document the resolution, root cause if known, and steps taken. Inform the user and request confirmation when appropriate. If the issue returns, reopen the existing ticket or create a linked incident according to the support process.