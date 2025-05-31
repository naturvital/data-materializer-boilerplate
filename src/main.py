import logging
import sys
from google.cloud import bigquery


# Configure logging at module level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


def main():
  
  logger.info('Starting job execution')
  
  try:
    result = materialize()
    logger.info(f"Query result: {result}")
  except Exception as e:
    logger.exception("Job failed due to an error")
    raise
  
  logger.info('Finishing job execution')


def materialize():
  
  client = bigquery.Client()
  
  query = """
  SELECT COUNT(*) AS total
  FROM `paranoid-playground.snapshots.oinv`
  """
  
  result = client.query(query).result()
  row = next(result)
  
  return {"total": row["total"]}
