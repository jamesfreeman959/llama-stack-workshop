# Fighting logs with Log Detective

**Speakers:** Tomas Tomecek, Jiri Podivin
                    
**Track:** Artificial Intelligence and Data Science
                    
**Room:** 30
                    
**Date & Time:** 2025-06-12 11:00:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
The current process of identifying the root cause of a package build failure in Copr or Koji is time-consuming and requires considerable expertise. Log Detective proposes an automated log analysis system to help diagnose such failures and assist maintainers.

Log Detective uses Template Mining and Large Language Models to process your log files. It’s very simple to use, just go to https://logdetective.com/explain, paste a link to your log file, wait one minute and the service will explain that log to you.

Existing models like granite, llama, or mistral can give good feedback on your logs, but they don't understand our specific ecosystem. We are collecting log annotations to train our own models under the CDLA-Permissive-2.0 license. Our aim is to create a service that provides near-perfect explanations and solutions, as if an experienced maintainer was guiding you.

In this talk, we’ll give you an overview of Log Detective, explain the technical decisions and finish with a demo. You shouldn’t miss this talk if you are building software as your job.
