# Encrypted DNS from Boot to Runtime: A Zero Trust Milestone in RHEL

**Speakers:** Triviño, Pavel Březina
                    
**Track:** Security and Compliance
                    
**Room:** 32
                    
**Date & Time:** 2025-06-13 15:30:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
As cybersecurity threats evolve, securing DNS traffic is a crucial step in achieving a Zero Trust Architecture (ZTA). To mitigate data leaks and unauthorized access, RHEL is integrating Encrypted DNS (eDNS) support, ensuring DNS queries are encrypted already during installation and boot using modern protocols such as DNS over TLS (DoT).

This presentation will cover the journey of enabling eDNS in RHEL, from the initial motivations to the technical challenges that shaped its implementation. Securing DNS at the operating system level required coordinated updates across several components, including FreeIPA, SSSD, Bind, Unbound, NetworkManager, and the newly introduced dnsconfd. Additionally, we made significant changes to core infrastructure in Anaconda, dracut, and OpenSSL to ensure encrypted DNS is available not only during runtime but also during system installation and early boot.

Attendees will gain technical insights into the rationale behind key architectural decisions and how RHEL enables system-wide encrypted DNS without requiring modifications at the application level. We will also delve into the complexities of certificate management for secure DNS communication, which is essential in environments with strict security requirements.

Looking ahead, we will outline RHEL’s roadmap for eDNS, including further enhancements, and upstream collaboration. Join us to learn how Red Hat is making Zero Trust a reality for Linux users.
