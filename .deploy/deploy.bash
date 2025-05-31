gcloud functions deploy hello-cf \
    --project=paranoid-playground \
    --region=us-east1 \
    --runtime=python39 \
    --memory=256MB \
    --trigger-http \
    --source=$(pwd)/source \
    --entry-point=fn_hook \
    --allow-unauthenticated \
    --vpc-connector=default