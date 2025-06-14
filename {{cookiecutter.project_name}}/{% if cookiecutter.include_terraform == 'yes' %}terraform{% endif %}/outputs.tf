{% if cookiecutter.include_terraform == 'yes' %}
output "service_url" {
  description = "URL of the deployed Cloud Run service"
  value       = google_cloud_run_v2_service.{{cookiecutter.service_name|replace('-', '_')}}.uri
}

output "service_status" {
  description = "Status of the Cloud Run service"
  value       = google_cloud_run_v2_service.{{cookiecutter.service_name|replace('-', '_')}}.terminal_condition
}
{% endif %}