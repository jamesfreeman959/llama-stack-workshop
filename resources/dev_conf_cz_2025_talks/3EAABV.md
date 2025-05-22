# Multi-Cluster Networking: A Technology-Agnostic Network Operator for Kubernetes Federation

**Speakers:** Ryan Jenkins
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 33
                    
**Date & Time:** 2025-06-14 15:15:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
As organizations scale their Kubernetes deployments across multiple clusters, seamless inter-cluster communication becomes a critical challenge. Traditional approaches rely on complex service meshes, VPNs, or manual configurations, making them difficult to manage and scale. To address this, we have developed a technology-agnostic Network Operator that automates federated network configuration in Kubernetes, enabling secure, application-level connectivity across clusters.

Our operator currently integrates with Skupper, but it is designed to be extensible to support other networking technologies such as Submariner and SD-WAN, providing flexibility based on deployment needs. This talk will explore how the operator simplifies multi-cluster networking by dynamically provisioning and managing inter-cluster service networks, handling topology changes, ensuring fault tolerance, and reducing operational overhead. Additionally, we will showcase its application in the real-world AC3 EU project, where federated Kubernetes infrastructure was essential for enabling distributed workloads across multiple regions while maintaining security and performance, directly supporting the project's goals.

Attendees will learn best practices for automating federated Kubernetes deployments, key design decisions behind our operator, and lessons from deploying it in production environments. Whether you’re managing hybrid cloud architectures, multi-region applications, or looking to simplify service-to-service connectivity across clusters, this session will provide valuable insights into the future of federated Kubernetes networking.
