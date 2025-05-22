# Post Quantum Crypto in Practice: Real-World Implementation with Firefox, OpenSSL, and Rust-Based Solutions

**Speakers:** Sahana Prasad, Nicola Tuveri, Akif Mehmood
                    
**Track:** Security and Compliance
                    
**Room:** 36
                    
**Date & Time:** 2025-06-13 10:15:00
                    
**Duration:** 80 minutes
                    
## Abstract
                    
As post-quantum cryptography (PQC) continues to evolve, ensuring a smooth and adaptable transition for end users, developers, and system administrators remains a top priority. Building on discussions from the last DevConf and the latest NIST recommendations, this session presents recent updates in the Fedora ecosystem with cryptographic components, including crypto-policies, demonstrating real-world PQC integration.
Our live demo will showcase a familiar user experience — a routine Firefox browsing session — that seamlessly incorporates PQC. By inspecting the security tab when connecting to a web server, we illustrate how the user experience remains intentionally "boring," signaling a successful, non-disruptive deployment of advanced cryptographic protocols. Beneath this simplicity, however, lies a powerful infrastructure of client-side and server-side components.
On the client side, we employ a nightly build of Firefox enhanced with PQC authentication and key exchange capabilities, made possible through Qryoptic — a rust based soft-token derived from the Kryoptic project — loaded alongside Firefox's default NSS soft-token. On the server side, we leverage vanilla nginx running over OpenSSL 3.2 with our Aurora provider, a rust written OpenSSL Provider designed to boost cryptographic agility by allowing flexible backend implementations for PQC primitives.
While some of these results could be approximated using vanilla Firefox and OpenSSL with the oqsprovider, our approach enhances cryptographic agility through shallow loadable modules — decoupling stable systems from rapidly evolving PQC ecosystems. Beyond the demo, we’ll dive into the experience of writing OpenSSL Providers in Rust and explore how open-source efforts like Kryoptic can be customized to build experimental PKCS#11 soft-tokens, offering valuable tools for developers and security researchers.
Concluding the session, we’ll discuss the broader methodology behind these efforts and how shallow loadable modules can empower users, sysadmins, developers, and cryptographers alike to achieve greater flexibility and security in a post-quantum world.
