# Why OCP networking performances on VMs are suboptimal and how to improve them by 5x

**Speakers:** Paolo Abeni
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-13 12:30:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Openshift can be happily deployed on top of Openstack. If you ever went through such an easy and rewarding task, you have possibly been disappointed by the networking performances of your application.

This talk will deep dive on the root causes - it always boils down to (the lack of) GRO and GSO - and will discuss an ongoing effort to address the relevant bottle-necks both at the kernel and virtio level
