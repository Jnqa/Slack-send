from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

client = WebClient(token="${{ inputs.SLACK_TOKEN }}")

try:
    if "${{ inputs.FILENAME }}":
        response = json.loads(client.files_upload(channels="${{ inputs.CHANNELS }}",
                                   initial_comment="""${{ inputs.MESSAGE_TEXT }}""",
                                   file="${{ inputs.FILENAME }}",))
        print(f"Result(with file):\n{response}")
        timestamp = response["file"]["timestamp"]
        client.reactions_add(channel="${{ inputs.CHANNELS }}", name="white_check_mark", timestamp=timestamp)
    else:
        response = client.chat_postMessage(channel="${{ inputs.CHANNELS }}",
                                           text="""${{ inputs.MESSAGE_TEXT }}""" )
        print(f"Result:\n{type(response)}")
except Exception as error:
    print(f"Error: \n{error}")
    response = json.loads(client.chat_postMessage(channel="${{ inputs.CHANNELS }}",
                                       text="""${{ inputs.MESSAGE_TEXT }}${{ inputs.ERROR_TEXT }}"""))
    print(f"Result:\n{type(response)}")
    timestamp = response["ts"]
    print(f"Timestamp:\n{timestamp}")
    client.reactions_add(channel="${{ inputs.CHANNELS }}", name="warning", timestamp=timestamp)
