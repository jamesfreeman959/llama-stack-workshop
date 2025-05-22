# Image Mode Support in Testing Farm

**Speakers:** Jan Havlín, Miroslav Vadkerti
                    
**Track:** Linux Distributions, Operating Systems, and Edge
                    
**Room:** 32
                    
**Date & Time:** 2025-06-13 13:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Image mode for RHEL, Fedora, and CentOS Stream is an important new deployment method for these operating systems. Ensuring that they are validated as a part of standard development workflows is crucial, and lowering the testing entry barrier for these variations is a key priority. This means they must receive first-class support in tmt and Testing Farm, which form the standard tooling and infrastructure for testing Fedora, RHEL, and CentOS Stream.

In this talk, we will dive into the details of Image Mode support in Testing Farm. We will explain:
* How Testing Farm and tmt prepare the testing environment for test execution.
* How to enable Image Mode testing alongside package mode testing for all available CI systems.
* How to quickly reserve a machine with Image Mode for testing and debugging purposes.
* How to easily execute existing tests against Image Mode.

More information on Image Mode support: https://docs.testing-farm.io/Testing%20Farm/0.1/rfd/rfd5-testing-image-mode.html
