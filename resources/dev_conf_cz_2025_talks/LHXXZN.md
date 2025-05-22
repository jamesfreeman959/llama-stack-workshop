# Qubes OS: Security Through Isolation

**Speakers:** Lukáš Czerner
                    
**Track:** Linux Distributions, Operating Systems, and Edge
                    
**Room:** 32
                    
**Date & Time:** 2025-06-12 14:45:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Security in modern computing is a mess. Traditional operating systems are fundamentally flawed when it comes to isolation - one compromise can bring down everything. Enter Qubes OS, a security-focused operating system that takes an entirely different approach: compartmentalization. Instead of relying on a single, monolithic system, Qubes OS splits the environment into isolated virtual machines (qubes), ensuring that a breach in one domain doesn't mean total compromise.

In this talk, I will introduce Qubes OS from a technical perspective, breaking down how its architecture works and what makes it different from other operating systems. We'll dive into the mechanics of qube separation, discussing how Qubes leverages Xen hypervisor, inter-qube communication, and how it balances security with usability.

As someone with a background in Linux filesystems, I want to go beyond the basics. This talk will also explore how Qubes OS handles storage - from how it separates user data, system templates, and volatile runtime environments to the specific technologies used under the hood. Expect an in-depth look at LVM, thin provisioning.

Finally, I'll discuss real-world use cases - from developers looking to isolate work environments to security professionals and journalists who need a system built to withstand targeted threats. By the end of this talk, attendees will leave with a solid understanding of Qubes OS, its advantages, and how they can start using it today.

If you've ever wondered whether a truly secure operating system is possible, or if you just love digging into the technical details of system architecture, this session is for you.
