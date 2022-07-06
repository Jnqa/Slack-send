# Send messages and files to Slack

## Usage


```yml
      - name: Upload file to slack
        uses: Jnqa/slack-send@v1
        id: send-message
        with:
          MESSAGE_TEXT: |
            :heavy_check_mark: Hello Slack! 
          SLACK_TOKEN: ${{ secrets.SLACK_TOKEN }}
          FILENAME: example.txt
          CHANNELS: channel_name
```

Reply in Thread:
```yml
      - name: Reply in Thread
        uses: Jnqa/slack-send@v1
        with:
          MESSAGE_TEXT: Reply
          SLACK_TOKEN: ${{ secrets.SLACK_TOKEN }}
          CHANNELS: channel_name
          TS: ${{ steps.send-message.outputs.TS }}
```

or Just a message:
```yml
      - name: Message
        uses: Jnqa/slack-send@v1
        with:
          MESSAGE_TEXT: some texts.
          SLACK_TOKEN: ${{ secrets.SLACK_TOKEN }}
          CHANNELS: channel_name
```

### Action inputs

| Name | Description | Required | Default |
| --- | --- | --- | --- |
| `MESSAGE_TEXT` | Message text | `Yes` | `-` |
| `SLACK_TOKEN` | Your slack Token | `Yes` | `-` |
| `CHANNELS` | Slack channels ID where message will be posted (separated with ,) | `Yes` | `-` |
| `FILENAME` | The path to the file | `No` | `-` |
| `TIMEOUT` | Timeout (for large files) | `No` | `74` |
| `TS` | Timestamp for reply in thread  | `No` | `-` |
| `REACTION` | Reaction on message | `No` | `-` |
| `BOTPIC` | Bot Avatar | `No` | `-` |

### Action outputs

| Name | Description | Usage |
| --- | --- | --- |
| `ts` | Output timestamp | `${{ steps.<step-id>.outputs.TS }}` |
