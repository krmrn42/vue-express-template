# Vue Express Fullstack Template

A comprehensive Cookiecutter template for creating production-ready fullstack monorepos with Vue 3, Express TypeScript, and Terraform infrastructure.

## 🚀 Features

- **Frontend**: Vue 3 + TypeScript + Vite + Pinia + Vue Router
- **Backend**: Express + TypeScript (ESM) + Zod validation
- **Infrastructure**: Terraform for GCP Cloud Run deployment
- **Testing**: Vitest with 100% coverage goal
- **Quality**: ESLint, Prettier, Husky pre-commit hooks
- **CI/CD**: GitHub Actions workflows
- **Package Management**: pnpm workspaces

## 📋 Prerequisites

Before using this template, ensure you have:

- **Node.js** >= 20.0.0
- **pnpm** >= 8.0.0
- **Git**
- **Python** (for Cookiecutter)

## 🛠️ Usage

### Option 1: Using pipx (Recommended)

```bash
# Install and run cookiecutter in one command
pipx run cookiecutter gh:krmrn42/vue-express-template
```

### Option 2: Using pip/venv

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install and run cookiecutter
pip install cookiecutter
cookiecutter gh:krmrn42/vue-express-template
```

### Option 3: Using Docker

```bash
docker run -it --rm -v $(pwd):/workspace python:3.11 bash -c "
  pip install cookiecutter &&
  cd /workspace &&
  cookiecutter gh:krmrn42/vue-express-template
"
```

## 📝 Template Configuration

You'll be prompted for the following configuration:

| Variable                 | Description             | Default                  | Example                    |
| ------------------------ | ----------------------- | ------------------------ | -------------------------- |
| `project_name`           | Name of your project    | `my-app`                 | `awesome-saas`             |
| `project_description`    | Brief description       | `Full-stack monorepo...` | `My awesome SaaS platform` |
| `author_name`            | Your name               | `Your Name`              | `John Doe`                 |
| `author_email`           | Your email              | `your.email@example.com` | `john@example.com`         |
| `service_name`           | Backend service name    | `hello-service`          | `api-service`              |
| `service_port`           | Service port            | `3000`                   | `8080`                     |
| `gcp_project_id`         | GCP Project ID          | `my-gcp-project`         | `my-saas-prod`             |
| `gcp_region`             | GCP Region              | `us-central1`            | `europe-west1`             |
| `include_terraform`      | Include Terraform files | `yes`                    | `yes/no`                   |
| `include_github_actions` | Include CI/CD workflows | `yes`                    | `yes/no`                   |
| `run_initial_setup`      | Auto-run setup commands | `yes`                    | `yes/no`                   |

## 🏗️ What Gets Created

After running the template, you'll have:

```
my-app/
├── apps/
│   └── web/              # Vue 3 app (created interactively)
├── services/
│   └── hello-service/    # Express TypeScript service
├── terraform/            # Infrastructure as Code (optional)
├── .github/
│   └── workflows/        # CI/CD pipelines (optional)
├── .husky/              # Git hooks
├── .vscode/             # VS Code configuration
├── package.json         # Root package.json with workspace scripts
├── pnpm-workspace.yaml  # pnpm workspace configuration
├── tsconfig.json        # TypeScript configuration
├── eslint.config.cjs    # ESLint configuration
└── README.md            # Project documentation
```

## 🎯 Interactive Setup Process

When `run_initial_setup` is `yes` (default), the template will:

1. **Initialize Git repository**
2. **Install root dependencies** via `pnpm install`
3. **Create Vue app interactively** - You'll be prompted to configure:
   - ✅ TypeScript: Yes (recommended)
   - ✅ Vue Router: Yes (recommended)
   - ✅ Pinia: Yes (recommended)
   - ✅ Vitest: Yes (recommended)
   - ✅ ESLint: Yes (recommended)
   - ✅ Prettier: Yes (recommended)
4. **Install service dependencies**
5. **Set up Husky git hooks**
6. **Run initial build and tests**
7. **Create initial git commit**

## 🚀 Next Steps After Generation

Test:

```bash
pnpm -r install
pnpm -r format
pnpm -r build
pnpm test
pnpm lint
git add .
pnpm lint-staged
git commit -m "initial commit"
```

Run:

```bash
# Navigate to your project
cd my-app

# Start development servers
pnpm dev

# Or start individually:
cd apps/web && pnpm dev        # Frontend on http://localhost:5173
cd services/hello-service && pnpm dev  # Backend on http://localhost:3000
```

### Available Scripts

```bash
pnpm dev         # Start all development servers
pnpm build       # Build all projects
pnpm test        # Run all tests
pnpm lint        # Lint all code
pnpm format      # Format all code
pnpm type-check  # Check TypeScript types
```

## 🏗️ Infrastructure Setup (Optional)

If you included Terraform:

```bash
cd terraform
terraform init
terraform plan -var="project_id=your-gcp-project"
terraform apply
```

## 🔄 CI/CD Setup (Optional)

If you included GitHub Actions, add these secrets to your GitHub repository:

- `GCP_PROJECT_ID` - Your GCP project ID
- `CLOUD_RUN_REGION` - GCP region (e.g., `us-central1`)
- `GCP_SA_EMAIL` - Service account email
- `WIF_PROVIDER` - Workload Identity Federation provider

## 📚 Architecture

This template follows modern best practices:

- **Monorepo**: Single repository with multiple packages
- **Domain-Driven Design**: Clear separation of concerns
- **Type Safety**: Full TypeScript coverage
- **Testing**: Unit tests with Vitest, 100% coverage goal
- **Code Quality**: ESLint + Prettier + Husky hooks
- **Modern Tooling**: ESM, pnpm workspaces, Vite
- **Cloud-Native**: Terraform + GCP Cloud Run deployment
- **DevOps**: GitHub Actions CI/CD pipeline

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch
3. Make your changes
4. Test the template generation
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.
