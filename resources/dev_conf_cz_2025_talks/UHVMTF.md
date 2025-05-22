# Understanding programmable system call security with Secomp-eBPF in Linux.

**Speakers:** Kiran Kashinath Belle, Ravina R. Jain
                    
**Track:** Linux Distributions, Operating Systems, and Edge
                    
**Room:** 32
                    
**Date & Time:** 2025-06-14 12:30:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
In today's computing world, protecting userspace applications is essential to mitigate security threats. The Linux kernel exposes approximately 400 system calls, each creating a potential vulnerability window that attackers could exploit to compromise application stability. 

BPF, Berkeley Packet Filter program can be used to observe events across a system and report information about those events to user space tools. Secure Computing-eBPF provides a mechanism to restrict the system calls that an application can make to the kernel. The fundamental concept involves implementing system call filtering based on both system call numbers and their arguments. Through this approach, security policies can precisely define which system calls should be permitted or prohibited, with filters making runtime decisions.

In this session, we will examine the implementation of seccomp-eBPF for improving application security, demonstrating how to create effective filtering rules that protect user space applications without compromising functionality or performance. We will cover practical demonstrations, use cases, common pitfalls to avoid, and techniques for balancing security with application requirements. 

Attendees will gain insights into Linux system security for applications against kernel-level exploits through system call restrictions.
