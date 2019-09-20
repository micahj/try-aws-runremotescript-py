# try-aws-runremotescript-py

    {"owner":"micahj", "repository":"try-aws-runremotescript-py"}

ssm sample code from aws console for triggering this: AWS-RunRemoteScript.\
Send sns message
```
aws ssm send-command --document-name "AWS-RunRemoteScript" --document-version "1" --targets '[{"Key":"InstanceIds","Values":["i-032995e31f28226b7"]}]' --parameters '{"sourceType":["GitHub"],"sourceInfo":["{\"owner\":\"micahj\", \"repository\":\"try-aws-runremotescript-py\"}"],"commandLine":["main.py"],"workingDirectory":[""],"executionTimeout":["3600"]}' --timeout-seconds 600 --max-concurrency "50" --max-errors "0" --service-role-arn "arn:aws:iam::883671954021:role/DevOpsSSMAutomationRole" --notification-config '{"NotificationArn":"try-aws-runremotescript","NotificationEvents":["All"],"NotificationType":"Command"}' --region ap-southeast-2
```

write to s3
```
aws ssm send-command --document-name "AWS-RunRemoteScript" --document-version "1" --targets '[{"Key":"InstanceIds","Values":["i-032995e31f28226b7"]}]' --parameters '{"sourceType":["GitHub"],"sourceInfo":["{\"owner\":\"micahj\", \"repository\":\"try-aws-runremotescript-py\"}"],"commandLine":["main.py"],"workingDirectory":[""],"executionTimeout":["3600"]}' --timeout-seconds 600 --max-concurrency "50" --max-errors "0" --output-s3-bucket-name "devops-patching-dev" --output-s3-key-prefix "micahj-tests" --region ap-southeast-2
```