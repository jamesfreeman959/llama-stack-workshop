# Avocado testing framework and how can make your testing easier

**Speakers:** Jan Richter, Harvey Lynden
                    
**Track:** DevOps and Automation
                    
**Room:** 31
                    
**Date & Time:** 2025-06-14 14:45:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
The talk will introduce the main features of Avocado testing framework (https://avocado-framework.readthedocs.io/en/latest/index.html), which is an open-source tool for automated testing widely used by open source projects like QEMU, libvirt, SoS and others for their self-tests. While mostly developed in Python, Avocado cares for tests written in virtually any language, but it takes care of finding and running tests written in virtually any language. Through a number of built-in features and an extensible architecture, any and multiple types of tests can be part of your test suite.

During the talk, we will talk about how Avocado features can improve your testing experience by making it better, faster and easier. Avocado allows you to run tests in isolated environments, like containers or virtual machines, to not corrupt your environment while providing  parallel test execution for improved efficiency. Next, Automatic dependency fulfilment to ensure a smooth testing experience. Also offers many output formats for your specific analysis needs. Furthermore, Avocado supports variant generation to facilitate combinatorial testing; this greatly reduces your test execution time while still providing quality results. And it guarantees reproducibility.

The second part of the presentation will focus on  "autils" (Avocado Utils), a new standalone repository that aims to unlock the full potential of Avocado's system-level utilities. Currently, these powerful utilities are embedded within Avocado and Avocado-VT, limiting their accessibility and leading to code duplication. The aautils project (to be hosted at avocado-project/aautils on GitHub and distributed as aautils on PyPI) will create a central hub for these system-level utilities, making them available to any project that needs to interact with system-level features and interfaces. This initiative reinforces Avocado's language-agnostic philosophy by separating these utilities from the Python-centric test framework. By lowering the barrier to entry - no longer requiring the full Avocado framework as a dependency - we expect to see increased adoption and collaboration from developers who can benefit from these battle-tested tools for their day-to-day tasks. Drawing inspiration from the success of focused projects like "avocado-misc-tests", aautils will foster its own community of contributors and users, leading to improved quality and broader applications of these essential utilities.
