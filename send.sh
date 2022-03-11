curl -F file=@${{ inputs.FILENAME }} \
        -F "initial_comment=${{ inputs.MESSAGE_TEXT }}" \
        -F channels=${{ inputs.CHANNELS }} \
        -H "Authorization: Bearer ${{ inputs.SLACK_TOKEN }}" \
        https://slack.com/api/files.upload