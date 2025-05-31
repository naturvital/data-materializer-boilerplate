import json
from http import HTTPStatus
from google.cloud import bigquery
from flask import Request, Response


def fn_hook(request: Request):
  
  if request.method != 'POST':
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)
  
  if not request.data:
    return Response(status=HTTPStatus.BAD_REQUEST)
  
  result = process_message(request.json)
  
  return Response(json.dumps(result), status=HTTPStatus.OK, content_type='application/json')


def process_message(payload: dict):
  client = bigquery.Client()
  query = """
  SELECT COUNT(*) AS total
  FROM `paranoid-playground.snapshots.oinv`
  """
  
  result = client.query(query).result()
  row = next(result)  # only one row expected
  return {"total": row["total"]}
