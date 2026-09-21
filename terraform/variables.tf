variable "aws_region" {
  description = "AWS region where TrafficOps infrastructure will be deployed"
  type        = string
  default     = "ap-south-1"
}


variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.small"
}

variable "key_name" {
  description = "Existing AWS EC2 key pair name"
  type        = string
}

variable "allowed_ssh_cidr" {
  description = "CIDR allowed to access SSH"
  type        = string
}
