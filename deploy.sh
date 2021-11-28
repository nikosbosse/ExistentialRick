#!bin/bash
gcloud functions deploy existentialrick \
    --project=existentialrick \
    --trigger-topic existentialrick \
    --memory=128MB \
    --env-vars-file .env.yaml \
    --region=us-central1 \
    --runtime python39 \
    --entry-point=post_tweet