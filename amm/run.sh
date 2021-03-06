#!/usr/bin/env bash
aws cloudformation create-stack --stack-name $1 --template-body file://amm-master.cfn.json --parameters file://launch-params.json --capabilities CAPABILITY_IAM --disable-rollback