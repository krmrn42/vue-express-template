#!/usr/bin/env python3
"""
Post-generation hook for fullstack monorepo template.
Runs all necessary setup commands after files are generated.
Follows the exact steps from README.md.
"""

import os
import subprocess
import sys
import shutil
from pathlib import Path

def run_command(command, description, cwd=None, shell=True, check=True):
    """Run a command and handle errors gracefully."""
    print(f"🔄 {description}...")
    try:
        if isinstance(command, str):
            cmd_display = command
        else:
            cmd_display = ' '.join(command)

        result = subprocess.run(
            command,
            shell=shell,
            check=check,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Command: {cmd_display}")
        print(f"   Error: {e.stderr}")
        if check:
            return None
        return e

def check_prerequisites():
    """Check if required tools are available."""
    required_tools = {
        'node': 'Node.js (>=20.0.0)',
        'pnpm': 'pnpm package manager (>=8.0.0)',
        'git': 'Git'
    }

    missing_tools = []
    for tool, description in required_tools.items():
        try:
            result = subprocess.run([tool, '--version'],
                                  capture_output=True, check=True, text=True)
            print(f"✅ {description} found: {result.stdout.strip().split()[0] if result.stdout else 'unknown version'}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing_tools.append(description)
            print(f"❌ {description} not found")

    if missing_tools:
        print(f"\n⚠️  Missing required tools: {', '.join(missing_tools)}")
        print("Please install them and run the setup again.")
        return False
    return True

def setup_git_repository():
    """Initialize git repository following README.md steps."""
    if not (Path.cwd() / '.git').exists():
        run_command('git init', 'Initializing Git repository')
    else:
        print("✅ Git repository already exists")

def install_root_dependencies():
    """Install root-level dependencies as per README.md."""
    run_command('pnpm install', 'Installing root dependencies')

def create_vue_app():
    """Create Vue app following README.md: pnpm create vue@latest web"""
    print("🎨 Creating Vue.js application...")
    print("📋 You will be prompted to configure the Vue app. Recommended choices:")
    print("   ✅ TypeScript: Yes")
    print("   ✅ JSX: No")
    print("   ✅ Vue Router: Yes")
    print("   ✅ Pinia: Yes")
    print("   ✅ Vitest: Yes")
    print("   ✅ End-to-End Testing: No (or Playwright if you prefer)")
    print("   ✅ ESLint: Yes")
    print("   ✅ Prettier: Yes")
    print()

    apps_dir = Path('apps')
    apps_dir.mkdir(exist_ok=True)

    # Change to apps directory and run the Vue creation
    result = run_command(
        'pnpm create vue@latest web --typescript --jsx --vue-router --pinia --vitest --cypress --eslint --prettier',
        'Creating Vue application',
        cwd=apps_dir,
        check=False
    )

    if result and result.returncode != 0:
        print("❌ Vue app creation failed. Please run manually:")
        print("   cd apps && pnpm create vue@latest web")
        return False

    # Move .vscode from web to root as per README.md
    web_vscode = Path('apps/web/.vscode')
    root_vscode = Path('.vscode')

    if web_vscode.exists() and not root_vscode.exists():
        shutil.move(str(web_vscode), str(root_vscode))
        print("✅ Moved .vscode directory to root")

    return True

def setup_vue_app():
    """Setup Vue app dependencies and configuration."""
    web_path = Path('apps/web')
    if not web_path.exists():
        print("❌ Vue app not found. Skipping Vue setup.")
        return False

    # Add coverage to vitest config as per README.md
    vitest_config = web_path / 'vitest.config.ts'
    if vitest_config.exists():
        content = vitest_config.read_text()
        if 'coverage' not in content:
            # Add coverage configuration
            updated_content = content.replace(
                'defineConfig({',
                '''defineConfig({
    test: {
      environment: 'jsdom',
      exclude: [...configDefaults.exclude, 'e2e/*'],
      root: fileURLToPath(new URL('./', import.meta.url)),
      coverage: {
        provider: 'v8',
        reporter: ['text', 'json', 'html']
      }
    },'''
            )
            vitest_config.write_text(updated_content)
            print("✅ Added coverage configuration to vitest.config.ts")

    # Install web app dependencies
    run_command('pnpm install', 'Installing web app dependencies', cwd=web_path)

    # Add coverage dependency
    run_command('pnpm add -D @vitest/coverage-v8', 'Adding Vitest coverage', cwd=web_path)

    return True

def install_service_dependencies():
    """Install service dependencies."""
    service_name = "{{ cookiecutter.service_name }}"
    service_path = Path('services') / service_name

    if service_path.exists():
        run_command('pnpm install', f'Installing {service_name} dependencies', cwd=service_path)
    else:
        print(f"❌ Service {service_name} not found")

def setup_husky():
    """Set up Husky git hooks as per README.md."""
    run_command('pnpm exec husky init', 'Setting up Husky git hooks')

    # Create pre-commit hook following README.md
    husky_dir = Path('.husky')
    pre_commit_file = husky_dir / 'pre-commit'

    pre_commit_content = '''pnpm exec lint-staged
git update-index --again
pnpm test
'''

    if pre_commit_file.exists():
        pre_commit_file.write_text(pre_commit_content)
        print("✅ Updated pre-commit hook")
    else:
        print("⚠️  Pre-commit hook not found, please set up manually")

def run_initial_verification():
    """Run initial verification as per README.md."""
    commands = [
        ('pnpm -r install', 'Installing all workspace dependencies'),
        ('pnpm -r format', 'Formatting all code'),
        ('pnpm -r build', 'Building all projects'),
        ('pnpm test', 'Running all tests'),
        ('pnpm lint', 'Running all linting')
    ]

    for command, description in commands:
        result = run_command(command, description, check=False)
        if result and result.returncode != 0:
            print(f"⚠️  {description} had issues, but continuing...")

def commit_initial_version():
    """Create initial git commit."""
    run_command('git add .', 'Adding all files to git')

    # Try to commit - might fail if there are lint issues, that's ok
    result = run_command(
        'git commit -m "Initial commit from template"',
        'Creating initial commit',
        check=False
    )

    if result and result.returncode == 0:
        print("✅ Initial commit created successfully")
    else:
        print("⚠️  Initial commit had issues - please review and commit manually")

def main():
    """Main setup sequence following README.md exactly."""
    run_setup = "{{ cookiecutter.run_initial_setup }}"
    if run_setup == "no":
        print("⏭️  Skipping automatic setup. Please follow README.md manually.")
        return

    print("🚀 Setting up your fullstack monorepo...")
    print("📖 Following the exact steps from README.md")
    print()

    # Check prerequisites first
    if not check_prerequisites():
        sys.exit(1)

    project_root = Path.cwd()
    print(f"📁 Working in: {project_root}")

    try:
        # Step 1: Git setup
        setup_git_repository()

        # Step 2: Install root dependencies
        install_root_dependencies()

        # Step 3: Create Vue app
        if not create_vue_app():
            print("⚠️  Vue app creation needs manual intervention")
        else:
            setup_vue_app()

        # Step 4: Install service dependencies
        install_service_dependencies()

        # Step 5: Set up Husky
        setup_husky()

        # Step 6: Run verification (following README.md test section)
        run_initial_verification()

        # Step 7: Initial commit
        commit_initial_version()

        print("\n🎉 Setup completed successfully!")
        print("\n📋 Next steps:")
        print("   1. cd {{ cookiecutter.project_name }}")
        print("   2. Review and customize configuration files")
        print("   3. Start development:")
        print("      - Frontend: cd apps/web && pnpm dev")
        print("      - Backend: cd services/{{ cookiecutter.service_name }} && pnpm dev")
        print("      - Or both: pnpm dev")

        include_terraform = "{{ cookiecutter.include_terraform }}"
        if include_terraform == 'yes':
            print("   4. Initialize Terraform: cd terraform && terraform init")

        include_github_actions = "{{ cookiecutter.include_github_actions }}"
        if include_github_actions == 'yes':
            print("   5. Set up GitHub secrets for CI/CD:")
            print("      - GCP_PROJECT_ID")
            print("      - CLOUD_RUN_REGION")
            print("      - GCP_SA_EMAIL")
            print("      - WIF_PROVIDER")

    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        print("You can complete the setup manually by following README.md")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed with error: {e}")
        print("Please complete the setup manually by following README.md")
        sys.exit(1)

if __name__ == '__main__':
    main()