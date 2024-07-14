
from azure.communication.email import EmailClient
def main():
    try:
        connection_string = "endpoint=https://azurecommunicationservice1432.asiapacific.communication.azure.com/;accesskey=2O14idRX8JNotk4H0cMuM7hBDVNM8InfwOc5OVTXENpSRM673CheJQQJ99AGACULyCpMmx0IAAAAAZCSzRWX"
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@762151c0-6f23-4033-80cb-79d7183ae004.azurecomm.net",
            "recipients":  {
                "to": [{"address": "mohsin.reja@elevateltd.net" }],
            },
            "content": {
                "subject": "Test Email",
                "plainText": "Hello world via email.",
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)
main()
