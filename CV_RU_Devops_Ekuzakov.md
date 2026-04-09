# Евгений Кузаков - **Senior / Team Lead DevOps Engineer**  
- Создаю production-ready Kubernetes-платформы с нуля — от кластера до доставки приложений за 15–30 минут через GitOps и IaC
- 7 лет в DevOps
- 15+ лет в инженерии
- Английский B2

---

## Профессиональное резюме

- **От платформы с нуля до production за минуты:** Создавал end-to-end SDLC-платформы с нуля — Terraform поднимает Talos-кластеры, FluxCD приводит платформу к целевому состоянию, Argo CD доставляет приложения — сокращая запуск нового окружения с дней до 15–30 минут.
- **Мультиоблачный Kubernetes в production:** Проектировал и эксплуатировал Kubernetes в 4 средах (DigitalOcean, vSphere, bare metal, Yandex MKS), управляя 7+ production-кластерами и поддерживая 5+ команд разработки в единой GitOps-first модели.
- **Измеримые результаты:** Добился 10x ускорения доступа к данным Vault за счёт Redis-кэширования, развернул платформу логирования на 300k msg/s на базе OpenSearch и устранил ручные операции благодаря 100% IaC/GitOps-автоматизации.

## Ключевые навыки

**GPU / AI workloads:** GPU Operator, vLLM, NVIDIA GPU workloads в VFIO/KubeVirt, контейнерах и Linux native environments  
**Kubernetes и GitOps:** Talos, FluxCD, Argo CD, Argo Rollouts, Helm, Helmfile, Kustomize, Cilium, Gateway API  
**IaC и автоматизация:** Terraform, Terramate, Ansible, SaltStack, Packer  
**CI/CD:** GitLab CI/CD, GitHub Actions, Docker BuildKit, Kaniko  
**Безопасность и секреты:** HashiCorp Vault, External Secrets, Keycloak, Authentik  
**Наблюдаемость:** Prometheus, Grafana, Loki, ELK/OpenSearch, Fluent Bit  
**Облака:** Yandex Cloud (основной), AWS, GCP, DigitalOcean

---

## Опыт работы

- **Проектная деятельность — Cloudless Labs, проект Fluence (янв 2026 – мар 2026) ([cloudless.dev](https://cloudless.dev))**
  - С помощью Terraform разработал интеграцию Authentik с GitHub как IdP и OIDC-авторизацию для NetBird, Kubernetes, Argo CD, Homepage, Cargo Registry и HashiCorp Vault.
  - Выполнил тюнинг Talos, NVIDIA Device Plugin и GPU Operator для provisioning NVIDIA GPU в окружениях VFIO/KubeVirt.
  - Провёл тесты производительности GPU workload в контейнерах, KubeVirt и на нативной Ubuntu для сравнения моделей развертывания и производительности.

### DevOps Engineer — NDA (сен 2025 – настоящее время)

- Построил полноценную SDLC-платформу с нуля в модели zero-manual-operations — 100% IaC и GitOps, сократив время подготовки production-ready кластера с дней до **15–30 минут**.
- Спроектировал Kubernetes-платформы на базе Talos в DigitalOcean, vSphere и на bare-metal серверах (включая kexec-based сценарии), используя FluxCD для платформы и Argo CD для доставки приложений.
- Реализовал progressive delivery через Argo Rollouts и мигрировал управление трафиком с Ingress controllers на Gateway API с Cilium — повысив безопасность релизов и гибкость маршрутизации.
- Построил end-to-end bootstrap pipeline: Terraform разворачивает Talos-кластеры, устанавливает Flux/flux-sync, а post-bootstrap автоматизация заполняет Vault-учётные данные для зависимых сервисов.
- Эксплуатировал ключевые платформенные сервисы: MinIO Operator, CloudNativePG, Vault, External Secrets, KubeVirt, vLLM, GPU Operator, NVIDIA Device Plugin, Node Feature Discovery.
- Интегрировал Authentik с GitLab и GitHub как IdP — обеспечил SSO для всех платформенных сервисов.

### Senior DevOps Engineer — HRS International (июл 2024 – авг 2025)

- Построил cloud-agnostic платформенный layout для 3 провайдеров (Yandex, AWS, GCP) — разделил инфраструктурный код и конфигурацию, что позволило независимо управлять релизными циклами и снизить межкомандные конфликты.
- Стандартизировал GitOps-first delivery для dev, test, prod и client-tenant окружений через merge-request-driven модель изменений.
- Разрабатывал reusable Terraform-модули и Terramate-стеки, реализовал drift detection и reconciliation — все изменения инфраструктуры проходили через Git без ручных правок.
- Эксплуатировал production-grade кластеры в Yandex MKS и управлял сервисами Yandex Cloud: VPC, DNS, NLB/ALB, Managed PostgreSQL, Object Storage, IAM, KMS.
- Внедрил Pod Security Standards, zero-trust network policies и управление секретами через Vault с автоматической ротацией.

### R&D Senior DevOps Engineer — SoftSwiss (дек 2022 – авг 2023)

- Переработал интеграцию SaltStack–Vault (Python): добился **2x** ускорения операций и **10x** ускорения доступа к данным за счёт Redis-кэширования, multi-endpoint access и поддержки Enhanced Key.
- Исследовал и внедрил корпоративную IAM/SSO-модель с Keycloak как единым источником идентификации.
- Реализовал SaltStack Users formula для управления пользователями и группами, SSH-доступом, 2FA и authorized_keys.

### Head of DevOps — Latoken (сен 2022 – окт 2022) · Contract/Audit

- Провёл полный аудит DevOps-инфраструктуры, сформировал roadmap и развернул платформу логирования производительностью **~300k msg/s** на базе 5 OpenSearch-узлов, 2 Logstash и 2 HAProxy VM.
- Внёс улучшения в community Ansible playbook для OpenSearch: Vagrant-based testing, reduced root requirements, optional UFW/Logstash integration и примеры Fluent Bit.

### Senior DevOps — Satel Pro (окт 2019 – авг 2022)

- Руководил DevOps-доставкой для 5+ команд разработки, управляя 2 dev/test и 5 production Kubernetes-кластерами.
- Построил полностью автоматизированный pipeline: Packer-образы → Terraform/Cloud-init VM → установка Kubernetes → сервисы через Helmfile → мониторинг и логирование — исключив ручные этапы provisioning.
- Перестроил rollout-модель на GitLab CI + Helm, внедрил release-driven процессы (dev → RC → prod) и защитил секреты через Vault.
- Оптимизировал Docker-сборки (multistage, BuildKit, distributed caching, lazy loading) и усилил надёжность workloads через requests/limits, probes, PDB и read-only filesystems.

---

## Открытые проекты и публикации

- **[Open CI/CD](https://gitlab.com/open_ci_cd/templates)** — production-grade шаблоны GitLab CI/CD, повторно используемые в нескольких проектах без модификаций. Включают Docker BuildKit-сборки, Helm-деплой (ArgoCD/FluxCD/Swarm), SAST, подпись артефактов через cosign, changelog и change detection для пропуска лишних job.
- **[Kubernetes Resource Calculator](https://github.com/korkin25/kube-resource-calc)** — CLI-инструмент для расчёта requests и limits в Kubernetes.
- **[Kubernetes Limits Calc Article](https://habr.com/en/post/680918/)** — опубликованная статья на Habr.
- **[25devops](https://t.me/korkin25devops)** — DevOps-канал о Kubernetes, Docker и DevSecOps.

---

## Полный стек технологий

| Категория | Стек |
| --- | --- |
| Kubernetes и OS | Talos, k0s, Containerd, Cilium, Calico, Gateway API |
| GitOps и доставка | FluxCD, Argo CD, Argo Rollouts, Helm, Helmfile, Kustomize |
| IaC и управление конфигурацией | Terraform, Terramate, Ansible, SaltStack, Packer |
| CI/CD и сборки | GitLab CI/CD, GitHub Actions, Docker BuildKit, Kaniko |
| Безопасность и IAM | HashiCorp Vault, External Secrets, Keycloak, Authentik |
| Наблюдаемость | Prometheus, Grafana, Loki, ELK/OpenSearch, Logstash, Fluent Bit, Fluentd |
| Данные и хранилища | CloudNativePG, Stolon, PoWA, Liquibase, MinIO, Nexus, Harbor |
| Виртуализация | VMware vSphere, KubeVirt, VirtualBox |
| GPU / AI | vLLM, GPU Operator, NVIDIA Device Plugin, Node Feature Discovery |
| Языки | Bash, Python |

## Облачные провайдеры

| Провайдер | Сервисы |
| --- | --- |
| Yandex Cloud | IAM, Compute Cloud, VPC, DNS, NLB, ALB, Managed PostgreSQL, Managed Redis, Cloud Logging, Lockbox, Object Storage |
| AWS | IAM, EC2, EKS, ELB, S3, RDS, Route 53, ACM |
| GCP | IAM, Compute Engine, Kubernetes Engine, Cloud Load Balancing, GCS, Cloud SQL, Cloud DNS, Certificate Manager |
| DigitalOcean | Droplets, Networking, Load Balancers, Managed Kubernetes |

---

## Образование

Омский государственный технический университет — факультет «Метрология и приборостроение»

## Формат работы

Remote · Full-time (preferred) · Part-time · Consulting

[PDF version](https://github.com/korkin25/cv/blob/main/CV_Devops_Ekuzakov.pdf)

Email: [eugeny.kuzakov@gmail.com](mailto:eugeny.kuzakov@gmail.com) · Telegram: [@korkin25](https://t.me/korkin25) · LinkedIn: [eugenykuzakov](http://www.linkedin.com/in/eugenykuzakov)  
WhatsApp: [+7-915-495-8170](https://wa.me/79154958170)

---

## Предыдущий опыт

- **IBS Expertise** — Systems Architect / Chief Project Engineer (окт 2016 – авг 2019): проектировал технические архитектуры и вёл presales для крупных государственных и корпоративных проектов.
- **Technoserv** — Systems Architect / Chief Project Engineer (июн 2014 – авг 2016): разрабатывал сложные инфраструктурные архитектуры и участвовал в крупных проектах, включая «Безопасный город».
- **Open Technologies Ltd.** — Systems Architect / Chief Technical Project Manager (авг 2012 – мар 2014): развивал vendor portfolio и технический presales для enterprise-инфраструктуры.
- **AMT Group** — Head of Data Processing Centers / Product Manager (июл 2008 – июл 2012): отвечал за развитие enterprise-платформ и стратегических партнёрств с вендорами.
- **Open Technologies Ltd.** — Senior Systems Engineer (фев 2001 – июн 2008): внедрял HA, storage, SAN, clustering и DR-решения для крупных дата-центров.
- **Ранние роли** (1994–2000): Systems/Network Administrator в International Trading Bank, Plusinfo и Laboratory 321 Ltd.

