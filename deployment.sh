#bin/bash

gcloud builds submit --tag gcr.io/regal-state-230718/tango-test

gcloud run deploy \
  --image gcr.io/regal-state-230718/tango-test \
  --platform managed \
  --allow-unauthenticated \
  --region us-central1 \
  --vpc-connector redis-connect \
  --set-env-vars REDISHOST=10.108.243.219,REDISPORT=6379





