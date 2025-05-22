# Serverless MicroVMs for Containerized Applications: Bridging Efficiency, Scalability, and Security

**Speakers:** Nikita Sanjay Patwa, Neeraj Bhatt
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 27
                    
**Date & Time:** 2025-06-13 14:00:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
As the cloud-native ecosystem matures, developers are continuously looking for ways to enhance performance, tighten security, and maximize resource efficiency. Serverless computing—renowned for its automatic scaling and operational simplicity—has emerged as a powerful model for building event-driven workloads. However, traditional serverless platforms often fall short when it comes to providing the level of isolation, control, and security required by multi-tenant or complex applications.

This talk introduces Serverless MicroVMs, a modern approach that combines the agility of containers with the strong isolation of virtual machines. Powered by Firecracker, a lightweight virtual machine monitor purpose-built for secure, fast-booting microVMs, and managed using Ignite, a container-native Firecracker manager, this model delivers the best of both worlds: rapid startup times, minimal overhead, and robust workload isolation.

By running OCI-compliant container images inside microVMs, Ignite allows developers to launch secure, ephemeral workloads with the ease of Docker commands. When integrated with Kubernetes, these microVMs can be orchestrated just like traditional pods, making it possible to run serverless functions and containerized applications side by side—securely and at scale. This architecture enables near-instant VM provisioning, fine-grained resource control, and seamless CI/CD integration, all while preserving the developer experience.

In this session, we’ll explore how microVMs close the gap between containers and traditional VMs in serverless environments. We'll walk through a live demo of deploying Firecracker microVMs using Ignite within a Kubernetes cluster, showcasing how serverless functions can be executed with enhanced security and isolation. We’ll also dive into practical use cases, architectural patterns, and emerging trends in microVM-based serverless computing.

Join us to discover how serverless microVMs—powered by Firecracker, Ignite, and Kubernetes—can reshape your approach to building scalable, secure, and efficient cloud-native applications.
