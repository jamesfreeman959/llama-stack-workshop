# Building a composable IPsec implementation with Rust

**Speakers:** Daiki Ueno
                    
**Track:** Security and Compliance
                    
**Room:** 32
                    
**Date & Time:** 2025-06-13 16:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
IPsec is used as a versatile solution to transparent traffic protection, as it works at L3 and thanks to the the flexible design of the protocol suite. The type of IPsec applications varies from a VPN server for intranet access, to an encrypted mesh network consisting only of managed nodes. On the other hand, the Internet Key Exchange (IKE) protocol, the control plane of the IPsec protocol suite, is typically implemented as a single monolithic daemon covering all the usage scenarios. This architecture sometimes complicates application integration.

In this talk, we will introduce our experimental project to create a modular IKE implementation with Rust, which can be composed at build time and embedded in the applications as a library. That way, it could simplify the IPsec configuration, make it easy to troubleshoot any issues, and minimize the attack surfaces.
