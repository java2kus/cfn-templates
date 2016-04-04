#!/usr/bin/env bash

BUCKET=${1-cfn-templates-dev}

echo ${BUCKET}
aws s3 sync . s3://${BUCKET} --exclude "*" --include "*.json"

