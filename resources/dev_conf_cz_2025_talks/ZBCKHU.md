# Passkeys through FIDO: How to write your own client?

**Speakers:** Mario Bodemann
                    
**Track:** Security and Compliance
                    
**Room:** 31
                    
**Date & Time:** 2025-06-12 12:30:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Passkeys, the way to get rid of passwords is great and all, but how do they work in detail?
This talk will be exploring the specification FIDO2 which essentially defines WebAuthn, the basis for passkeys.
Expect a quick run through of what a passkey is, how a user uses it, and how a developer could leverage an SDK, or a platform credential provider to create safe and easy credentials using cryptographically save passkeys. 
After this quick overview, we’ll dive down into nitty gritty details on what the SDKs actually do and how you would implement them in your own client. Ultimately, I hope to shed a bit of light on the complete process of creating and asserting credentials, how to create the binary representation to be sent to the platform or authenticator and dive a bit deeper into how an authenticator translates those into another binary representation.
In the end you should have some detailed knowledge of how the Passkeys work and maybe why you should not be writing your own passkey client.
