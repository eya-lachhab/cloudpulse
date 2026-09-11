terraform {
  required_version = ">= 1.6"

  cloud {
    organization = "eya-lachhab"

    workspaces {
      name = "cloudpulse"
    }
  }

  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.8"
    }
  }
}