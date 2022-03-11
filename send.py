from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="${{ inputs.SLACK_TOKEN }}")

message_ts = None

try:
    response_main = client.chat_postMessage(channel="${{ inputs.CHANNELS }}", text="""${{ inputs.MESSAGE_TEXT }}""")
    print(f"Result(Main):\n{response_main}")
    try:
        message_ts = response_main["ts"]
    except Exception as err:
        print(f"ERR! No message_ts cuz: {err}")
    if "${{ inputs.FILENAME }}":
        response = client.files_upload(channels="${{ inputs.CHANNELS }}",
                                       file="${{ inputs.FILENAME }}",
                                       thread_ts=message_ts)
        print(f"Result(with file):\n{response}")
except Exception as error:
    print(f"ERR! Error: \n{error}")
    response = client.chat_update(channel="${{ inputs.CHANNELS }}",
                                  text="""${{ inputs.MESSAGE_TEXT }}${{ inputs.ERROR_TEXT }}""",
                                  ts=message_ts)
    print(f"Result:\n{response}")
