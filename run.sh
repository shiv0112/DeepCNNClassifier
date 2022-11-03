echo [$(date)]: "START"
python src/DeepCNNClassifier/pipeline/stage_01_ingestion.py
python src/DeepCNNClassifier/pipeline/stage_02_prepare_base_model.py
python src/DeepCNNClassifier/pipeline/stage_03_training.py
python src/DeepCNNClassifier/pipeline/stage_04_evaluation.py
dvc init -f
dvc repro
dvc dag
echo [$(date)]: "END"