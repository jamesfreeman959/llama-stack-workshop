# Predicting Faulty Validations in Cluster Issue Detection: A Machine Learning Approach

**Speakers:** Liat Pele, Ofir Pele
                    
**Track:** Artificial Intelligence and Data Science
                    
**Room:** 30
                    
**Date & Time:** 2025-06-12 14:00:00
                    
**Duration:** 35 minutes
                    
## Abstract
                    
Our team maintains a large-scale codebase for detecting and predicting issues in clusters, with hundreds of validation rules contributed and regularly updated by SRE engineers. A key challenge is identifying false positives and predicting which validations are most likely to require fixes.

In this research, we analyze validation rules as repeated code patterns, creating a unique dataset for machine learning. We compute numerical descriptors—such as code length, complexity, entropy, and time since introduction—across different Git branches and compare them with historical bug fixes. Preliminary results indicate strong correlations between these factors and validation reliability.

In this talk, we will present our findings using classical machine learning models and benchmark them against modern large language models (LLMs). We will discuss the effectiveness of both approaches, and the potential impact on automated validation quality improvement.
