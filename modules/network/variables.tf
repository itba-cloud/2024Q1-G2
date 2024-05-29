variable "vpc_name" {
  description = "Name of the VPC"
  type        = string
  default     = "CC-2024Q1-G2"
}
variable "vpc_cidr" {
  description = "CIDR of the VPC"
  type        = string
}
variable "public_cidr" {
  description = "CIDR of the public subnet"
  type        = string
}
variable "public_az" {
  description = "Name of the public availability zone"
  type        = string
}