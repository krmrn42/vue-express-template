#!/usr/bin/env python3
"""
Pre-generation hook for validation and setup checks.
"""

import re
import sys

def validate_project_name(name):
    """Validate project name follows conventions."""
    if not re.match(r'^[a-z][a-z0-9-]*$', name):
        print("❌ Project name must start with lowercase letter and contain only lowercase letters, numbers, and hyphens")
        return False
    return True

def validate_service_name(name):
    """Validate service name follows conventions."""
    if not re.match(r'^[a-z][a-z0-9-]*$', name):
        print("❌ Service name must start with lowercase letter and contain only lowercase letters, numbers, and hyphens")
        return False
    return True

def validate_service_port(port):
    """Validate service port is reasonable."""
    try:
        port_num = int(port)
        if not (1024 <= port_num <= 65535):
            print("❌ Service port must be between 1024 and 65535")
            return False
    except ValueError:
        print("❌ Service port must be a number")
        return False
    return True

def validate_gcp_project_id(project_id):
    """Validate GCP project ID format."""
    if not re.match(r'^[a-z][a-z0-9-]*[a-z0-9]$', project_id):
        print("❌ GCP project ID must start with lowercase letter, contain only lowercase letters, numbers, and hyphens, and end with letter or number")
        return False
    if len(project_id) < 6 or len(project_id) > 30:
        print("❌ GCP project ID must be between 6 and 30 characters")
        return False
    return True

def main():
    """Run pre-generation validations."""
    project_name = "{{ cookiecutter.project_name }}"
    service_name = "{{ cookiecutter.service_name }}"
    service_port = "{{ cookiecutter.service_port }}"
    gcp_project_id = "{{ cookiecutter.gcp_project_id }}"
    
    print("🔍 Validating template parameters...")
    
    if not validate_project_name(project_name):
        sys.exit(1)
    
    if not validate_service_name(service_name):
        sys.exit(1)
    
    if not validate_service_port(service_port):
        sys.exit(1)
    
    if not validate_gcp_project_id(gcp_project_id):
        sys.exit(1)
    
    print("✅ All validations passed!")

if __name__ == '__main__':
    main()