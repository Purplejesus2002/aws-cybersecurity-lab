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
  
