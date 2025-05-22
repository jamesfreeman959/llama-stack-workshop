# Passwordless authentication: a JSON-Based Approach for modern authentication with SSSD and GNOME

**Speakers:** Iker Pedrosa
                    
**Track:** Security and Compliance
                    
**Room:** 32
                    
**Date & Time:** 2025-06-14 13:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
This presentation explores a novel approach to passwordless authentication in Gnome, leveraging the power of [SSSD](https://sssd.io/) and a newly developed extension to the Pluggable Authentication Module (PAM) conversation. We introduce a JSON-based messaging system that significantly enriches the communication between PAM modules and client applications, enabling sophisticated authentication flows. This enhanced communication facilitates contextual information sharing, adaptive authentication, and seamless multi-factor authentication, all within the familiar GNOME desktop environment.
The talk delves into the technical details of this JSON-based interface between SSSD and [GDM](https://en.wikipedia.org/wiki/GNOME_Display_Manager), providing insights into its [design](https://github.com/SSSD/sssd.io/pull/79) and implementation. Furthermore, a simple PAM rust application will be presented as a practical example, serving as a reference for developers seeking to integrate this protocol into their own PAM applications. This opens up a wide range of possibilities for enhanced authentication flows, including:

* **Contextual information**: sharing user-specific data or authentication challenges.
* **Adaptive authentication**: dynamically adjusting authentication steps.
* **Multi-Factor authentication**: orchestrating complex authentication sequences.

The presentation will conclude with live demonstrations showcasing the capabilities of this extended PAM conversation and its potential for innovation in authentication systems.
We will also share the current development status and preliminary GUI designs, subject to ongoing development progress.
