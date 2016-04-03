# cfn-templates
AWS CloudFormation Templates - Infrastructure as Code

## Overview
The infrastructure, resources, and application into three templates:

1. master - parent template that defines embeded Cloud Formation stacks.
2. resources - stack to define all dependancies for the application (RDS databases, ElastiCache cluster, DynamoDB tables, S3 bucket, IAM roles, etc.  It outputs all IDs it creates.
3. application - stack to define the application and environment that runs our application.  This stack depends on the outputs provided by the resources stack.

## Template sections
```javascript
{
  "AWSTemplateFormatVersion" : "version date",

  "Description" : "JSON string",

  "Metadata" : {
    //template metadata
  },

  "Parameters" : {
    //set of parameters
  },

  "Mappings" : {
    //set of mappings
  },

  "Conditions" : {
    //set of conditions
  },

  "Resources" : {
    //set of resources
  },

  "Outputs" : {
    //set of outputs
  }
}
```

## References
- [AWS CloudFormation Best Practices](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html "AWS CloudFormation Best Practices")
- [Template Anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html "Template Anatomy")
- [Sample Templates](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-sample-templates.html "Sample Templates")
- [Modeling an Elastic Beanstalk Application and its Dependencies in CloudFormation](https://blogs.aws.amazon.com/application-management/post/Tx2DUJYZVBMJ92J/Part-1-Develop-Deploy-and-Manage-for-Scale-with-Elastic-Beanstalk-and-CloudForma "Modeling an Elastic Beanstalk Application and its Dependencies in CloudFormation")

