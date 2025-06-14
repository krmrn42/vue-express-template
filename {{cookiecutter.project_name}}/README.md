# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## 🚀 Quick Start

```bash
# Install dependencies
pnpm install

# Start development servers
pnpm dev

# Run tests
pnpm test

# Build all projects
pnpm build
```

## 📁 Project Structure

```
{{cookiecutter.project_name}}/
├── apps/
│   └── web/              # Vue 3 frontend application
├── services/
│   └── {{cookiecutter.service_name}}/      # Express TypeScript service
{% if cookiecutter.include_terraform == 'yes' -%}
├── terraform/            # Infrastructure as Code
{% endif -%}
├── .github/
│   └── workflows/        # CI/CD pipelines
└── .husky/              # Git hooks
```

## 🛠️ Development

### Frontend (Vue 3)
```bash
cd apps/web
pnpm dev
```

### Backend (Express + TypeScript)
```bash
cd services/{{cookiecutter.service_name}}
pnpm dev
```

{% if cookiecutter.include_terraform == 'yes' -%}
### Infrastructure (Terraform)
```bash
cd terraform
terraform init
terraform plan
terraform apply
```
{% endif -%}

## 📋 Scripts

- `pnpm dev` - Start all development servers
- `pnpm build` - Build all projects
- `pnpm test` - Run all tests
- `pnpm lint` - Lint all code
- `pnpm format` - Format all code
- `pnpm type-check` - Check TypeScript types

## 🧪 Testing

This project aims for 100% test coverage. Tests are written using Vitest.

```bash
# Run all tests with coverage
pnpm test

# Run tests for specific workspace
cd services/{{cookiecutter.service_name}}
pnpm test:unit
```

## 🔧 Configuration

### Environment Variables

Create `.env` files in each service directory:

```bash
# services/{{cookiecutter.service_name}}/.env
PORT={{cookiecutter.service_port}}
NODE_ENV=development
```

### Git Hooks

Pre-commit hooks are configured with Husky to:
- Run linting and formatting
- Run tests
- Validate commit messages

## 🚀 Deployment

{% if cookiecutter.include_github_actions == 'yes' -%}
Deployment is automated via GitHub Actions. On push to `main`:

1. Tests are run
2. Applications are built
3. Docker images are created
4. Services are deployed to GCP Cloud Run
{% endif -%}

{% if cookiecutter.include_terraform == 'yes' -%}
### Infrastructure

Infrastructure is managed with Terraform:

```bash
cd terraform
terraform init
terraform plan -var="project_id={{cookiecutter.gcp_project_id}}"
terraform apply -var="project_id={{cookiecutter.gcp_project_id}}"
```
{% endif -%}

## 📚 Tech Stack

- **Frontend**: Vue 3, TypeScript, Vite, Pinia, Vue Router
- **Backend**: Express, TypeScript, ESM, Zod validation
- **Testing**: Vitest, Supertest
- **Linting**: ESLint with TypeScript rules
- **Formatting**: Prettier
- **Git Hooks**: Husky + lint-staged
- **Package Manager**: pnpm workspaces
{% if cookiecutter.include_terraform == 'yes' -%}
- **Infrastructure**: Terraform, GCP Cloud Run
{% endif -%}
{% if cookiecutter.include_github_actions == 'yes' -%}
- **CI/CD**: GitHub Actions
{% endif -%}

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details