- [Pre-requisites](#pre-requisites)
  - [Create container registry](#create-container-registry)
  - [Build and push the image](#build-and-push-the-image)
- [Architecture Overview](#architecture-overview)
- [Terraform](#terraform)
  - [Requirements](#requirements)
  - [Providers](#providers)
  - [Modules](#modules)
  - [Resources](#resources)
  - [Inputs](#inputs)
  - [Outputs](#outputs)
  - [Functions](#functions)
  - [Meta-arguments](#meta-arguments)

# Pre-requisites
In order to give our cluster a base Image that will be used to compute the data and make the analysis we need to build an Image using docker , and store it on container Registry.
## Create container registry
In ECR Service on AWS Console , create the container registry `sentimental-analysis`
## Build and push the image
Configure aws cli on your local machine so it has access to the lab (see Configure AWS CLI part)

In ECR Service , click on view push commands.

On your local machine , go the directory where our Dockerfile is stored and copy paste all commands

Verify that the image is in the repository

# Architecture Overview
![architecture-overview](https://i.imgur.com/NeOvXwK.png)


# Terraform
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.49.0 |

## Providers

No providers.

## Modules

| Name | Source | Purpose |
|------|--------|---------|
| <a name="module_application"></a> [application](modules/application) | ./modules/application | Custom module that initiates both AWS Lambda & AWS API Gateway |
| <a name="module_compute"></a> [compute](modules/compute) | ./modules/compute | Custom module that initiates an EventBride Scheduler cron, an ECS cluster and defines an ECS task |
| <a name="module_database"></a> [database](modules/database) | ./modules/database | External module that initates two DynamoDB databases |
| <a name="module_network"></a> [network](modules/network) | ./modules/network | Custom module that initiates the VPC and its components |
| <a name="module_security"></a> [security](modules/security) | ./modules/security | Custom module that initiates a SG |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_id"></a> [account\_id](#input\_account\_id) | ID of your AWS account | `string` | n/a | yes |
| <a name="input_aws_region"></a> [aws\_region](#input\_aws\_region) | AWS region for all resources | `string` | n/a | yes |
| <a name="input_db_billing_mode"></a> [db\_billing\_mode](#input\_db\_billing\_mode) | Billing mode for the Dynamo database | `string` | `"PAY_PER_REQUEST"` | no |
| <a name="input_public_az"></a> [public\_az](#input\_public\_az) | Name of the public availability zone | `string` | n/a | yes |
| <a name="input_public_cidr"></a> [public\_cidr](#input\_public\_cidr) | CIDR of the public subnet | `string` | n/a | yes |
| <a name="input_table_names"></a> [table\_names](#input\_table\_names) | Name of the DynamoDB tables | `list(string)` | <pre>[<br>  "tweets-raw",<br>  "tweets-processed"<br>]</pre> | no |
| <a name="input_vpc_cidr"></a> [vpc\_cidr](#input\_vpc\_cidr) | CIDR of the VPC | `string` | n/a | yes |
| <a name="input_vpc_name"></a> [vpc\_name](#input\_vpc\_name) | Name of the VPC | `string` | `"CC-2024Q1-G2"` | no |

## Outputs

No outputs.

## Functions
| Name | Source | Purpose |
|------|--------|---------|
| <a name="function_jsonencode"></a> [jsonencode](https://developer.hashicorp.com/terraform/language/functions/jsonencode) | [./modules/compute/main.tf](modules/compute/main.tf#L16) | Encode the `container_definitions` to a string from a JSON format|
| <a name="function_sha1"></a> [sha1](https://developer.hashicorp.com/terraform/language/functions/sha1) | [./modules/compute/main.tf](modules/application/main.tf#L178) | Computes the SHA1 of the API resources for redeployment purposes|
| <a name="function_toset"></a> [sha1](https://developer.hashicorp.com/terraform/language/functions/toset) | [./modules/compute/main.tf](modules/database/main.tf#L3) | Converting `var.table_names` to a set for iteration purposes|
| <a name="function_lower"></a> [sha1](https://developer.hashicorp.com/terraform/language/functions/lower) | [./modules/compute/main.tf](main.tf#L3) | Forcing lowercase for `var.vpc_name` to mantain styling consistency|

## Meta-arguments
<!-- END_TF_DOCS -->