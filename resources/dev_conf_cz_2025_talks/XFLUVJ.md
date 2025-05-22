# Inflight Checks: Asynchronous Preflights for a Robust Cloud Service

**Speakers:** Zohar Galor
                    
**Track:** Cloud, Hybrid Cloud, and Hyperscale Infrastructure
                    
**Room:** 33
                    
**Date & Time:** 2025-06-13 14:15:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
Before a request is processed in a cloud service, it often undergoes **preflight checks**—validations that ensure the environment is properly configured to handle it. These checks can verify resource availability, security policies, and other prerequisites, preventing failures down the line. 
However, when performed synchronously, preflight checks can become a major bottleneck, increasing latency and limiting scalability.

In this talk, I’ll share how we transitioned from synchronous preflight checks to asynchronous **inflight checks**, running validations while the request is in motion rather than blocking it upfront. I’ll walk through the requirements that drove this change, the architectural considerations we had to weigh, and the solution we ultimately implemented. If you’re looking for ways to improve performance and scalability in cloud services, this session will provide valuable insights into rethinking traditional validation workflows.
