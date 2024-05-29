variable "account_id" {
  description = "ID of your AWS account"
  type        = string
}
variable "api_gateway_url" {
  description = "URL to invoke the API pointing to the stage"
  type        = string
}
variable "subnet_ids" {
  description = "IDs of subnets"
  type        = list(string)
}
variable "region" {
  description = "Region of your deployed architecture"
  type        = string
}