{% if cookiecutter.include_terraform == 'yes' %}
terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_v2_service" "{{cookiecutter.service_name|replace('-', '_')}}" {
  name     = "{{cookiecutter.service_name}}"
  location = var.region

  template {
    containers {
      image = "gcr.io/${var.project_id}/{{cookiecutter.service_name}}:latest"
      
      ports {
        container_port = {{cookiecutter.service_port}}
      }

      env {
        name  = "PORT"
        value = "{{cookiecutter.service_port}}"
      }

      resources {
        limits = {
          cpu    = "1000m"
          memory = "512Mi"
        }
      }
    }

    scaling {
      min_instance_count = 0
      max_instance_count = 10
    }
  }

  traffic {
    percent = 100
    type    = "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"
  }
}

# Allow unauthenticated access
resource "google_cloud_run_v2_service_iam_binding" "{{cookiecutter.service_name|replace('-', '_')}}_noauth" {
  location = google_cloud_run_v2_service.{{cookiecutter.service_name|replace('-', '_')}}.location
  name     = google_cloud_run_v2_service.{{cookiecutter.service_name|replace('-', '_')}}.name
  role     = "roles/run.invoker"
  members = [
    "allUsers",
  ]
}
{% endif %}