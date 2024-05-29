<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_ecs_cluster.compute_cluster](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_cluster) | resource |
| [aws_ecs_task_definition.process_raw_tweets](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition) | resource |
| [aws_scheduler_schedule.cron](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/scheduler_schedule) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_account_id"></a> [account\_id](#input\_account\_id) | ID of your AWS account | `string` | n/a | yes |
| <a name="input_api_gateway_url"></a> [api\_gateway\_url](#input\_api\_gateway\_url) | URL to invoke the API pointing to the stage | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | Region of your deployed architecture | `string` | n/a | yes |
| <a name="input_subnet_ids"></a> [subnet\_ids](#input\_subnet\_ids) | IDs of subnets | `list(string)` | n/a | yes |

## Outputs

No outputs.
<!-- END_TF_DOCS -->