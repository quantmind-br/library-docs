---
title: aws-sdk-ruby · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/examples/aws/aws-sdk-ruby/index.md
source: llms
fetched_at: 2026-01-24T15:22:10.245755359-03:00
rendered_js: false
word_count: 58
summary: This document explains how to configure and use the Ruby AWS S3 SDK to interact with Cloudflare R2 storage, covering authentication and basic bucket operations.
tags:
    - cloudflare-r2
    - ruby
    - aws-sdk-s3
    - s3-compatibility
    - object-storage
category: tutorial
---

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.



Many Ruby projects also store these credentials in environment variables instead.

Add the following dependency to your `Gemfile`:

```ruby
gem "aws-sdk-s3"
```

Then you can use Ruby to operate on R2 buckets:

```ruby
require "aws-sdk-s3"


@r2 = Aws::S3::Client.new(
  # Retrieve your S3 API credentials for your R2 bucket via API tokens (see: https://developers.cloudflare.com/r2/api/tokens)
  access_key_id: "#{ACCESS_KEY_ID}",
  secret_access_key: "#{SECRET_ACCESS_KEY}",
  # Provide your Cloudflare account ID
  endpoint: "https://#{ACCOUNT_ID}.r2.cloudflarestorage.com",
  region: "auto", # Required by SDK but not used by R2
)


# List all buckets on your account
puts @r2.list_buckets


#=> {
#=>   :buckets => [{
#=>     :name => "your-bucket",
#=>     :creation_date => "…",
#=>   }],
#=>   :owner => {
#=>     :display_name => "…",
#=>     :id => "…"
#=>   }
#=> }


# List the first 20 items in a bucket
puts @r2.list_objects(bucket:"your-bucket", max_keys:20)


#=> {
#=>   :is_truncated => false,
#=>   :marker => nil,
#=>   :next_marker => nil,
#=>   :name => "your-bucket",
#=>   :prefix => nil,
#=>   :delimiter =>nil,
#=>   :max_keys => 20,
#=>   :common_prefixes => [],
#=>   :encoding_type => nil
#=>   :contents => [
#=>     …,
#=>     …,
#=>     …,
#=>   ]
#=> }
```