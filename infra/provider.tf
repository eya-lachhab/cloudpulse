provider "render" {
  api_key  = var.render_api_key
  owner_id = var.render_owner_id
}

variable "render_api_key" {
  type      = string
  sensitive = true
}

variable "render_owner_id" {
  type      = string
  sensitive = true
}