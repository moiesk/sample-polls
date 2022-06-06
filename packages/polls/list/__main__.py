import os
from urllib.parse import urlparse
import psycopg2

def main(args):
  
  dbUrl = os.environ['DATABASE_URL']
  p = urlparse(dbUrl)

  pg_connection_dict = {
    'dbname': p.path.strip("/"),
    'user': p.username,
    'password': p.password,
    'port': p.port,
    'host': p.hostname,
    'sslmode': 'require'
  }
  query = "SELECT COUNT(1) as count FROM polls_question"
  
  conn = psycopg2.connect(**pg_connection_dict)
  cur = conn.cursor()
  
  cur.execute(query)
  result = cur.fetchone()
  
  cur.close()
  conn.close()

  return {
    'body': {
      'question_count': result[0]
    }
  }