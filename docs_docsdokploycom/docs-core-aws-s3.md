---
title: AWS S3 | Dokploy
url: https://docs.dokploy.com/docs/core/aws-s3
source: crawler
fetched_at: 2026-02-14T14:13:06.054714-03:00
rendered_js: true
word_count: 289
summary: This guide provides step-by-step instructions for configuring Amazon S3 as a backup destination, including setting up IAM policies and generating access credentials for integration.
tags:
    - aws-s3
    - backup-storage
    - iam-policy
    - access-keys
    - dokploy
    - cloud-configuration
category: guide
---

S3 Destinations

Configure S3 buckets for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

AWS provides a simple and cost-effective way to store and retrieve data. It is a cloud-based service that allows you to store and retrieve data from anywhere in the world. This is a great option for storing backups, as it is easy to set up and manage.

1. Create a new bucket and set any name you want.
2. Search for `IAM` in the search bar.
3. Click on `Policies` in the left menu.
4. Click on `Create Policy`.
5. Select `JSON` and paste the following policy: Make sure to replace the bucket name with your bucket name.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowListBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::bucket-name"
    },
    {
      "Sid": "AllowBucketObjectActions",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      // Make sure to set the name of your bucket
      "Resource": "arn:aws:s3:::bucket-name/*"
    }
  ]
}
```

06. Click on `Review Policy`.
07. Assign a name to the policy.
08. Click on `Create Policy`.
09. Click on User Group and assign a Name.
10. Click on `Add User to Group`.
11. Add the user you want to assign to the group.
12. In the `Attached Policies` section, filter by type `Customer Managed` and select the policy you created.
13. Click on `Attach Policy`.
14. Go to `Users` and select the user you've assigned to the group.
15. Go to Security Credentials.
16. Click on `Create Access Key`.
17. Select `Programmatic Access`.
18. Click on `Create New Access Key`.

Now copy the following variables:

- `Access Key` -&gt; `Access Key (Dokploy)` = eg. `AK2AV244NFLS5JTUZ554`
- `Secret Key` -&gt; `Secret Key (Dokploy)` = eg. `I0GWCo9fSGOr7z6Lh+NvHmSsaE+62Vwk2ua2CEwR`
- `Bucket` -&gt; `Bucket (Dokploy)` = eg. `dokploy-backups` use the name of the bucket you created.
- `Region` -&gt; `Region (Dokploy)` = eg. `us-east-1, us-west-2, etc` it will depend on the region you are using.
- `Endpoint` -&gt; `Endpoint (Dokploy) (Optional)` = eg. `https://s3.<region>.amazonaws.com` you will find this endpoint in the Bucket Card at the Home Page.

Test the connection and you should see a success message.