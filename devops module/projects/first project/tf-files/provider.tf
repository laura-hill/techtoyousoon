terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.24.0"
    }
    github = {
      source = "integrations/github"
      version = "4.28.0"
    }    
  }
}

provider "aws" {
  # Configuration options
  region = "us-east-1"
// profile = "xxxxxxxx" # do not use this one
  access_key = "AKIAQCAXGPQGUAQY6DWG"
  secret_key = "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"
# Configuration options
}

provider "github" {
  # Configuration options
  token = "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"
}