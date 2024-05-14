import pandas as pd
from rdkit import Chem

# CSV 파일 로드
file_path = 'demo_smiles.csv'  # 파일 경로를 여기에 입력하세요
data = pd.read_csv(file_path)

# 유효한 SMILES 문자열 개수 계산
valid_count = 0
for smiles in data['smiles']:
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        valid_count += 1

# 결과 출력
print(f"유효한 SMILES 문자열의 개수: {valid_count}")
