# Evgenii Kuzakov - **Senior / Team Lead DevOps Engineer**  
- Building production-ready Kubernetes platforms from scratch — cluster to app delivery in 15–30 min via GitOps & IaC
- 7 yrs DevOps
- 15+ yrs Engineering
- English B2

---

## Professional Summary

- **Platform from zero to production in minutes:** Built end-to-end SDLC platforms from scratch — Terraform provisions Talos clusters, FluxCD reconciles the platform, Argo CD delivers apps — cutting new environment provisioning from days to 15–30 minutes.
- **Multi-cloud Kubernetes at scale:** Designed and operated Kubernetes across 4 providers (DigitalOcean, vSphere, bare metal, Yandex MKS), managing 7+ production clusters and serving 5+ development teams with a unified GitOps-first delivery model.
- **Measurable performance gains:** Achieved 10x Vault data-access speedup via Redis caching, deployed a 300k msg/s logging platform on OpenSearch, and eliminated manual operations with 100% IaC/GitOps automation.

## Core Skills

**GPU / AI Workloads:** GPU Operator, vLLM, NVIDIA GPU workloads in VFIO/KubeVirt, containers, and Linux native environments  
**Kubernetes & GitOps:** Talos, FluxCD, Argo CD, Argo Rollouts, Helm, Helmfile, Kustomize, Cilium, Gateway API  
**IaC & Automation:** Terraform, Terramate, Ansible, SaltStack, Packer  
**CI/CD:** GitLab CI/CD, GitHub Actions, Docker BuildKit, Kaniko  
**Security & Secrets:** HashiCorp Vault, External Secrets, Keycloak, Authentik  
**Observability:** Prometheus, Grafana, Loki, ELK/OpenSearch, Fluent Bit  
**Cloud:** Yandex Cloud (primary) · AWS · GCP · DigitalOcean

---

## Employment

- **Project activity — Cloudless Labs, Fluence project (Jan 2026 – Mar 2026) ([cloudless.dev](https://cloudless.dev))**
  - Developed Terraform-based integration of Authentik with GitHub IdP and OIDC authorization for NetBird, Kubernetes, Argo CD, Homepage, Cargo Registry, and HashiCorp Vault.
  - Tuned Talos, NVIDIA Device Plugin, and GPU Operator for provisioning NVIDIA GPUs across VFIO/KubeVirt environments.
  - Ran GPU workload performance tests across containers, KubeVirt, and native Ubuntu environments to validate deployment models and performance characteristics.

### DevOps Engineer — NDA (Sep 2025 – Present)

- Built a full SDLC platform from scratch with a zero-manual-operations model — 100% IaC and GitOps, reducing new production-ready cluster provisioning from days to **15–30 minutes**.
- Designed Talos-based Kubernetes platforms across DigitalOcean, vSphere, and bare-metal servers (kexec-based flows), with FluxCD for platform reconciliation and Argo CD for application delivery.
- Implemented progressive delivery with Argo Rollouts and migrated traffic management from Ingress controllers to Gateway API with Cilium — improving rollout safety and routing flexibility.
- Built the end-to-end bootstrap pipeline: Terraform provisions Talos clusters, installs Flux/flux-sync, and post-bootstrap automation populates Vault credentials for all dependent services.
- Operated core platform services: MinIO Operator, CloudNativePG, Vault, External Secrets, KubeVirt, vLLM, GPU Operator, NVIDIA Device Plugin, Node Feature Discovery.
- Integrated Authentik with GitLab and GitHub as IdPs — delivered SSO across all platform services.

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
| Observability | Prometheus, Grafana, Loki, ELK/OpenSearch, Logstash, Fluent Bit, Fluentd |
| Data & Storage | CloudNativePG, Stolon, PoWA, Liquibase, MinIO, Nexus, Harbor |
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
- **Earlier roles** (1994–2000): Systems/Network Administrator at International Trading Bank, Plusinfo, and Laboratory 321 Ltd.

