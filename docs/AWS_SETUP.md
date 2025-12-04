# AWS Setup Guide

## Option 1: Install AWS CLI (Recommended)

1. Download AWS CLI for Windows: https://aws.amazon.com/cli/
2. Run the installer
3. Restart your terminal
4. Run: `aws configure`
5. Enter your AWS Access Key ID, Secret Access Key, and region

## Option 2: Manual Credentials File

Create a file at: `C:\Users\YourUsername\.aws\credentials`

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-east-1
```

## Option 3: Environment Variables

Set these in PowerShell:

```powershell
$env:AWS_ACCESS_KEY_ID="your-access-key"
$env:AWS_SECRET_ACCESS_KEY="your-secret-key"
$env:AWS_REGION="us-east-1"
```

## Verify Setup

After configuration, test with:

```python
python -c "import boto3; print(boto3.client('bedrock-runtime'))"
```

If no errors, you're ready to use the Rap Battle Arena!

