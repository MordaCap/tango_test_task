# tango_test_task
Tango test task repo

Deployment to the gcp cloud run with redis: 
<br> ./deployment.sh
or follow commands:
1) gcloud builds submit --tag gcr.io/regal-state-230718/tango-test
2) gcloud run deploy \                                                 
--image gcr.io/regal-state-230718/tango-test \
--platform managed \
--allow-unauthenticated \
--region us-central1 \
--vpc-connector redis-connect \
--set-env-vars REDISHOST=10.108.243.219,REDISPORT=6379
   
<br><br>

-> curl -X GET https://gcp-tango-okdpdxpega-uc.a.run.app/
Hello

-> curl -X GET https://gcp-tango-okdpdxpega-uc.a.run.app/ping
pong

-> curl -X POST https://tango-test-task-end-okdpdxpega-uc.a.run.app/test/user_id
user_id

-> curl -X GET https://tango-test-task-end-okdpdxpega-uc.a.run.app/get_test
ttl_cache: b'user_id, di_resu'

(5 sec) 
-> curl -X GET https://tango-test-task-end-okdpdxpega-uc.a.run.app/get_test
redis_cache: b'user_id, di_resu'

(~2 sec) 
-> curl -X GET https://tango-test-task-end-okdpdxpega-uc.a.run.app/get_test
ttl_cache: b'user_id, di_resu'

(5 sec) 
-> curl -X GET https://tango-test-task-end-okdpdxpega-uc.a.run.app/get_test
redis_cache: b'user_id, di_resu'
