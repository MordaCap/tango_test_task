# tango_test_task
Tango test task repo

Deployment ot the gcp cloud run with redis: 
<br> ./deployment.sh
or follow commands:
1) gcloud builds submit --tag gcr.io/regal-state-230718/tango-test-task
2) gcloud run deploy \                                                 
--image gcr.io/regal-state-230718/tango-test-task \
--platform managed \
--allow-unauthenticated \
--region us-central1 \
--vpc-connector redis-connect \
--set-env-vars REDISHOST=10.206.9.131,REDISPORT=6378
   
<br><br>
