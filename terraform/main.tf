resource "aws_vpc" "trafficops" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "trafficops-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.trafficops.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "trafficops-public-subnet"
  }
}

resource "aws_internet_gateway" "trafficops" {
  vpc_id = aws_vpc.trafficops.id

  tags = {
    Name = "trafficops-igw"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.trafficops.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.trafficops.id
  }

  tags = {
    Name = "trafficops-public-route-table"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_security_group" "trafficops" {
  name        = "trafficops-sg"
  description = "Security group for TrafficOps"
  vpc_id      = aws_vpc.trafficops.id

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.allowed_ssh_cidr]
  }

  ingress {
    description = "TrafficOps API"
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "trafficops-sg"
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "trafficops" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type

  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids     = [aws_security_group.trafficops.id]
  key_name                    = var.key_name
  associate_public_ip_address = true

  tags = {
    Name = "trafficops-ec2"
  }
}
