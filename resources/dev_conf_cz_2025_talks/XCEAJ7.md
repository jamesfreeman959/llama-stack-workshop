# OCI Hooks: Enhancing Kubernetes Runtime Management

**Speakers:** Igor Bezukh
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-14 14:00:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
While developing an alternative solution for enabling swap in Kubernetes (wasp-agent [1]) we conducted an in-depth exploration of pod runtime management. 
This talk focuses on a critical yet often overlooked aspect: OCI hooks.

To provide a complete picture, I will cover:

* Container Runtime Interface (CRI) overview and its role in Kubernetes.
* Open Container Initiative (OCI) overview and its relevance.
* How Kubernetes components like kubelet, CRI-O, and runc implement these standards.
* OCI hooks, their practical usage in wasp-agent.
* Pitfalls and alternatives to OCI hooks for runtime customization.

What You’ll Learn:
* A closer look at the Kubernetes node software stack.
* How to leverage OCI hooks for advanced scenarios like cgroup modifications and container debugging.
* Common challenges and alternatives when working with OCI hooks.

By the end of this talk, you’ll gain practical insights into Kubernetes runtime internals and walk away with actionable knowledge to enhance container lifecycle management.

[1] https://github.com/openshift-virtualization/wasp-agent
