output "instance_public_ip" {
  description = "Public IP address of the TrafficOps EC2 instance"
  value       = aws_instance.trafficops.public_ip
}

output "instance_id" {
  description = "TrafficOps EC2 instance ID"
  value       = aws_instance.trafficops.id
}

output "vpc_id" {
  description = "TrafficOps VPC ID"
  value       = aws_vpc.trafficops.id
}

output "subnet_id" {
  description = "TrafficOps public subnet ID"
  value       = aws_subnet.public.id
}

output "security_group_id" {
  description = "TrafficOps security group ID"
  value       = aws_security_group.trafficops.id
}
