---
title: SMS gateway | Moodle Developer Resources
url: https://moodledev.io/docs/4.5/apis/plugintypes/sms
source: sitemap
fetched_at: 2026-02-17T15:12:43.724012-03:00
rendered_js: false
word_count: 0
summary: This PHP code provides the implementation for an AWS SNS SMS gateway, detailing the methods for formatting recipient numbers and dispatching messages through the service.
tags:
    - php
    - aws-sns
    - sms-gateway
    - cloud-messaging
    - api-integration
    - moodle-development
category: reference
---

```
<?php
namespacesmsgateway_aws;

usesmsgateway_aws\local\service\aws_sns;

classgatewayextends\core_sms\gateway{
#[\Override]
publicfunctionsend(
message$message,
):message{
// Sample code to send an SMS message.
$config=(object)json_decode(
$awsconfig,
true,
512,
JSON_THROW_ON_ERROR,
);
$class=$this->get_gateway_service($config);
$recipientnumber=manager::format_number(
phonenumber:$message->recipientnumber,
countrycode:isset($config->countrycode)??null,
);

$status=call_user_func(
[$class,'send_sms_message'],
$message->content,
$recipientnumber,
$config,
);

return$message->with(
status:$status,
);
}

privatefunctionget_gateway_service(\stdClass$config):string{
returnmatch($config->gateway){
'aws_sns'=>aws_sns::class,
default=>thrownewmoodle_exception("Unknown Message Handler {$config->gateway}"),
};
}

#[\Override]
publicfunctionget_send_priority(message$message):int{
return50;
}
}

```