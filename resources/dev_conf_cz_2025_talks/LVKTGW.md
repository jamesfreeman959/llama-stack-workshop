# Kubernetes Networking: One Size Doesn’t Fit All

**Speakers:** Surya Seetharaman, Miguel Duarte Barroso
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 35
                    
**Date & Time:** 2025-06-12 12:30:00
                    
**Duration:** 80 minutes
                    
## Abstract
                    
By default, Kubernetes networking follows an open model—every pod within a cluster is connected to a single, shared network, allowing unrestricted communication. To enforce traffic restrictions, users must manually define Network Policies, which can be complex and cumbersome to design.

But what if we could rethink how Kubernetes networks are designed?

Join our interactive workshop as we challenge conventional Kubernetes networking. Using OVN-Kubernetes (a robust networking solution for Kubernetes) and KubeVirt (a virtual machine orchestrator for Kubernetes), we’ll explore how to create multiple, isolated cluster networks within the same Kubernetes cluster.

Through step-by-step guidance, you’ll learn how to:
✅ Set up a KIND (Kubernetes in Docker) cluster with OVN-Kubernetes and KubeVirt plugins
✅ Create multiple user-defined, isolated networks
✅ Attach workloads (VMs and pods) to these networks
✅ Achieve native workload isolation through network segmentation—without extra policy configurations

This hands-on tutorial will equip you with practical skills to secure Kubernetes workloads easily while meeting high-security standards. No more complex Network Policies—just simple, effective isolation.

Ready to rethink Kubernetes networking? Join us and take control of your cluster’s connectivity! No prior experience required! Just bring your laptop with Podman (or Docker), Kind and Kubectl installed.
