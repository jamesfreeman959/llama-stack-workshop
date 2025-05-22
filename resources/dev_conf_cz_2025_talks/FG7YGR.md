# Flying Bug-Free: Scalable Blue-Green Deployment & Canary Releases in Airline Systems

**Speakers:** shivang, Shailendra Kumar Singh, abhinav srivastava
                    
**Track:** DevOps and Automation
                    
**Room:** 31
                    
**Date & Time:** 2025-06-14 13:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
To ensure high availability (HA) and risk-free deployments in airline systems, a multi-cluster active-active architecture is implemented using Kubernetes/OpenShift. Both clusters serve as production environments, with one designated as the Canary Release Cluster, allowing new versions to be tested with controlled traffic before full rollout. Load Balancer is responsible for dynamically managing traffic flow between clusters, ensuring a seamless and scalable deployment strategy.

Key Topics Covered:
• HA Active-Active Multi-Cluster Model: How Kubernetes/OpenShift clusters operate in parallel, balancing live traffic for resilience and scalability.
• Role of Load Balancer in Traffic Management: How Load Balancer intelligently routes user requests, gradually shifting traffic from the stable production cluster to the Canary Release Cluster.
• Canary Release Process in Kubernetes/OpenShift: Deploying new versions incrementally with real-time monitoring, rollback mechanisms, and traffic percentage control.
• CI/CD Automation with GitOps: Using Jenkins, GitOps, and a hub cluster to orchestrate deployments across multiple OpenShift/Kubernetes clusters.
• Monitoring & Observability: Leveraging Prometheus, Grafana, and automated rollback triggers to ensure performance and system stability.
• Business Impact: Achieving zero-downtime deployments, improved reliability, and faster feature delivery while reducing the risk of production failures.
