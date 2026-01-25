# 🚀 DevOps Roadmap 2026

**5 Günlük Production ML Pipeline** ☸️🐳🔄

## 📊 Progress
✅ GÜN1: FastAPI + Docker + Test
✅ GÜN2: GitHub Actions CI/CD + Docker Hub + Pages
🔄 GÜN3: Minikube Kubernetes
🔄 GÜN4: Terraform Infrastructure
🔄 GÜN5: Helm + ArgoCD + Monitoring
## 🟢 Live Demos
| Service | Status | URL |
|---------|--------|-----|
| **CI/CD Pipeline** | 🟢 Live | https://github.com/iremhalac/devops-roadmap-2026/actions |
| **Docker Image** | 🟢 Pushed | https://hub.docker.com/r/iremhalac/devops-roadmap |
| **API Docs** | 🟢 Hosted | https://iremhalac.github.io/devops-roadmap-2026/openapi.json |
| **Swagger UI** | 🔄 Local | \`localhost:8080/docs\` |

## 🏗️ Architecture
GitHub → Actions (CI/CD) → Docker Hub → Minikube (K8s) → Production
↓
GitHub Pages (Docs)

## 🚀 Quick Demo
\`\`\`bash
# M2 Mac uyumlu
docker pull --platform linux/amd64 iremhalac/devops-roadmap:latest
docker run --platform linux/amd64 -p 8080:8000 iremhalac/devops-roadmap:latest
open http://localhost:8080/docs  # FastAPI Swagger UI
\`\`\`

## 📈 Pipeline Flow
\`\`\`mermaid
graph TD
    A[Push Code] --> B[GitHub Actions]
    B --> C[Pytest]
    C --> D[Docker Build]
    D --> E[Docker Hub Push]
    E --> F[GitHub Pages Docs]
    F --> G[✅ Deployed]
\`\`\`

## 🛠️ Tech Stack
🐍 FastAPI + Pytest + Uvicorn
🐳 Docker Multi-stage
🔄 GitHub Actions
📦 Docker Hub
☸️ Minikube (GÜN3)
🌐 GitHub Pages

## 📋 Günlük Checkpoints
- **GÜN1**: \`docker run\` → localhost:8080/docs ✅
- **GÜN2**: Actions YEŞİL + Docker Hub + Pages ✅
- **GÜN3**: \`kubectl get pods\` → Running
- **GÜN4**: \`terraform apply\` → K8s cluster
- **GÜN5**: \`helm install\` → Zero-downtime

---
**İrem Halac** | ML Engineer | Jan 2026
