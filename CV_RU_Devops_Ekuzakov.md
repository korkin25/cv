# Евгений Кузаков - **Senior DevOps Engineer / AI Agent Engineer**  
- Создаю production-ready Kubernetes-платформы с нуля — от кластера до доставки приложений за 15–30 минут через GitOps и IaC
- 7 лет в DevOps
- 30+ лет в инженерии
- Английский B2

---

## Профессиональное резюме

- **Агентная разработка (Agentic AI):** Собственная среда (harness) для многоагентной разработки проектов любой сложности: детерминированный оркестратор ведёт задачи от выбора до merge без затрат токенов на координацию, без галлюцинаций и сжатия контекста — каждая задача и каждое ревью идут в свежей изолированной сессии, а результат агента проверяется кодом; единый слой для Claude Code, Codex, агентов ACP и Google ax, MCP.
- **Платформы из кода:** 100% IaC/GitOps на vSphere, в Yandex Cloud, AWS и GCP: Terraform, Terramate и Ansible поднимают кластеры Talos, Flux приводит платформу к целевому состоянию, Argo CD с ApplicationSets доставляет приложения из Helm и Kustomize; новый кластер разворачивается из Git за 15–30 минут.
- **Kubernetes как платформа:** Двухуровневая архитектура — центральный кластер держит логирование, метрики, реестр образов Harbor и резервные копии (CloudNativePG, Vault, Garage), рабочие кластеры подключаются к нему по mTLS; сеть на Cilium и Gateway API (Envoy Gateway); при необходимости — работа в изолированном контуре.
- **Доступ и секреты:** Единый IAM на Authentik с OIDC для всех сервисов и Kubernetes (Pinniped); 100% секретов в HashiCorp Vault с автоматической выдачей через External Secrets; сертификаты через cert-manager.
- **Безопасная поставка:** SAST, проверка образов на CVE, подпись Cosign и допуск в кластер только подписанных образов через Kyverno; унифицированные сборки на Docker BuildKit с максимальным использованием кэша, GitLab CI/CD, GitHub Actions, версии по GitVersion.
- **Наблюдаемость:** От инфраструктуры до бизнеса на VictoriaMetrics, Prometheus, Grafana, Loki и Grafana Alloy — качественные логи без шума, метрики из логов, бизнес-метрики и дашборды.
- **GPU-нагрузки:** Выдача NVIDIA GPU контейнерам и виртуальным машинам KubeVirt (VFIO) через GPU Operator, запуск vLLM.

---

## Опыт работы

- **Сооснователь — ISAIYA Health ([isaiya.health](https://isaiya.health))**
  - Разрабатываю детерминированный оркестратор многоагентной разработки: код, а не модель, выбирает задачи из графа зависимостей и ведёт claim, commit, MR и merge, а агенты Claude Code, Codex, ACP и Google ax подключаются через единый слой драйверов и работают в изолированных сессиях без доступа к git и учётным данным.
  - Обеспечил устойчивость поставки к сбоям: машина состояний, журнал внешних действий и lease с fencing token доводят задачу ровно до одного merge после аварийной остановки в любой точке цикла.
  - Встроил независимую проверку результата агента: ревью в свежей сессии только на чтение с вердиктом по строгой схеме, приёмочные тесты до исполнителя, собственный прогон проверок, поиск секретов и merge только при зелёном CI.
  - Разработал плагин для Claude Code и Codex, который ведёт очередь задач с агентами в панелях tmux: watchdog зависаний, восстановление после сбоев, песочница bwrap, вопросы агента и ответы владельца через Telegram.
  - Разработал центральный сервис учёта экземпляров оркестратора и их поставок (Next.js, PostgreSQL, Authentik OIDC, mTLS).
  - Разработал оркестратор проектирования электроники устройства: ИИ-агенты проводят изделие по стадиям, а оркестратор на каждой стадии автоматически проверяет результат:
    - входные данные — проверка по схеме и фиксация требований;
    - схема — ERC (Electrical Rules Check, проверка электрических правил) в KiCad, проверка перечня компонентов (BOM, Bill of Materials) и SPICE-моделирование схемы в ngspice;
    - размещение — DRC (Design Rules Check, проверка правил проектирования) и проверка механики по корпусу;
    - трассировка — DRC и расчёт волнового импеданса дорожек методом конечных элементов в Elmer;
    - финальная медь — тепловой расчёт методом конечных элементов в Elmer;
    - производство — выпуск файлов CAM (Computer-Aided Manufacturing: Gerber, сверловка, файлы монтажа) и проверка DFM (Design for Manufacturing, технологичность изготовления).

- **Проектная деятельность — Cloudless Labs, проект Fluence (янв 2026 – мар 2026) ([cloudless.dev](https://cloudless.dev))**
  - С помощью Terraform разработал интеграцию Authentik с GitHub как IdP и OIDC-авторизацию для NetBird, Kubernetes, Argo CD, Homepage, Cargo Registry и HashiCorp Vault.
  - Выполнил тюнинг Talos, NVIDIA Device Plugin и GPU Operator для provisioning NVIDIA GPU в окружениях VFIO/KubeVirt.
  - Провёл тесты производительности GPU workload в контейнерах, KubeVirt и на нативной Ubuntu для сравнения моделей развертывания и производительности.

### DevOps Engineer — CSSSR (сен 2025 – окт 2026)

- Реализовал в банке стандарт управления Kubernetes-кластерами в изолированном контуре со **100% IaC/GitOps-автоматизацией**: новый кластер Talos на vSphere разворачивается из Git за **15–30 минут** (Terraform, Terramate, Flux) без ручных операций.
- Спроектировал двухуровневую архитектуру кластеров: платформенный кластер `infra` централизует логирование, метрики, реестр образов и резервное копирование, а рабочие кластеры (dev, prod) подключаются к нему по mTLS без общих паролей.
- Внедрил централизованную авторизацию на собственном IAM (Authentik): единый вход по OIDC для Kubernetes, Vault, Argo CD, Grafana, Harbor, Garage и Hubble UI, доступ по группам.
- Перевёл **100%** чувствительных данных в HashiCorp Vault: все учётные данные генерируются, обновляются и подставляются сервисам автоматически через External Secrets.
- Выстроил централизованное логирование с упором на качество: убрал шум (объём аудита сокращён на **~90%**), из логов строятся метрики, критичные события уходят в SIEM банка.
- Сделал бизнес-наблюдаемость: метрики и дашборды BNPL-операций, бизнес-алерты и статус сервиса для заказчика.
- Задал всю конфигурацию сервисов через GitOps: каждое окружение описано одним декларативным манифестом, из которого Argo CD ApplicationSets создают приложения, а CI проверяет его по JSON Schema.
- Свёл выпуск релиза к слиянию ветки: `chart-updater` автоматически обновляет версии сервисов в манифесте, и новая версия попадает в окружение примерно за **2 минуты**.
- Унифицировал сборку .NET-микросервисов единым решением на Dockerfile с максимальным использованием кэша BuildKit.
- Настроил резервное копирование баз данных (полные копии и непрерывный архив WAL с восстановлением на любой момент времени), Vault и S3-хранилищ.
- Выстроил безопасную цепочку поставки образов: SAST и подпись Cosign в CI, сканирование на CVE в Harbor, подпись сторонних образов только без критических уязвимостей (исключения ведутся в Git с владельцем и сроком) и политика Kyverno, которая допускает в prod-кластер только подписанные образы.

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
| Наблюдаемость | Prometheus, Grafana, Loki, ELK, Logstash, Fluent Bit, Fluentd |
| Данные и хранилища | CloudNativePG, Stolon, PoWA, Liquibase, Garage, Nexus, Harbor |
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
- **Ранние роли** (1995–2000): Systems/Network Administrator в International Trading Bank, Plusinfo и Laboratory 321 Ltd.

