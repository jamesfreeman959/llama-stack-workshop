# Beware of the kernel RTNL mutex

**Speakers:** Toke Høiland-Jørgensen
                    
**Track:** Linux Distributions, Operating Systems, and Edge
                    
**Room:** 32
                    
**Date & Time:** 2025-06-13 11:00:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
The Linux kernel RTNL mutex is the big lock protecting all of the internal kernel data structures related to networking. While there is work underway in the upstream community to reduce its scope, today this mutex is a major source of scalability problems in the kernel networking subsystem. It mostly affects control path operations (such as bringing network interfaces up and down), but unless care is taken to avoid it, RTNL lock issues can also spill over into the data path, causing intermittent stalls in networking applications that can be
hard to debug.

In this talk I will dive into techniques for debugging applications stalls caused by contention on the RTNL lock, using an example application that is derived from a real-world case. We will look at kernel tracing tools that can be used to identify and debug such issues, and talk about ways to mitigate them in the application. I will also briefly outline the upstream efforts to reduce the scope of the RTNL in the kernel, and how this will affect systems going forward.
