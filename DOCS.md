# Home Assistant Add-on: AWS SQS Subscriber

## Installation

Follow these steps to get the add-on installed on your system:

1. Navigate in your Home Assistant frontend to **Supervisor** -> **Add-on Store**.
2. Find the "AWS SQS Subscriber" add-on and click it.
3. Click on the "INSTALL" button.

## How to use

The add-on has a couple of options available. To get the add-on running:

1. Start the add-on.
2. Have some patience and wait a couple of minutes.
3. Check the add-on log output to see the result.

If you have old AWS SQS Subscriber settings available, remove this old integration and restart Home Assistant to see the new one.

## Configuration

Add-on configuration:

```yaml
sqs_queue: '',
aws_access_key: '',
aws_secret_key: '',
aws_region: ''
```

### Option: `sqs_queue`

URL to SQS queue:

```yaml
sqs_queue: https://sqs.us-west-2.amazonaws.com/1234567890/queuename
```

### Option: `aws_access_key`

AWS access key of IAM user.

#### Option: `aws_secret_key`

AWS secret key of IAM user.

#### Option: `aws_region`

AWS region where queue located.

Default value: `us-west-2`

## Support

Got questions?

In case you've found a bug, please [open an issue on our GitHub][issue].