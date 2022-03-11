from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="${{ inputs.SLACK_TOKEN }}")

try:
    if "${{ inputs.FILENAME }}":
        response = client.files_upload(channels="${{ inputs.CHANNELS }}",
                                   initial_comment="""${{ inputs.MESSAGE_TEXT }}""",
                                   file="${{ inputs.FILENAME }}",)
        print(f"Result is:\n{response}")
        client.reactions_add(channel="${{ inputs.CHANNELS }}", name="white_check_mark", timestamp=response["file"]["timestamp"])
    else:
        response = client.chat_postMessage(channel="${{ inputs.CHANNELS }}", text="""${{ inputs.MESSAGE_TEXT }}""" )
        print(response)
except Exception as error:
    print(f"Error: \n{error}")
    response = client.chat_postMessage(channel="${{ inputs.CHANNELS }}", text="""${{ inputs.MESSAGE_TEXT }}""")
    print(response)
    client.reactions_add(channel="${{ inputs.CHANNELS }}", name="warning", timestamp=response["file"]["timestamp"])
