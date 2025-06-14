#!/usr/bin/env python3
"""
Test script to validate the cookiecutter template.
Run this before publishing to ensure everything works correctly.
"""

import subprocess
import tempfile
import os
import sys
from pathlib import Path

def run_test():
    """Test the cookiecutter template generation."""
    print("🧪 Testing Vue Express Template...")
    
    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        os.chdir(tmp_dir)
        
        # Get the template path
        template_path = Path(__file__).parent.absolute()
        
        # Test data
        test_data = {
            "project_name": "test-app",
            "project_description": "Test application",
            "author_name": "Test Author",
            "author_email": "test@example.com",
            "service_name": "api-service",
            "service_port": "8080",
            "gcp_project_id": "test-project-123",
            "gcp_region": "us-central1",
            "include_terraform": "yes",
            "include_github_actions": "yes",
            "run_initial_setup": "no"  # Skip setup for testing
        }
        
        # Create cookiecutter input file
        cookiecutter_input = '\n'.join([
            test_data["project_name"],
            test_data["project_description"],
            test_data["author_name"],
            test_data["author_email"],
            test_data["service_name"],
            test_data["service_port"],
            test_data["gcp_project_id"],
            test_data["gcp_region"],
            test_data["include_terraform"],
            test_data["include_github_actions"],
            test_data["run_initial_setup"]
        ])
        
        # Run cookiecutter
        try:
            result = subprocess.run(
                ['cookiecutter', str(template_path), '--no-input'],
                input=cookiecutter_input,
                text=True,
                capture_output=True,
                timeout=60
            )
            
            if result.returncode != 0:
                print(f"❌ Template generation failed:")
                print(f"STDOUT: {result.stdout}")
                print(f"STDERR: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("❌ Template generation timed out")
            return False
        except FileNotFoundError:
            print("❌ cookiecutter not found. Please install it: pip install cookiecutter")
            return False
        
        # Verify generated structure
        project_path = Path(tmp_dir) / test_data["project_name"]
        
        required_files = [
            "package.json",
            "pnpm-workspace.yaml",
            "tsconfig.json",
            "eslint.config.cjs",
            ".gitignore",
            "README.md",
            f"services/{test_data['service_name']}/package.json",
            f"services/{test_data['service_name']}/src/server.ts",
            f"services/{test_data['service_name']}/src/index.ts",
            f"services/{test_data['service_name']}/tests/index.test.ts",
            "terraform/main.tf",
            "terraform/variables.tf",
            ".github/workflows/ci.yml",
            ".vscode/settings.json"
        ]
        
        missing_files = []
        for file_path in required_files:
            if not (project_path / file_path).exists():
                missing_files.append(file_path)
        
        if missing_files:
            print(f"❌ Missing required files: {missing_files}")
            return False
        
        # Check if templating worked correctly
        package_json = project_path / "package.json"
        content = package_json.read_text()
        
        if test_data["project_name"] not in content:
            print("❌ Project name not templated correctly in package.json")
            return False
        
        if test_data["author_name"] not in content:
            print("❌ Author name not templated correctly in package.json")
            return False
            
        # Check service file
        service_index = project_path / f"services/{test_data['service_name']}/src/index.ts"
        service_content = service_index.read_text()
        
        if test_data["service_port"] not in service_content:
            print("❌ Service port not templated correctly")
            return False
        
        print("✅ All tests passed!")
        return True

if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)