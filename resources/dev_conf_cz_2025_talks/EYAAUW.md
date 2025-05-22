# Click-Click and Kubernetes: Kubernetes-in-Kubernetes with Kamaji, KubeVirt, and the Cluster API

**Speakers:** Andrei Kvapil
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-14 13:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
The Cluster API provides a standardized method for the creation and management of multiple clusters, controllable directly from another Kubernetes instance. But, is it possible to use it without a cloud, on your own bare-metal infrastructure? Yes, you can!

Explore how to implement Cluster API for bare-metal setups and deploy Kubernetes clusters within Kubernetes using the Kamaji and KubeVirt projects.
We'll discuss:

- The architecture of the Cluster API
- Running Kubernetes control plane as containers with Kamaji
- Running Kubernetes worker nodes as VMs using KubeVirt
- Delivering updates and system components into tenant clusters
- The Cluster Autoscaler implementation
- Storage: how to organize dynamic volume provisioning
- Networking: routing traffic into tenant clusters
- Security: how to separate tenants from each other and management cluster
