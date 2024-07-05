from pathlib import Path
import os

project_name = 'textsummarizer'
files = [
    
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_transformation.py',
    f'src/{project_name}/components/model_building.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logger/__init__.py',
    f'src/{project_name}/exception/__init__.py',
    f'src/{project_name}/units_tests/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/predict_pipeline.py',
    f'src/{project_name}/pipeline/train_pipeline.py'
    
]

for file in files:
    path = Path(file)

    filedir, filename = os.path.split(path)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
    
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path,'w') as fileobj:
            pass



