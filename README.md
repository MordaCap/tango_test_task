# tango_test_task
Tango test task repo

Deployment to the gcp cloud run with redis: 
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

-> curl -X GET https://tango-test-task-end-okdpdxpega-uc.a.run.app
Hello

-> curl -X GET https://tango-test-task-end-okdpdxpega-uc.a.run.app/ping
pong

(failed with connection refused by redis)
-> curl -X POST https://tango-test-task-end-okdpdxpega-uc.a.run.app/test/user_id

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
500 Internal Server Error
Internal Server Error
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.

(failed with connection refused by redis)
-> curl -X GET https://tango-test-task-end-okdpdxpega-uc.a.run.app/get_test

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
500 Internal Server Error
Internal Server Error
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.



