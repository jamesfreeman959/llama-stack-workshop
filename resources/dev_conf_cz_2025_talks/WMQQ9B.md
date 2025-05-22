# What Have I Modified in SELinux: a new addition to your SELinux toolbox

**Speakers:** Juraj Marcin
                    
**Track:** Open Track
                    
**Room:** 33
                    
**Date & Time:** 2025-06-12 11:35:00
                    
**Duration:** 15 minutes
                    
## Abstract
                    
Let's be honest: managing a SELinux policy is not the easiest thing in the world. With so many modules, rules, and packages, sometimes it's hard to keep track of every little change you made to prevent that one niche application from crashing. Or even worse, you're not the one who made the changes, and now you're left with a problem to fix.

WhimSE (What Have I Modified in SELinux) is a new tool I developed as my master's thesis and will help you find all whims your SELinux policy has. It scans your current policy and lists changes made compared to a clean policy contained in the installed packages. That includes changed, removed, or added policy modules, modifications introduced via userspace tools (semanage, setsebool, etc.), or manual changes to SELinux configuration files. Distributed SELinux Policy is also supported.
