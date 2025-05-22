# Breaking Changes Without Breaking Users: Lessons from Packit 1.0

**Speakers:** Maja Massarini
                    
**Track:** Open Track
                    
**Room:** 34
                    
**Date & Time:** 2025-06-13 13:15:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
In Q1 of this year, we released Packit 1.0.0, a significant milestone that included some breaking changes. While version updates are commonplace in software development, reaching 1.0.0 is an important moment for any project, and this particular release presented unique challenges for our ecosystem.

Packit isn't just a standalone CLI tool. It powers a CI service used by numerous projects across the open-source community. This meant that any breaking changes in the core tool could potentially disrupt CI pipelines for several developers.

In this talk, I'll walk through:

The Breaking Changes: A brief overview of what changed in Packit 1.0 and why these changes were necessary for the project's evolution.

Our Mitigation Strategy: How we planned the transition to minimize disruption, including:

 - the deprecation process we implemented months/years before the release
 - our communication strategy with users
 - technical solutions: automate migration process.

Real-world Results: data on how successful our approach was.

Lessons Learned: what worked, what didn't, where we faced some issues.

I'd like to conclude with a structured feedback session where attendees can share their own experiences. Attendees will leave with practical strategies for managing breaking changes in libraries that power services and will help us improve the next Packit release.
