{% if cookiecutter.include_terraform == 'yes' %}
# Configure Terraform backend for remote state storage
# Uncomment and configure when ready to use remote state

# terraform {
#   backend "gcs" {
#     bucket = "{{cookiecutter.project_name}}-terraform-state"
#     prefix = "terraform/state"
#   }
# }
{% endif %}