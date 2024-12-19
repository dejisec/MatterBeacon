import os
import sys

# Your Mattermost webhook
webhookurl = "https://your-mattermost-url/hooks/your-webhook-id"

message = ' '.join(sys.argv[1:])
payload = f'{{"text": "{message}"}}'
os.system(
    f'curl --location --request POST "{webhookurl}" '
    f'--header \'Content-Type: application/json\' '
    f'--data-raw \'{payload}\''
)
