# Black box side-channel leakage verification using statistical approach

**Speakers:** Alicja Kario
                    
**Track:** Security and Compliance
                    
**Room:** 31
                    
**Date & Time:** 2025-06-12 10:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Side-channel attacks are a common threat to cryptographic implementations. Unfortunately, most available tooling to combat this threat has limited usability, especially in black-box testing scenarios. This talk presents lessons learned from testing RSA implementations (Marvin Attack), ECDSA implementations (Minerva vulnerability), and how these lessons have been applied to test ML-KEM.

The talk will briefly discuss issues with approaches used by Box Test, TVLA, and deduct, and how these issues can be addressed. The proposed approach is suitable for black-box testing, including with algorithms that use rejection sampling. It is algorithm- and architecture-agnostic, can be performed remotely (over a network), and, despite using statistical methods, allows for verification of the absence of side-channel leakage. The tool, presented as free open-source software, has been used in the speaker’s CI system for a couple of years.
