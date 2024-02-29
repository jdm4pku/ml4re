# Machine Learning for Requirements Engineering
![GitHub last commit](https://img.shields.io/github/last-commit/jdm4pku/ml4re)

This repository contains a curated list of papers, datasets, and tools that are devoted to research on Machine Learning for Requirements Engineering. 

This repository is referred to [saltudelft/ml4se](https://github.com/saltudelft/ml4se). Next, I will keep adding papers I read、datasets and tools. 

Welcome to send a pull request to add papers and relevant content.

## Content
- [Papers](#papers)
  - [Human Aspects](#human-aspects)
  - [Requirements Elicitation](#requirements-elicitation)
  - [Requirements Modeling](#requirements-modeling)
  - [Requirements Validation](#requirements-validation)
  - [Requirements Specification](#requirements-specification)
  - [Requirements Extraction](#requirements-extraction)
  - [Requirements Classification](#requirements-classification)
  - [Requirements Ambiguity](#requirements-ambiguity)
  - [Requirements Consistency](#requirements-consistency)
  - [Requirements Prioritization](#requirements-prioritization)
  - [Requirements Dependency](#requirements-dependency)
  - [Requirements Changes](#requirements-changes)
  - [Requirements Traceability](#requirements-traceability)
  - [Requirements Generation](#erquirements-generation)
  - [Formal Requirements](#formal-requirements)
  - [Surveys](#surveys)
  - [Misc](#misc)
- [PhD Theses](#phd-theses)
- [Talks](#talks)
- [Datasets](#datasets)
- [Tools](#tools)
- [Research Groups](#research-groups)
- [Venues](#venues)

# Papers

## Human Aspects
- **The Effects of Human Aspects on the Requirements Engineering Process: A Systematic Literature Review** TSE 2022. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9325916)
- **The Influence of Human Aspects on Requirements Engineering-related Activities: Software Practitioners' Perspective** TOSEM 2023. [[pdf]](https://arxiv.org/pdf/2109.07868.pdf)

## Requirements Elicitation
- **Strategies, Benefits and Challenges of App Store-inspired Requirements Elicitation** ICSE 2023. [[pdf]](https://ieeexplore.ieee.org/document/10172539)
- **Towards a Formal Framework for Normative Requirements Elicitation**  ASE 2023. [[pdf]]()
- **ChatGPT Prompt Patterns for Improving Code Quality, Refactoring, Requirements Elicitation, and Software Design** ArXiv 2023. [[pdf]]()
- **Investigating ChatGPT's Potential to Assist in Requirements Elicitation Processes** ArXiv 2023. [[pdf]]()
- **Towards dialogue based, computer aided software requirements elicitation** ArXiv 2023. [[pdf]]()
- **Generating Requirements Elicitation Interview Scripts with Large Language Models** RE 2023. [[pdf]]()
- **A Software Requirements Ecosystem: Linking Forum, Issue Tracker, and FAQs for Requirements Management** TSE 2022. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9940985)
- **A Deep Multitask Learning Approach for Requirements Discovery and Annotation from Open Forum** ASE 2020. [[pdf]](https://dl.acm.org/doi/10.1145/3324884.3416627)

## Requirements Modeling
- **Model Transformation Development Using Automated Requirements Analysis, Metamodel Matching, and Transformation by Example** TOSEM 2022. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3471907) 
- **Dealing with Non-Functional Requirements in Model-Driven Development: A Survey** TSE 2021. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8665968)
- **FREPA: An Automated and Formal Approach to Requirement Modeling and Analysis in Aircraft Control Domain**  FSE 2020. [[pdf]](https://arxiv.org/pdf/2306.01260.pdf)
- **Prema: A Tool for Precise Requirements Editing, Modeling and Analysis** ASE 2020. [[pdf]]()
- **Automated Reuse of Model Transformations through Typing Requirements Models** TOSEM 2019. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3340108)

## Requirements Validation
- **Targeting Requirements Violations of Autonomous Driving Systems by Dynamic Evolutionary Search** ASE 2021. [[pdf]](https://ieeexplore.ieee.org/document/9678883)
- **It Takes Two to Tango: Combining Visual and Textual Information for Detecting Duplicate Video-Based Bug Reports** ICSE 2021. [[pdf]]()
- **NERO: A Text-based Tool for Content Annotation and Detection of Smells in Feature Requests** RE 2020. [[pdf]]()
- **Evaluating model testing and model checking for finding requirements violations in Simulink models** FSE 2019. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3338906.3340444)
- **Images don’t lie: Duplicate crowdtesting reports detection with screenshot information** IST2019. [[pdf]]()
- **Inference of Properties from Requirements and Automation of Their Formal Verification** ASE 2019. [[pdf]]()
- **Validation of requirements for hybrid systems: A formal approach** TOSEM 2012. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/2377656.2377659)
- **An Experimental Study of Fault Detection In User Requirements Documents** TOSEM 1992. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/128894.128897)

## Requirements Specifications
- **How Templated Requirements Specifications Inhibit Creativity in Software Engineering** TSE 2022. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9537306)

## Requirements Extraction
- **Empirical Evaluation of ChatGPT on Requirements Information Retrieval Under Zero-Shot Setting** ArXiv 2023. [[pdf]]()
- **Zero-shot Learning for Named Entity Recognition in Software Specification Documents** RE 2023. [[pdf]]()
- **Where is Your App Frustrating Users** ICSE 2022. [[pdf]](https://arxiv.org/abs/2204.09310) [[code]]()
- **COREQQA: a COmpliance REQuirements understanding using question answering tool** FSE 2022. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3540250.3558926)
- **Identifying Key Features from App User Reviews** ICSE 2021. [[pdf]](https://ieeexplore.ieee.org/document/9402119) [[code]](https://github.com/GIST-NJU/KEFE)
- **ISPY: Automatic Issue-Solution Pair Extraction from Community Live Chats** ASE 2021. [[pdf]]()
- **Learning to extract transaction function from requirements: an industrial case on financial software** FSE 2020. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3368089.3417053)
- **Automatic Extraction of Cause-Effect-Relations from Requirements Artifacts** ASE 2020. [[pdf]](https://dl.acm.org/doi/10.1145/3324884.3416549)
- **Caspar: extracting and synthesizing user stories of problems from app reviews** ICSE 2020. [[pdf]]()
- **Automating Intention Mining** TSE 2020. [[pdf]]()
- **Automated Extraction of Requirement Entities by Leveraging LSTM-CRF and Transfer Learning** ICSME 2019. [[pdf]]()
- **Supporting analysts by dynamic extraction and classification of requirements-related knowledge** ICSE 2019. [[pdf]](https://ieeexplore.ieee.org/document/8812084)
- **Pattern-based mining of opinions in Q&A websites** ICSE 2019. [[pdf]]()
- **INFAR: insight extraction from app reviews** FSE 2018. [[pdf]]()
- **On user rationale in software engineering** Requir.Eng 2018. [[pdf]]()
- **Online app review analysis for identifying emerging issues** ICSE 2018. [[pdf]]()
- **Infar: Insight extraction from app reviews** FSE 2018. [[pdf]]()
- **SAFE: A Simple Approach for Feature Extraction from App Descriptions andApp Reviews** RE 2017. [[pdf]]()
- **Automated Extraction and Clustering of Requirements Glossary Terms** TSE 2017. [[pdf]](https://ieeexplore.ieee.org/document/7765062) 
- **A systematic literature review: Opinion mining studies from mobile app store user reviews** JSS 2017. [[pdf]]()
- **What would users change in my app? summarizing app reviews for recommending software changes** FSE 2016. [[pdf]]()
- **Phrase-based extraction of user opinions in mobile app reviews** ASE 2016. [[pdf]]()
- **What Parts of Your Apps are Loved by Users** ASE 2015. [[pdf]]()
- **Mining User Opinions in Mobile App Reviews: A Keyword-Based Approach** ASE 2015. [[pdf]]()
- **How Do Users Like This Feature? A Fine Grained Sentiment Analysis of App Reviews** RE 2014. [[pdf]]()
- **Automatic extraction of glossary terms from natural language requirements** RE 2013. [[pdf]]()


## Requirements Classification
- **Which AI Technique Is Better to Classify Requirements? An Experiment with SVM, LSTM, and ChatGPT** ArXiv 2023. [[pdf]]()
- **PRCBERT: Prompt Learning for Requirement Classification using BERT-based Pretrained Language Models** ASE 2022. [[pdf]](https://dl.acm.org/doi/10.1145/3551349.3560417)
- **Automated classification of actions in bug reports of mobile apps** ISSTA. [[pdf]]()
- **Domain Adaptation for Test Report Classification in Crowdsourced Testing** ICSE 2017. [[pdf]]()
- **Applying deep learning based automatic bug triager to industrial projects** FSE 2017. [[pdf]]()
- **What works better? a study of classifying requirements** RE 2017. [[pdf]]()
- **Ardoc: App reviews development oriented classifier** FSE 2016. [[pdf]]()
- **Analyzing and automatically labelling the types of user issues that are raised in mobile app reviews** ESE 2016. [[pdf]]()
- **How can i improve my app? Classifying user reviews for software maintenance and evolution** ICSME 2015. [[pdf]]()
- **Bug report, feature request, or simply praise? On automatically classifying app reviews** RE 2015. [[pdf]]()
- **Ensemble methods for app review classification: An approach for software evolution** ASE 2015
- **AR-miner: mining informative reviews for developers from mobile app marketplace** ICSE 2014. [[pdf]]()



## Requirements Ambiguity
- **Automated Handling of Anaphoric Ambiguity in Requirements: A Multi-solution Study** ICSE 2022. [[pdf]](https://dl.acm.org/doi/10.1145/3510003.3510157) 
- **TAPHSIR: towards AnaPHoric ambiguity detection and ReSolution in requirements** FSE 2022. [[pdf]](https://dl.acm.org/doi/10.1145/3540250.3558928)
- **Using Domain-specific Corpora for Improved Handling of Ambiguity in Requirements** ICSE 2021. [[pdf]](https://ieeexplore.ieee.org/document/9402055/)
- **A Deep Context-wise Method for Coreference Detection in Natural Language Requirements** RE 2020. [[pdf]]()

## Requirements Consistency
- **Inconsistency Detection in Natural Language Requirements using ChatGPT: a Preliminary Evaluation** RE 2023. [[pdf]]()
- **Consistency checking in requirements analysis** ISSTA 2017. [[pdf]](https://dl.acm.org/doi/10.1145/3092703.3098239)
- **Reasoning about inconsistencies in natural language requirements** TOSEM 2015. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/1072997.1072999)
- **Automated Consistency Checking of Requirements Specifications** TOSEM 1996. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/234426.234431)


## Requirements Prioritization
- **Uncertainty-wise Requirements Prioritization with Search** TOSEM 2021. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3408301).

## Requirements Dependency
- **A Zone-Based Model for Analysis of Dependent Failures in Requirements Inspection** TSE 2023. [[pdf]](https://dl.acm.org/doi/10.1109/TSE.2023.3266157) 
- **Detecting Software Security Vulnerabilities Via Requirements Dependency Analysis** TSE 2022. [[pdf]](https://ieeexplore.ieee.org/document/9222252)

## Requirements Changes
- **The Emotional Roller Coaster of Responding to Requirements Changes in Software Engineering** TSE 2023. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9769966)
- **A Framework for Emotion-Oriented Requirements Change Handling in Agile Software Engineering** TSE 2023. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10061282)
- **A Faceted Taxonomy of Requirements Changes in Agile Contexts** TSE 2022. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9513607)
- **A Prediction Model for Software Requirements Change Impact** ASE 2021. [[pdf]](https://ieeexplore.ieee.org/document/9678582)
- **Automated change impact analysis between SysML models of requirements and design** FSE 2016. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/2950290.2950293)
- **NARCIA: an automated tool for change impact analysis in natural language requirements** FSE 2015. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/2786805.2803185)

## Requirements Traceability
- **Cross-Domain Requirements Linking via Adversarial-based Domain Adaptation** ICSE 2023. [[pdf]](https://ieeexplore.ieee.org/document/10172688/)
- **Using Consensual Biterms from Text Structures of Requirements and Code to Improve IR-Based Traceability Recovery** ASE 2022. [[pdf]](https://dl.acm.org/doi/10.1145/3551349.3556948)
- **A novel approach to tracing safety requirements and state-based design models** ICSE 2020. [[pdf]](https://dl.acm.org/doi/10.1145/3377811.3380332)
- **Leveraging Historical Associations between Requirements and Source Code to Identify Impacted Classes** TSE 2020. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8423658)
- **Improving the effectiveness of traceability link recovery using hierarchical bayesian networks** ICSE 2020. [[pdf]]()
- **Establishing multilevel test-to-code traceability links** ICSE 2020. [[pdf]]()
- **Traceability in the wild: automatically augmenting incomplete trace links** ICSE 2018. [[pdf]]()
- **Imprecise Matching of Requirements Specifications for Software Services Using Fuzzy Logic** TSE 2017. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7755807)
- **Preventing Defects: The Impact of Requirements Traceability Completeness on Software Quality** TSE 2017. [[pdf]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7723818)
- **Semantically enhanced software traceability using deep learning techniques** ICSE 2017. [[pdf]]()
- **Gray links in the use of requirements traceability** FSE 2016. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/2950290.2950354)

## Requirements Generation
- **On-Demand Security Requirements Synthesis with Relational Generative Adversarial Networks** ICSE 2023. [[pdf]](https://ieeexplore.ieee.org/document/10172729/)
- **Towards Human-Bot Collaborative Software Architecting with ChatGPT** EASE 2023. [[pdf]]()
- **Impact of Large Language Models on Generating Software Specifications** ArXiv 2023. [[pdf]]()
- **Improving Requirements Completeness: Automated Assistance through Large Language Models** ArXiv 2023. [[pdf]]()
- **Automated Generating Natural Language Requirements based on Domain Ontology** ArXiv 2022. [[pdf]]()
- **StoryDroid: automated generation of storyboard for Android apps** ICSE 2019. [[pdf]](https://ieeexplore.ieee.org/document/8812084)
- **Automatic Generation of Graphical User Interface Prototypes from Unrestricted Natural Language Requirements** ASE 2019.

## Formal Requirements
- **DeepSTL - From English Requirements to Signal Temporal Logic** ICSE 2022. [[pdf]]()


## Survey
- **Status Quo in Requirements Engineering: A Theory and a Global Family of Surveys** (2019), TOSEM 2019. [[pdf]](https://dl.acm.org/doi/pdf/10.1145/3306607)

## Misc
- **Advancing Requirements Engineering through Generative AI: Assessing the Role of LLMs** (2023), ArXiv 2023. [[pdf]]()
- **Advancing Requirements Engineering through Generative AI: Assessing the Role of LLMs** (2023), ArXiv 2023. [[pdf]]()
- **AI-based Question Answering Assistance for Analyzing Natural-language Requirements** (2023), ICSE 2023. [[pdf]]()
- **If a Human Can See It, So Should Your System: Reliability Requirements for Machine Vision Components** (2022), ICSE 2022. [[pdf]]()
- **Dialogue Disentanglement in Software Engineering: How Far are We?** (2021), IJCAI 2021. [[pdf]]()
- **MuiDial: Improving Dialogue Disentanglement with Intent-Based Mutual Learning** (2022), IJCAI 2022. [[pdf]]()



# PhD Thesis


# Talks

- **人机物融合背景下的需求工程**, CNCC 2023 [[video]](hhttps://dl.ccf.org.cn/video/videoDetail.html?id=6700020661831680&_state=&_ack=1)

# Datasets

- [RALIC](http://www0.cs.ucl.ac.uk/staff/S.Lim/soolinglim/Datasets.html#ralic):  The dataset contains data of stakeholders and their requirements. It can be used to assess requirements priorities and dependencies.

- [Word](https://sites.google.com/site/mrkarim/data-sets): The dataset has 50 requirements and 81 requirements dependencies. It can be used to assess requirements priorities and dependencies.

- [ReleasePlanner](https://sites.google.com/site/mrkarim/data-sets): This publicly accessible dataset has 25
requirements and 39 dependencies. 

- [KeyFeature](https://github.com/GIST-NJU/KEFE/): This dataset has Chinese requirement description and user review. It can be used to assess extract key feature from requirement description.




# Tools

# Research Groups

- [Jin Zhi](https://scholar.google.com.hk/citations?user=ZC7SObAAAAAJ&hl=zh-CN), Peking University, requirements engineering and software automation.
- [Shi Lin](https://scholar.google.com/citations?hl=en&user=jBcYmbwAAAAJ&view_op=list_works&sortby=pubdate), Beihang University, Intelligent Requirements Engineering.
- [John Grundy](https://sites.google.com/site/johncgrundy/), Monash University, Human Aspects of RE. 
- [Lionel C. Briand](https://scholar.google.com/citations?hl=en&user=Zj897NoAAAAJ&view_op=list_works&sortby=pubdate), University of Ottawa, Requirement Analysis and Quality.


# Venues

## Conferences
- **ICSE**, the International Conference on Software Engineering
- **FSE**, Symposium on the Foundations of Software Engineering
- **ASE**, the International Conference on Automated Software Engineering
- **RE**, the International Conference on Requirements Engineering
- **MSR**, the Mining Software Repositories conference
- **ICPC**, the International Conference on Program Comprehension
- **ISSTA**, the International Symposium on Software Testing and Analysis
- **ICLR**, the International Conference on Learning Representations
- **ICML**, the International Conference on Machine Learning
- **ICMLA**, the International Conference on Machine Learning and Applications
- **AAAI**, the Association for the Advancement of Artificial
Intelligence 
- **ACL**, the Association for Computational Linguistics
- **OOPSLA**, the ACM Conference on Systems, Programming, Languages, and Applications

## Journals
- **TSE**, the IEEE Transactions on Software Engineering
- **TOSEM**, ACM Transactions on Software Engineering and Methodology
- **JSS**, Journal of Systems and Software
- **EMSE**, Journal of Empirical Software Engineering



    
