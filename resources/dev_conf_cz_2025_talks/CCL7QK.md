# Up your SSH security game

**Speakers:** Allison Karlitskaya
                    
**Track:** Security and Compliance
                    
**Room:** 33
                    
**Date & Time:** 2025-06-12 13:15:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
Since 2020, OpenSSH has supported using widely-available FIDO2 security tokens as the basis for private-key based authentication.  This is supported by the popular Git forges (GitHub, Forĝejo/Codeberg, etc.).  Hardware-based keys have several desirable security properties not shared by private key files: they can't be copied, and they can be configured to require a PIN and a physical touch in order to authenticate.  It's possible to configure Git to require these steps only when pushing (ie: not increasing the friction of clone/fetch/pull).   Many people are still using file/software-based SSH keys because they don't know how easy it is to set this up.  An introduction.
