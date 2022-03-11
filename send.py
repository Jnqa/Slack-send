from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="${{ inputs.SLACK_TOKEN }}")

message_ts = None

try:
    if "${{ inputs.FILENAME }}":
        response_main = client.chat_postMessage(channel="${{ inputs.CHANNELS }}", text="""${{ inputs.MESSAGE_TEXT }}""")
        print(f"Result(Main):\n{response_main}")
        try:
            message_ts = response_main["ts"]
        except Exception as err:
            print(f"ERR! No message_ts cuz: {err}")
        response = client.files_upload(channels="${{ inputs.CHANNELS }}",
                                       initial_comment="""${{ inputs.MESSAGE_TEXT }}""",
                                       file="${{ inputs.FILENAME }}",
                                       thread_ts=message_ts)
        print(f"Result(with file):\n{response}")
        # try:
        #     timestamp = str(response).split("'timestamp': '", 1)[1].split("'", 1)[0]
        #     print(f"Timestamp:\n{timestamp}")
        #     client.reactions_add(channel="${{ inputs.CHANNELS }}", name="white_check_mark", timestamp=timestamp)
        # except Exception as error:
        #     print(f"ERROR: No reaction:{error}")
    else:
        response_main = client.chat_postMessage(channel="${{ inputs.CHANNELS }}", text="""${{ inputs.MESSAGE_TEXT }}""")
        print(f"Result:\n{response}")
except Exception as error:
    print(f"ERR! Error: \n{error}")
    response = client.chat_update(channel="${{ inputs.CHANNELS }}",
                                  text="""${{ inputs.MESSAGE_TEXT }}${{ inputs.ERROR_TEXT }}""",
                                  ts=message_ts)
    print(f"Result:\n{response}")
    # try:
    #     timestamp = str(response).split("'ts': '", 1)[1].split("'", 1)[0]
    #     print(f"Timestamp:\n{timestamp}")
    #     client.reactions_add(channel="${{ inputs.CHANNELS }}", name="warning", timestamp=timestamp)
    # except Exception as error:
    #     print(f"ERROR: No reaction:{error}")
