#!bin/bash
gcloud scheduler jobs create pubsub existentialrick \
    --project=existentialrick \
    --schedule="0 12 * * *" \
    --topic=existentialrick \
    --description="Post an existentialrick tweet" \
    --message-body="Post an existentialrick tweet"