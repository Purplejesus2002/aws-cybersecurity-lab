# AWS Cybersecurity Lab Environment

## Overview
This project focuses on building a secure AWS cloud environment designed for cybersecurity testing and monitoring. It utilizes AWS services such as EC2, VPC, CloudWatch, GuardDuty, and WAF to establish a multi-layered security architecture.

## Architecture
The architecture includes:
- **Virtual Private Cloud (VPC)** with both public and private subnets
- **EC2 instance** for hosting, with automated patch management
- **Internet Gateway** and custom **Route Table** for public subnet access
- **CloudWatch** for monitoring and **VPC Flow Logs** for logging traffic
- **AWS GuardDuty** and **Inspector** for threat detection and vulnerability scanning
- **AWS WAF** for web application protection

## Setup Guide

### 1. Create a Virtual Private Cloud (VPC)
1. In the AWS Console, navigate to **VPC** > **Create VPC**.
2. Name the VPC and assign a CIDR block 
3. Create a **Public Subnet** with CIDR block `********` and enable auto-assign public IPs.
4. Create an **Internet Gateway** and attach it to the VPC.
5. Create a **Route Table** for the VPC and add a route `0.0.0.0/0` targeting the Internet Gateway.
6. Associate the route table with the public subnet.

### 2. Launch an EC2 Instance
1. Navigate to **EC2** > **Launch Instance** and select the **Ubuntu Server 20.04 LTS** AMI.
2. Select the instance type (`t2.micro` for free-tier eligibility).
3. Configure network settings:
   - Select the VPC and Public Subnet.
   - Ensure that **Auto-assign Public IP** is enabled.
4. Configure security group rules:
   - Open **SSH (Port 22)** for your IP address.
   - Customize additional rules based on specific needs (e.g., HTTP/HTTPS).
5. Launch the instance and connect using SSH:
   ```bash

   References:
AWS Documentation
Ubuntu UFW Guide
Amazon CloudWatch Logs
AWS WAF Managed Rules
  
### Image and Video Analysis with AWS Rekognition

**Purpose**: AWS Rekognition provides advanced image and video analysis, enabling automated detection of objects, text, scenes, and activities. For this project, AWS Rekognition can be integrated as an additional security layer to monitor visual content or as a data analysis tool.

**Use Cases**:
- **Security Monitoring**: Analyze images or video feeds to detect suspicious objects or activities.
- **Content Management**: Automatically tag and categorize images, which is useful for managing media assets securely in S3.

**Setup Guide**:

#### 1. Create an S3 Bucket for Image Storage
1. Go to the **S3 Dashboard** and create a new bucket (e.g., `my-security-images-bucket`).
2. Set appropriate permissions for AWS Rekognition to access the images in this bucket.
   
#### 2. Configure IAM Permissions for Rekognition
1. Go to the **IAM Dashboard** > **Policies** > **Create Policy**.
2. Add the following permissions for Rekognition and S3:
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:GetObject",
                   "s3:PutObject",
                   "s3:ListBucket"
               ],
               "Resource": "arn:aws:s3:::my-security-images-bucket/*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "rekognition:DetectLabels",
                   "rekognition:DetectModerationLabels"
               ],
               "Resource": "*"
           }
       ]
   }

