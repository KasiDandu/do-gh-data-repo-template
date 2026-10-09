# Data pipeline repo

Created from `do-gh-data-repo-template`.

## What you edit

| Folder | Contents |
|---|---|
| `config/glue/` | `{env}_glue_job_config.yaml`: Glue job settings per environment |
| `config/lambda/` | `{env}_config.yaml`: Lambda settings per environment (optional) |
| `src/glue/` | ETL code. `main.py` is the Glue entry script; other modules ship via `--extra-py-files` |
| `src/lambda/` | Lambda handler (optional) |
| `tests/` | PyTests, which must pass before merge |
| `mappings/`, `schemas/`, `sql/` | Pipeline-specific assets |

**Do not modify `.github/`.** The workflows call `do-gh-shared-actions` and are owned by the
platform team.

## How deployment works

- Push to any branch: tests, then code is uploaded to S3, then the `dev` config is committed to the
  same branch name in `do-aws-pipeline-infra`, which runs `terraform apply`.
- Tag `tc-*` deploys to test, `pp-*` to preprod, `pd-*` to prod.

Repo variables (set by the platform repo): `DATA_PIPELINE`, `BLUEPRINT_TYPE`,
`ENABLE_GLUE`, `ENABLE_LAMBDA`. Repo secret: `GH_AUTOMATION_TOKEN`.

## Local checks

```bash
bash ci/setup.sh
.venv/bin/pre-commit run --all-files
.venv/bin/pytest -q tests/
```
