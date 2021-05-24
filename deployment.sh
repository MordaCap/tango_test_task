#bin/bash

gcloud builds submit --tag gcr.io/regal-state-230718/tango-test-task

gcloud run deploy \                                                 
--image gcr.io/regal-state-230718/tango-test-task \
--platform managed \
--allow-unauthenticated \
--region us-central1 \
--vpc-connector redis-connect \
--set-env-vars REDISHOST=10.206.9.131,REDISPORT=6378




