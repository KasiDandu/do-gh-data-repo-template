import json
import os

import boto3

glue = boto3.client("glue")


def lambda_handler(event, context):
    """Starts the Glue job once per SQS message."""
    run_ids = []
    for record in event.get("Records", []):
        body = json.loads(record["body"])
        run = glue.start_job_run(
            JobName=os.environ["GLUE_JOB_NAME"],
            Arguments={"--TRIGGER_KEY": body.get("key", "")},
        )
        run_ids.append(run["JobRunId"])
    return {"started": run_ids}
