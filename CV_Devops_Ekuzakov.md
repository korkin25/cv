# Evgenii Kuzakov - **Senior DevOps Engineer / AI Agent Engineer**  
- Building production-ready Kubernetes platforms from scratch — cluster to app delivery in 15–30 min via GitOps & IaC
- 7 yrs DevOps
- 30+ yrs Engineering
- English B2

---

## Professional Summary

- **Agentic AI engineering:** My own multi-agent development harness for projects of any complexity: a deterministic orchestrator drives tasks from selection to merge with no tokens spent on coordination, no hallucinations, and no context compaction — every task and every review runs in a fresh isolated session, and agent output is verified by code; a single layer for Claude Code, Codex, ACP agents, and Google ax, plus MCP.
- **Platforms as code:** 100% IaC/GitOps on vSphere, Yandex Cloud, AWS, and GCP: Terraform, Terramate, and Ansible provision Talos clusters, Flux reconciles the platform, and Argo CD with ApplicationSets delivers applications from Helm and Kustomize; a new cluster is deployed from Git in 15–30 minutes.
- **Kubernetes as a platform:** A two-tier architecture — a central cluster hosts logging, metrics, the Harbor image registry, and backups (CloudNativePG, Vault, Garage), and workload clusters connect to it over mTLS; networking on Cilium and Gateway API (Envoy Gateway); air-gapped deployment as an option.
- **Access and secrets:** A single IAM on Authentik with OIDC for all services and Kubernetes (Pinniped); 100% of secrets in HashiCorp Vault with automatic delivery via External Secrets; certificates via cert-manager.
- **Secure delivery:** SAST, CVE scanning, Cosign signing, and admission of signed images only via Kyverno; unified Docker BuildKit builds that make maximum use of the cache, GitLab CI/CD, GitHub Actions, and GitVersion-based versioning.
- **Observability:** From infrastructure to business on VictoriaMetrics, Prometheus, Grafana, Loki, and Grafana Alloy — clean, noise-free logs, metrics derived from logs, and business metrics and dashboards.
- **GPU workloads:** NVIDIA GPUs for containers and KubeVirt VMs (VFIO) via GPU Operator, and vLLM.

---

## Employment

- **Co-founder — ISAIYA Health ([isaiya.health](https://isaiya.health))**
  - Developing a deterministic multi-agent development orchestrator: code, not the model, picks tasks from the dependency graph and runs claim, commit, MR, and merge, while Claude Code, Codex, ACP, and Google ax agents plug in through a single driver layer and work in isolated sessions with no access to git or credentials.
  - Made delivery crash-safe: a state machine, an external-action journal, and leases with fencing tokens bring a task to exactly one merge after a crash at any point of the cycle.
  - Built independent verification of agent output: review in a fresh read-only session with a strict-schema verdict, acceptance tests written before the executor, orchestrator-run checks, secret scanning, and merge only on green CI.
  - Developed a plugin for Claude Code and Codex that runs a task queue with agents in tmux panes: stall watchdog, crash recovery, bwrap sandbox, and agent questions with owner answers over Telegram.
  - Developed a central registry service for orchestrator instances and their deliveries (Next.js, PostgreSQL, Authentik OIDC, mTLS).
  - Developed a device electronics design orchestrator: AI agents take the device through the design stages, and the orchestrator automatically verifies the result at every stage:
    - inputs — schema validation and requirements freeze;
    - schematic — ERC (Electrical Rules Check) in KiCad, BOM (Bill of Materials) check, and SPICE circuit simulation in ngspice;
    - placement — DRC (Design Rules Check) and mechanical fit against the enclosure;
    - routing — DRC and finite-element trace impedance analysis in Elmer;
    - final copper — finite-element thermal analysis in Elmer;
    - manufacturing — CAM (Computer-Aided Manufacturing) outputs: Gerber, drill and assembly files, plus a DFM (Design for Manufacturing) check.

- **Project activity — Cloudless Labs, Fluence project (Jan 2026 – Mar 2026) ([cloudless.dev](https://cloudless.dev))**
  - Developed Terraform-based integration of Authentik with GitHub IdP and OIDC authorization for NetBird, Kubernetes, Argo CD, Homepage, Cargo Registry, and HashiCorp Vault.
  - Tuned Talos, NVIDIA Device Plugin, and GPU Operator for provisioning NVIDIA GPUs across VFIO/KubeVirt environments.
  - Ran GPU workload performance tests across containers, KubeVirt, and native Ubuntu environments to validate deployment models and performance characteristics.

### DevOps Engineer — CSSSR (Sep 2025 – Oct 2026)

- Implemented the bank's standard for Kubernetes cluster management in an air-gapped environment with **100% IaC/GitOps automation**: a new Talos cluster on vSphere is deployed from Git in **15–30 minutes** (Terraform, Terramate, Flux) with zero manual steps.
- Designed a two-tier cluster architecture: the platform `infra` cluster centralizes logging, metrics, the image registry, and backups, while workload clusters (dev, prod) connect to it over mTLS with no shared passwords.
- Implemented centralized authorization on an in-house IAM (Authentik): OIDC single sign-on for Kubernetes, Vault, Argo CD, Grafana, Harbor, Garage, and Hubble UI, with group-based access.
- Moved **100%** of sensitive data into HashiCorp Vault: all credentials are generated, updated, and injected into services automatically via External Secrets.
- Built centralized logging focused on quality: removed noise (audit volume cut by **~90%**), derived metrics from logs, and forwarded critical events to the bank's SIEM.
- Delivered business observability: metrics and dashboards for BNPL operations, business-level alerts, and a service status feed for the customer.
- Defined all service configuration through GitOps: each environment is described by a single declarative manifest from which Argo CD ApplicationSets generate applications, and CI validates it against a JSON Schema.
- Reduced a release to a branch merge: `chart-updater` automatically bumps service versions in the manifest, and a new version reaches its environment in about **2 minutes**.
- Unified .NET microservice builds with a single Dockerfile-based solution that makes maximum use of the BuildKit cache.
- Set up backups of databases (full backups plus continuous WAL archiving with point-in-time recovery), Vault, and S3 storage.
- Built a secure image supply chain: SAST and Cosign signing in CI, CVE scanning in Harbor, signing of third-party images only when free of critical vulnerabilities (exceptions tracked in Git with an owner and expiry), and a Kyverno policy that admits only signed images to the prod cluster.

### Senior DevOps Engineer — HRS International (Jul 2024 – Aug 2025)

- Built a cloud-agnostic platform layout across 3 providers (Yandex, AWS, GCP) — decoupled infra code from config to enable independent release cycles and cut cross-team deployment conflicts.
- Standardized GitOps-first delivery across dev, test, prod, and client-tenant environments through merge-request-driven change management.
- Authored reusable Terraform modules and Terramate stacks, managed drift detection and reconciliation — all infrastructure changes went through Git, zero manual modifications.
- Operated production-grade Yandex MKS clusters and governed cloud services: VPC, DNS, NLB/ALB, Managed PostgreSQL, Object Storage, IAM, KMS.
- Enforced Pod Security Standards, zero-trust network policies, and Vault-based secrets management with automated rotation.

### R&D Senior DevOps Engineer — SoftSwiss (Dec 2022 – Aug 2023)

- Reworked SaltStack–Vault integration (Python): achieved **2x** operation speed improvement and **10x** data-access speedup via Redis caching, multi-endpoint access, and Enhanced Key support.
- Researched and implemented a company-wide IAM/SSO model with Keycloak as the central identity source.
- Built a SaltStack Users formula covering user/group management, SSH access, 2FA, and authorized_keys.

### Head of DevOps — Latoken (Sep 2022 – Oct 2022) · Contract/Audit

- Conducted a full DevOps infrastructure audit, defined the roadmap, and deployed a **~300k msg/s** logging platform on 5 OpenSearch nodes + 2 Logstash + 2 HAProxy VMs.
- Contributed improvements to the OpenSearch community Ansible playbook: Vagrant-based testing, reduced root requirements, optional UFW/Logstash integration, and Fluent Bit examples.

### Senior DevOps — Satel Pro (Oct 2019 – Aug 2022)

- Led DevOps delivery across 5+ development teams, managing 2 dev/test and 5 production Kubernetes clusters.
- Built a fully automated pipeline: Packer images → Terraform/Cloud-init VMs → Kubernetes install → Helmfile services → monitoring & logging — eliminating manual provisioning steps.
- Reworked rollout model with GitLab CI + Helm; implemented release-driven flows (dev → RC → prod) with Vault-secured secrets.
- Optimized Docker builds (multistage, BuildKit, distributed caching, lazy loading) and hardened workloads with requests/limits, probes, PDBs, and read-only filesystems.

---

## Open Projects and Publications

- **[Open CI/CD](https://gitlab.com/open_ci_cd/templates)** — production-grade GitLab CI/CD templates reused across multiple projects without modification. Covers Docker BuildKit builds, Helm deployments (ArgoCD/FluxCD/Swarm), SAST, cosign signing, changelogs, and change detection to skip unnecessary jobs.
- **[Kubernetes Resource Calculator](https://github.com/korkin25/kube-resource-calc)** — CLI tool for calculating Kubernetes resource requests and limits.
- **[Kubernetes Limits Calc Article](https://habr.com/en/post/680918/)** — published on Habr.
- **[25devops](https://t.me/korkin25devops)** — DevOps news channel covering Kubernetes, Docker, and DevSecOps.

---

## Full Technology Reference

| Area | Stack |
| --- | --- |
| Kubernetes & OS | Talos, k0s, Containerd, Cilium, Calico, Gateway API |
| GitOps & Delivery | FluxCD, Argo CD, Argo Rollouts, Helm, Helmfile, Kustomize |
| IaC & Config Mgmt | Terraform, Terramate, Ansible, SaltStack, Packer |
| CI/CD & Builds | GitLab CI/CD, GitHub Actions, Docker BuildKit, Kaniko |
| Security & IAM | HashiCorp Vault, External Secrets, Keycloak, **Authentik** |
| Observability | Prometheus, Grafana, Loki, ELK, Logstash, Fluent Bit, Fluentd |
| Data & Storage | CloudNativePG, Stolon, PoWA, Liquibase, Garage, Nexus, Harbor |
| Virtualization | VMware vSphere, KubeVirt, VirtualBox |
| GPU / AI | vLLM, GPU Operator, NVIDIA Device Plugin, Node Feature Discovery |
| Languages | Bash, Python |

## Cloud Providers

| Provider | Services |
| --- | --- |
| Yandex Cloud | IAM, Compute Cloud, VPC, DNS, NLB, ALB, Managed PostgreSQL, Managed Redis, Cloud Logging, Lockbox, Object Storage |
| AWS | IAM, EC2, EKS, ELB, S3, RDS, Route 53, ACM |
| GCP | IAM, Compute Engine, Kubernetes Engine, Cloud Load Balancing, GCS, Cloud SQL, Cloud DNS, Certificate Manager |
| DigitalOcean | Droplets, Networking, Load Balancers, Managed Kubernetes |

---

## Education

Omsk State Technical University — "Metrology and Device Manufacturing" faculty

## Availability

Remote · Full-time (preferred) · Part-time · Consulting

[PDF version](https://github.com/korkin25/cv/blob/main/CV_Devops_Ekuzakov.pdf)

Email: [eugeny.kuzakov@gmail.com](mailto:eugeny.kuzakov@gmail.com) · Telegram: [@korkin25](https://t.me/korkin25) · LinkedIn: [eugenykuzakov](http://www.linkedin.com/in/eugenykuzakov)  
WhatsApp: [+7-915-495-8170](https://wa.me/79154958170)

---

## Prior Experience

- **IBS Expertise** — Systems Architect / Chief Project Engineer (Oct 2016 – Aug 2019): Designed technical architectures and led pre-sales for large-scale government and enterprise projects.
- **Technoserv** — Systems Architect / Chief Project Engineer (Jun 2014 – Aug 2016): Developed complex infrastructure architectures and led major delivery initiatives, including the Secure City program.
- **Open Technologies Ltd.** — Systems Architect / Chief Technical Project Manager (Aug 2012 – Mar 2014): Managed vendor portfolio development and technical pre-sales for enterprise infrastructure.
- **AMT Group** — Head of Data Processing Centers / Product Manager (Jul 2008 – Jul 2012): Led business development of enterprise infrastructure platforms and strategic vendor partnerships.
- **Open Technologies Ltd.** — Senior Systems Engineer (Feb 2001 – Jun 2008): Delivered HA, storage, SAN, clustering, and DR solutions for large data center projects.
- **Earlier roles** (1995–2000): Systems/Network Administrator at International Trading Bank, Plusinfo, and Laboratory 321 Ltd.

