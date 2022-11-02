# DeepCNNClassifier

## Workflow

1. update config.yaml
2. update secrets.yaml[optional]
3. update params.yaml
4. update the entity
5. update the config manager in src
6. update the components
7. update the pipeline
8. Test tun the pipeline
9. run tox for testing package
10. update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline


*********************************************

STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/shiv0112/FSDS_NOV_deepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=shiv0112 \
MLFLOW_TRACKING_PASSWORD=<> \

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and mode