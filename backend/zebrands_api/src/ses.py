import boto3
from botocore.exceptions import ClientError


class Email:
    SENDER = "info@mitco.cloud"
    AWS_REGION = "us-east-1"
    CHARSET = "UTF-8"
    ACCESS_ID = 'AKIAYALF2HILTIZD5Q7L'
    ACCESS_KEY = '0XMPNN2zd3qfFHimj0mMFrtYuxd7q4Q0L/LBUE2W'

    def __init__(self, recipient, subject, message_html, message_text=""):
        self.recipient = recipient
        self.subject = subject
        self.message_text = message_text
        self.message_html = message_html

    def send(self):
        # Create a new SES resource and specify a region.
        client = boto3.client('ses',
                              aws_access_key_id=self.ACCESS_ID,
                              aws_secret_access_key=self.ACCESS_KEY,
                              region_name=self.AWS_REGION)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [self.recipient, ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': Email.CHARSET,
                            'Data': self.message_html,
                        },
                        'Text': {
                            'Charset': Email.CHARSET,
                            'Data': self.message_text,
                        },
                    },
                    'Subject': {
                        'Charset': Email.CHARSET,
                        'Data': self.subject,
                    },
                },
                Source=Email.SENDER,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID: {}".format(response['MessageId'])),
            return response['MessageId']
