# Keylime: Pushing the Boundaries of Remote Attestation on the Edge

**Speakers:** Anderson Toshiyuki Sasaki
                    
**Track:** Security and Compliance
                    
**Room:** 32
                    
**Date & Time:** 2025-06-12 16:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Keylime is a TPM-based remote attestation framework that originally relied on a pull model, where the verifier initiated attestation requests to monitored systems. However, this approach posed challenges for edge and IoT environments, where devices often operate with constrained resources and behind firewalls.

In this talk, we’ll dive into the transition from a pull-based model to a push-based (agent-driven) attestation model, where the agent on the monitored system actively pushes integrity measurements to the verifier. We’ll explore the architectural changes, the technical challenges we tackled, and how this shift makes remote attestation more practical for edge, cloud, and IoT deployments.

Additionally, we’ll highlight how this work was made possible through open-source collaboration, showcasing not only the technical advancements in Keylime but also the power of open-source development in solving real-world security challenges.
