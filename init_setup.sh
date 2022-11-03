echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activating the environment"
source activate ./env
echo [$(date)]: "Installing the dev env"
pip install -r requirements_dev.txt
echo [$(date)]: "Installing predictions"
pip install -r prediction_service/requirements_dev.txt
source activate ./env
echo [$(date)]: "END"