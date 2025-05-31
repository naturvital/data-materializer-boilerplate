gcloud builds submit --tag gcr.io/paranoid-playground/data-materializer-boilerplate

gcloud beta run jobs create sample-job \
  --image gcr.io/paranoid-playground/data-materializer-boilerplate \
  --region=us-east1 \
  --service-account=nv-bq-default-usr@paranoid-playground.iam.gserviceaccount.com