{% if cookiecutter.include_terraform == 'yes' %}
variable "project_id" {
  description = "The GCP project ID"
  type        = string
  default     = "{{cookiecutter.gcp_project_id}}"
}

variable "region" {
  description = "The GCP region for resources"
  type        = string
  default     = "{{cookiecutter.gcp_region}}"
}

variable "service_name" {
  description = "Name of the Cloud Run service"
  type        = string
  default     = "{{cookiecutter.service_name}}"
}
{% endif %}