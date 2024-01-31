# Eugenii Kuzakov
   https://github.com/korkin25/cv/blob/main/CV_Devops_Ekuzakov.pdf

## Position of Interest
   Senior/Team Lead Devops Engineer

## Professional Experience

- DevOps Engineer: 4+ Years
- Systems Architect / Pre-sales Consultant / Business Development Manager: 10 Year
- Lead Engineer (Software & Hardware): 15+ Years

## Professional Strengths

- Proficient in architecture
- Results-oriented approach
- Excellent communication skills and openness
- Active stance in both professional and personal life

## Language Proficiency

- English: Between B1 Intermediate and B2 Upper Intermediate

## Core Professional Skills

- Advanced proficiency in DevOps, including team leadership
- Extensive experience in designing technical architecture for complex projects
- Significant expertise in technical project management, team coordination, and crafting complex technical proposals

## DevOps Experience

- Senior DevOps Engineer with team ***leadership experience***
- ***Python developer***
- ***Kubernetes from scratch***: bare-metal (kubeadm, kubespray, k0s) clouds (terraform), with focus on security, networking, logging, and monitoring
- ***Highload*** experience: National scale project - Unified call center of the Russian Pension Fund

## Software stack
- **Scripting languages**: bash, python, sed, awk, egrep + etc
- **Cloud Platforms**: Hetzner, DigitalOcean, AWS
- **Virtualization**: VMware vSphere, VirtualBox
- **Kubernetes Bootstrappers**: Kubeadm, Kubespray, k0s, Terraform
- **Kubernetes Networking (CNI)**: Cilium, Calico, Weave
- **Kubernetes Container Runtime (CRI)**: Containerd, Docker
- **Docker image builders**: Docker/build_kit, Kaniko
- **Ingress Controllers**: Nginx, Haproxy
- **CI/CD**: GitLab CI/CD, GitHub Actions
- **Docker registry**: Nexus, Harbor
- **Kubernetes deployments**: Helm, Helmfile
- **Infrastructure as Code**: Terraform, Packer, Ansible, SaltStack
- **Logging**: ELK/OpenSearch, Logstash, Fluent Bit, Fluentd
- **Message streaming**: Kafka (Strimzi), ActiveMQ
- **Security**: Hashicorp Vault
- **Monitoring**: Prometheus/Grafana
- **Databases/management**: PostgreSQL, Stolon, Consul
- **Misc**: MetalLB, GeoServer, Grafana, Hasura, Keycloak, Liquibase,Node.js, Angular, Consul, PoWA, etc.

## Public relations

- ***25devops*** - news channel for **#kubernetes** **#docker** **#devsecops** and other **#devops** staff [[https://t.me/korkin25devops]](https://t.me/korkin25devops)
- ***Kubernetes limits calc article*** [[https://habr.com/en/post/680918/]](https://habr.com/en/post/680918/)

## Github projects
- ***Kubernetes resource calculator*** [[https://github.com/korkin25/kube-resource-calc]](https://github.com/korkin25/kube-resource-calc)

## Potential Work Arrangements (@remote)
Full-time(preferred), Part-time, Consulting

## Education

Omsk State Technical University, "Metrology and Device manufacturing" faculty

## Contacts
- ***e-mail:[eugeny.kuzakov@gmail.com](mailto://eugeny.kuzakov@gmail.com)***
- ***[Telegram @korkin25](https://t.me/korkin25)***
- ***[Whatsapp +7-915-495-8170](https://wa.me/79154958170)***
- ***[http://www.linkedin.com/in/eugenykuzakov](http://www.linkedin.com/in/eugenykuzakov)***

## Employment

### *Research and Development Senior DevOps engineer at* Hidden (Dec 2022 - Aug 2023)

##### SaltStack and Vault Integration Enhancement
- Reworked the integration process between SaltStack and Vault.
- Implemented caching of Vault data in Redis to boost performance. 
- Developed a system for accessing multiple Vault endpoints, significantly enhancing efficiency.
- Achieved a twofold increase in the speed of Vault operations, independent of Redis utilization.
- Introduced "Enhanced Key" feature, allowing for the storage of dictionaries as separate Vault keys, a functionality not present in the original version. 
 
##### Research company wide IAM, Single Sign-On (SSO) solution
- Conducted extensive research on Single Sign-On (SSO) authentication and access policy management.
- Integrated Keycloak as the centralized source of truth.
- Focused targets included SSH host access, Hashicorp Vault, and databases such as Postgres, Cassandra, Mongo, etc.

##### SaltStack "Users" Formula Implementation
- Managed Linux authentication objects, including the creation and deletion of users, groups, and their memberships.
 - Oversaw the configuration of all Linux attributes.
 - Controlled SSH access for management users.
 - Implemented Google Authenticator for generating and storing 2FA keys in Vault and established SSH 2FA authentication for managed users.
 - Managed user authorized_keys for secure access control. 

### *Head of DevOps at* Latoken - crypto-currency exchange (Sep 2022 - Oct 2022)

##### Senior Responsibilities
- DevOps Infrastructure Audits: conducted comprehensive audits of the DevOps infrastructure to assess and improve systems.
- Developed and strategized the company's roadmap for DevOps  and infrastructure initiatives.
- Team Collaboration: close work with DevOps-team members and developers to ensure cohesive project execution.
 
##### DevOps Tasks 
- High-Load Logging Cluster Deployment:
  - Deployed a high-load logging cluster for production Kubernetes clusters, processing approximately 300k messages per second.
  - Utilized OpenSearch on 5 hardware servers, complemented by 2 Logstash and 2 Haproxy VMs.
  - Implemented rebalancing rules, aligning every Kubernetes namespace with a corresponding index.
  - OpenSearch Community Repository (Ansible Playbook) Modifications ([OpenSearch Ansible Playbook](https://github.com/korkin25/opensearch-ansible-playbook)):
      - Introduced a Vagrantfile for in-depth stack testing.
      - Reduced the need for root-level operations.
      - Added "host_download" feature to facilitate artifact download on the Ansible controller, aiding in remote operations in closed segments or slow internet contexts.
      - Configured optional support for Uncomplicated Firewall (UFW).
      - Enabled optional integration with Logstash.
      - Enhanced the playbook with various usability features.
      - Provided Fluent Bit configuration examples for better implementation. 

### Senior DevOps at "Satel Pro" (https://satel.org) - software development company for government projects. (Oct 2019 Aug 2022)
 
##### Leadership Role 
 - Led the DevOps team in planning tasks, resources, and timelines
 - Mentored team members, aiding in their rapid skill enhancement and helping them become proficient DevOps engineers, who are content in their new roles
 - Worked closely with over five development teams 
 - Managed 2 Kubernetes dev/test clusters with loops for the entire development stack
 - Maintained 5 production Kubernetes clusters for clients 
 
##### Comprehensive Rollout Rework 
 
 - Undertook a complete overhaul of the rollout using GitLab CI + Helm for the entire product stack
 - Developed and implemented a corporate methodology for a fully automated pipeline (using GitLab CI/CD) for project implementation and maintenance, which included: 
 
###### Infrastructure as Code
   - Preparation of OS images (using HashiCorp Packer)
   - Creation/modification of virtual machines (using HashiCorp Terraform, Cloud-init)
   - Kubernetes installation (using Kubespray, Kubeadm, etc.)
   - Deployment of Kubernetes infrastructure services (usingHelmfile/static manifests)
   - Management of infrastructure services (such as Minio, Postgres/Stolon, Docker registry/cache, GitLab runners, DNS/Bind9, ELK, Prometheus, etc.)
   - Setup of logging and monitoring for the entire installed stack 
 
###### GitOps
- Automated rollout of microservices according to the release plan:
   - Development: automatic deployment from the "develop" branch
   - Release Candidate: automatic deployment from the "master" branch
   - Production: a consistent set of tested versions of microservices 

###### Configuration Management  
   - Used HashiCorp Vault for pipeline-sensitive data and Kubernetes configmaps/secrets 
 
###### Continuous pipeline/deploy optimization 
 
- Docker Builds: multistage, BuildKit(distributed layer caching, parallel stages building, and lazy loading), Alpine.
- Language specific tuning/caching: repo caching for Java/Go/apt/npm/maven, container runtime optimization
- Java container runtime specific tuning: -XX:+UseCGroupMemoryLimitForHeap, -XX:MaxRAMFraction, preStop.
- CI/CD: Artifact caching(Sonatype Nexus), universal templates
- Kubernetes: capabilities, RO FS, res limits/requests, probes, scaling, PDB 

### *Systems architect at* «IBS Expertise» - the biggest systems integrator in Russia (https://www.ibs.ru/)) (Oct 2016 - Aug 2019)

##### Systems Architect 
 I perform analysis and structuring of the customer"s needs, 
 develop the technical architecture for complex projects, write 
 technical specifications, ensure solution protection, and handle 
 other related tasks. 
 
##### Chief Project Engineer 
 
 I lead large-scale projects from intricate pre-sales stages through 
 to design and implementation. I am also responsible for the 
 technical oversight of project execution. 

### *Systems architect at* Technoserv - one of biggest, well known in Russia systems integrator company (*Jun 2014 - Aug 2016*) 

##### Systems Architect 
specialize in analyzing and structuring customer needs, developing the technical architecture for complex projects, drafting technical and commercial proposals, and creating technical documentation among other tasks. 

##### Chief Project Engineer
   I handle the management of large-scale projects, guiding them from complex pre-sales stages through to design and implementation. 

##### the biggest project
   I serve as the main Architect for 112-Systems and am the primary IT Infrastructure Architect for the "Secure City" global project. 

### Systems architect/presale-manager at Open Technologies Ltd. - one of the most well known in Russia systems integrator company (Aug 2012 - Mar 2014)

##### Business Development Manager (BDM) 
I have brought new vendors and solutions into the AMT product portfolio for the Russian/CIS market, and have conducted seminars for sales managers. 
 
##### Pre-sales Manager
I have engaged in aggressive pre-sales activities, including customer meetings and presentations. I have a deep understanding of the advantages and disadvantages of various vendors, products,  technologies, and methods. I"m able to persuade my customers to choose the most suitable solutions based on various parameters. I continuously search for new vendors and products to introduce to our customers. 
 
##### Chief Technical Project Manager 
I manage large projects during complex pre-sales stages. This involves close collaboration with vendors, partners, customers, and others. 

### Head of data processing centers direction at "AMT Group" - one of well known in Russia systems integrator company (Jul 2008 - Jul 2012) 

##### From a technical standpoint
I serve as a team leader in high-end solution provision. 
In my role as a Business Development Manager (BDM): I introduce new vendors and solutions to the Russian/CIS market for integration into the AMT product portfolio and customer base. I also conduct seminars for sales managers. 
 
##### Product Manager 
I coordinate operations with vendors such as EMC, IBM, Symantec, Azul, Varonis, and the AMT sales team. I"ve helped establish AMT Group partnerships with IBM, Symantec/Veritas, WorldITSystems Azul/Pillar, among others, and EMC. Some of these relationships were revived or entirely new for the AMT Group, involving numerous certifications and extensive work with the AMT Group"s top management to drive more business into the company. 
 
##### Pre-sales Manager 
I engage in high levels of pre-sales activities to introduce products, technologies, and projects to customers. Over the past year, I"ve honed my skills in this area, managing customer meetings, technical offer documents, demonstrations, and tender documentation effectively. 
 
##### Engineer 
I am responsible for setting up the hardware/software of vendors like EMC, Veritas, Sun, and Azul. 

### Senior systems engineer at "Open Technologies Ltd" - one of biggest, well known in Russia systems integrator company (Feb 2001 - Jun 2008) 

In my role as a Team Leader and Architect in high availability and storage systems:
- I work with a group of engineers, coordinating their work, offering assistance, and supervising them
- I serve as a technical project coordinator and architect
- I take on the responsibilities of an education manager, analyzing engineers experience, and planning their education
- I act as a 24/7 support team engineer for Sun/EMC systems 

Major projects I"ve completed involve numerous large data centers, incorporating cluster systems, EMC and Hitachi storage systems and software, Sun and HP servers, storage management software, and Oracle databases. The largest of these projects includes: 

- Four 1-8 nodes Veritas Clusters (RAC and HA) connected by a Global Cluster option 
- Two DMX-3 systems replicated via SRDF 
- The design of an agent that provides coordination between failover/parallel groups in different clusters

In this project, I fulfilled several roles: 

- Technical project coordination between EMC, OT managers & engineers, and the customer
- Design and implementation of clusters service high availability- Design and configuration of SAN (Cisco MDS with VSAN, ISL, IVR technologies)
- Planning of EMC DMX-3 storage allocation, building .bin files with dynamic & static SRDF-capability 
- Implementation of new agents to run & control applications in Veritas Clusters 
- Fixing of vendor bugs found in the Veritas SRDF cluster agent 
- Implementation of new actions for different types of cluster resources (e.g., Oracle, OEBS) 
- Design and implementation of hot backup for an Oracle database (running on primary site) to a secondary site using EMC TimeFinder SRDF & Snap technologies. This included the creation of numerous well-documented scripts. 

I have experience working with a broad range of servers/storage equipment and management: 

- EMC Clariion CX series, EMC Symmterix/DMX systems (including SRDF), SAN (McData, Brocade, Cisco MDS), EMC Solution Enabler, EMC Powerpath, EMC Control Center, Veritas Netbackup 
- Sun Microsystems equipment and software including Sun Enterprise and SunFire servers, Sun StorEdge, Solaris 
- High availability clusters such as Veritas Cluster Server, Veritas Storage Foundation and Storage Foundation for Oracle RAC, Global Cluster Option, and Sun Cluster Server 
- Replication software/hardware like EMC MirrorView Sync/Async, EMC SRDF Sync/Async, Veritas Volume Replicator 

### Systems administrator at "Plusinfo" internet channel and hosting provider (Sep 2000 Nov 2000) 

- Reconstructed web-hosting service 
- Automated customer management (virtual sites and mail users) 

References:
- General director Mikhail Ushakov <misha@ushakov.ru>

### Systems/network administrator at "International Trading Bank" - commercial bank http://www.itbank.ru (Jan 2000-Aug 2000) 

- Upgraded SCO Open Server 5.0 and Windows servers to Solaris & FreeBSD systems
- Implemented Samba/CIFS solutions in a Wide Area Network (WAN)
- Optimized branch communications by building FreeBSD-based VPNs
- Entirely rebuilt the company"s internet connection and implemented a corporate email/internet access service
- Replaced direct serial x.25 channels for ATMs with FreeBSD IPsec channels
- Ensured 24/7 stable operation of corporate servers and local area network machines 

### Systems/network administrator  at "Laboratory 321 Ltd" is one of biggest solution provider in Omsk city (http://www.lab321.ru) (July 1994 - Dec 1999)

- Installation and configuration of Solaris (Sparc/x86), FreeBSD, SCO OSE, and Windows NT servers and workstations
- Building, administration, and support of corporate heterogeneous distributed networks using TCP/IP, NetBIOS over IP, and IPX protocols
- Technical support for corporate servers, including user management, security control, firewall management, routing, email services, dedicated and dial-up lines, usage accounting,  daily backup, among others on FreeBSD, Solaris (Sparc/x86), SCO OSE 5, and Linux
- Technical support for the corporate web server ([[http://www.lab321.ru]](http://www.lab321.ru/)) utilizing Apache, Servlets, JSP, SSI, and virtual hosting
- Technical support for LAN users and client machines running Windows NT/95/98
- Transformation of XML documents into HTML using XSL
- Ensured 24/7 stable operation of corporate servers and local area network machines
- Documentation of tasks, server/network configurations in SGML
- Provided support services for customers with installed Unix servers 
- Offered consulting services in network/internet technologies to customers 
- Installation and configuration of complex hardware/software configurations for customers 

References: 

- Company"s director Serge Bush  [[bush@lab321.ru]](mailto:bush@lab321.ru) 
- Paul Romanchenko [[paul@justnews.ru]](mailto:paul@justnews.ru) 

## Outdated

### Cryptocurrency Experience

- Active miner, constantly seeking profitable coins and swiftly implementing algorithms for public/private mining
- Managed a public mining pool, as evidenced here: [[Miner Tokyo]](https://web.archive.org/web/20210525033158/https://miner.tokyo/)
- Maintained the official mining pool for the Sinovate coin, found at [[Sinovate.io]](https://sinovate.io/)
- Developed the x25x algorithm implementation for YIIMP, demonstrating my coding proficiency
- Designed a Python-based project aimed at automatically switching mining rigs to the most profitable coins, utilizing difficulty-based profit calculation, exchange rates, and the HiveOS API.

### Publications

- «How to optimize a DataCenter? Expert advices» [[http://www.cnews.ru/reviews/index.shtml?2009/07/31/356058_6]](http://www.cnews.ru/reviews/index.shtml?2009/07/31/356058_6)

- «Actual aspects of the operation of data storage systems» [[http://www.connect.ru/article.asp?id=8869]](http://www.connect.ru/article.asp?id=8869) ( [[http://www.amt.ru/content/rus/art_text_pict/219/74.pdf]](http://www.amt.ru/content/rus/art_text_pict/219/74.pdf))

### Trainings and certifications

- Symantec Technical Specialist in Veritas Netbackup 6.5 for 31 Oct 2009 Windows 
- Symantec Technical Specialist in Veritas Netbackup 6.5 for 31 Oct 2009 Unix
- Symantec Technical Specialist in Veritas Storage Foundation 01 Nov 2009 5 for UNIX
- Symantec Technical Specialist in Veritas Storage Foundation 06 Aug 2008 5 for Unix
- Symantec Sales Expert in Veritas Cluster 5 19 Aug 2008
- Symantec Technical Specialist in Veritas NetBackup 6 for Windows
- Symmetrix DMX-3 Workshop 12 Oct 2006
- Symmetrix Business Continuity TimeFinder Solutions 26 Sept 2006
- Symmetrix Configuration 15 Sept 2005
- Symmetrix Series Workshop 15 July 2005
- Sun Certification: Type SF x800, Ex900. Installation of Sun 16 May 2005
- Installable systems CLARiiON Core Curriculum (Workshop) 13 May 2005
- TDC150 Sun Cluster 3.x Configuration, Installation & Maintanance & required Exam
- TDC103 Supporting & Troubleshooting Sparc III Products & 23 Aug 2004 required Exam
- TDC102 Supporting & Troubleshooting Sparc II Products & 20 Aug 2004 required Exam
- TDC100 Field Engineer Basic Principles & required Exam 06 Aug 2004
- Sun 99X0 StorEdge TOI Training Lecture (Hitachi 997x) 2 July 2004
- CLARiiON CX Installation and Configuration 16 April 2003
- Integration Certification: Accredited Integration 31 March 
- Specialist HP OpenView Systems and Servers 2003
- Integration Certification: Accredited Integration 19 Oct 2002 Specialist HP OpenView Systems and Servers
- HP Star Certified OpenView Consultant: Operations I (6.03) 19 Oct 2002
- H4357S HP OpenView VantagePoint Operations II 15-18 July 2002
- H4356A HP OpenView VantagePoint Operations I 8-11 July 2002
- Brainbench: HTML Programmer 29 Sept 1999
- Brainbench: C Programmer 14 Aug 1999
- Brainbench: Internet Security Specialist 20 July 1999
- Brainbench: Unix Programmer 11 July 1999
- Brainbench: Master Unix Administrator 17 May 1999