resource "render_web_service" "cloudpulse" {
  name           = "cloudpulse"
  plan           = "free"
  region         = "frankfurt"
  environment_id = "evm-dai663jm8hqs73eh21a0"

  runtime_source = {
    image = {
      image_url = "ghcr.io/eya-lachhab/cloudpulse"
      tag       = "latest"
    }
  }
}