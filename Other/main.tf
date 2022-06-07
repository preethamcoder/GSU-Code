provider "aws"{
  region = "us-east-1"
}

resource "aws_instance" "preetham_instance"{
  count = 10
  ami = "ami-0ddbdea833a8d2f0d"
  instance_type = "t2.micro"
  tags = {
    Name = "preetham_instance"
  }
}
