# Practical experiences with OpenStack on OpenShift

**Speakers:** Jack Henschel, Sven Kieske
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-13 16:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Running an OpenShift Baremetal cluster is a challenging task in itself - so why not add OpenStack on top of it? This brand-new deployment model for the well-known Infrastructure-as-a-Service (IaaS) project offers the ability to quickly bootstrap OpenStack environments, save computing resources and easier operations for administrators - in theory.

In practice, we have found that orchestrating baremetal servers from inside a Kubernetes cluster requires knowledge of many moving pieces at various layers. Nevertheless, for organizations already comfortable with OpenShift, this approach provides a more familiar way to deploy and manage OpenStack without needing to become OpenStack wizards themselves.

In this technical session we want to share what we have learned while building such a solution for our customer.

We will talk about:

* Architecture overview for Red Hat OpenStack Services on OpenShift (RHOSO)
* Provisioning baremetal machines with Kubernetes operators (Metal3)
* Bootstrapping OpenStack control planes and data planes
* Automating this setup with infrastructure as code (GitOps anyone?)
* The challenges of hardware networking (IP address pools, bonds, VLANs, oh my!)
* Day 2 operations: living with the monster you’ve built
* How to avoid shooting your own foot (Gotchas)

**Who should attend**: DevOps and Platform engineers, system administrators managing on-premises infrastructure, and brave souls who enjoy juggling complex distributed systems while maintaining their sanity.

**Why attend**: Whether you're planning a similar deployment, curious about advanced OpenShift/OpenStack architectures, or simply enjoy watching others navigate treacherous waters so you don't have to, you'll walk away with practical insights and hard-won wisdom that no documentation will ever tell you.
