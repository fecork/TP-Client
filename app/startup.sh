gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app \
    --log-level=debug \
    --log-file=- \
    --access-logfile=-
