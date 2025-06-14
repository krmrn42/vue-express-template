# Vue Express Template Usage Guide

## 🚀 Quick Start

```bash
pipx run cookiecutter gh:krmrn42/vue-express-template
```

Follow the prompts and you'll have a fully configured monorepo!

## 📋 What This Template Creates

### Project Structure

```
my-app/
├── apps/
│   └── web/              # Vue 3 app (created via `pnpm create vue@latest web`)
├── services/
│   └── hello-service/    # Express TypeScript microservice
├── terraform/            # GCP Cloud Run infrastructure (optional)
├── .github/workflows/    # CI/CD pipelines (optional)
├── .husky/              # Git hooks (auto-generated)
├── .vscode/             # VS Code workspace settings
├── package.json         # Root workspace configuration
├── pnpm-workspace.yaml  # pnpm workspace definition
├── tsconfig.json        # TypeScript base configuration
├── eslint.config.cjs    # ESLint flat configuration
└── README.md            # Comprehensive project documentation
```

### What Happens During Generation

1. **Pre-generation validation**: Validates all input parameters
2. **File generation**: Creates all template files with your values
3. **Post-generation setup** (if enabled):
   - Initializes Git repository
   - Installs root dependencies (`pnpm install`)
   - **Interactive Vue app creation** - You configure:
     - TypeScript (recommended: Yes)
     - Vue Router (recommended: Yes)
     - Pinia (recommended: Yes)
     - Vitest (recommended: Yes)
     - ESLint (recommended: Yes)
     - Prettier (recommended: Yes)
   - Installs service dependencies
   - Sets up Husky git hooks
   - Runs initial build and test
   - Creates initial git commit

## 🛠️ Configuration Options

| Variable                 | Description                  | Example           |
| ------------------------ | ---------------------------- | ----------------- |
| `project_name`           | Kebab-case project name      | `awesome-saas`    |
| `service_name`           | Backend service name         | `api-service`     |
| `service_port`           | Service port (1024-65535)    | `8080`            |
| `gcp_project_id`         | GCP project for deployment   | `my-prod-project` |
| `include_terraform`      | Include infrastructure files | `yes/no`          |
| `include_github_actions` | Include CI/CD workflows      | `yes/no`          |
| `run_initial_setup`      | Auto-run setup commands      | `yes/no`          |

## 📚 Technology Stack

- **Frontend**: Vue 3 + TypeScript + Vite + Pinia + Vue Router
- **Backend**: Express + TypeScript (ESM) + Zod validation
- **Testing**: Vitest with coverage reporting
- **Code Quality**: ESLint + Prettier + Husky pre-commit hooks
- **Package Management**: pnpm workspaces
- **Infrastructure**: Terraform + GCP Cloud Run
- **CI/CD**: GitHub Actions with GCP deployment

## 🏃‍♂️ Development Workflow

After generation:

```bash
cd my-app

# Start all development servers
pnpm dev

# Or start individually:
cd apps/web && pnpm dev        # Frontend: http://localhost:5173
cd services/api-service && pnpm dev  # Backend: http://localhost:8080

# Run tests
pnpm test

# Build everything
pnpm build

# Lint and format
pnpm lint
pnpm format
```

## 🚀 Deployment

### GitHub Actions (if enabled)

1. Set repository secrets:

   - `GCP_PROJECT_ID`
   - `CLOUD_RUN_REGION`
   - `GCP_SA_EMAIL`
   - `WIF_PROVIDER`

2. Push to `main` branch triggers:
   - Tests and builds
   - Docker image creation
   - Deployment to Cloud Run

### Manual Terraform (if enabled)

```bash
cd terraform
terraform init
terraform plan -var="project_id=my-gcp-project"
terraform apply
```

## 🔧 Customization

### Adding New Services

1. Create new service in `services/` directory
2. Follow the same structure as the generated service
3. Add to workspace scripts in root `package.json`

### Adding New Apps

1. Create new app in `apps/` directory
2. Add to pnpm workspace
3. Update root scripts as needed

### Environment Variables

Create `.env` files in each service:

```bash
# services/api-service/.env
PORT=8080
NODE_ENV=development
```

## 🧪 Testing

- **Unit Tests**: `pnpm test` (runs Vitest in all workspaces)
- **Coverage**: Automatic coverage reporting with v8 provider
- **Pre-commit**: Tests run automatically on commit via Husky

## 📝 Code Quality

- **ESLint**: TypeScript-strict configuration with Vitest rules
- **Prettier**: Consistent code formatting
- **Husky**: Pre-commit hooks for linting, formatting, and testing
- **lint-staged**: Only lint changed files for performance

## 🆘 Troubleshooting

### Vue App Creation Fails

If the interactive Vue creation fails during setup:

```bash
cd apps
pnpm create vue@latest web
# Follow the prompts, then continue with manual setup
```

### Permission Issues

Make sure hooks are executable:

```bash
chmod +x .husky/pre-commit
```

### Dependency Issues

Clear and reinstall:

```bash
rm -rf node_modules */node_modules
rm pnpm-lock.yaml
pnpm install
```

## 📖 Further Reading

- [Vue 3 Documentation](https://vuejs.org/)
- [Express Documentation](https://expressjs.com/)
- [Terraform GCP Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [pnpm Workspaces](https://pnpm.io/workspaces)
- [Vitest Documentation](https://vitest.dev/)
