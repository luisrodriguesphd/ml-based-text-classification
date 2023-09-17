uvicorn serving.app:app --host 0.0.0.0 --port 7860
# gunicorn app:app --access-logfile - --workers 2 --worker-class uvicorn.workers.UvicornWorker --max-requests 10 --bind 0.0.0.0:7860