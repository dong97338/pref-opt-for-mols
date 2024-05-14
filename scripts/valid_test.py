from rdkit import Chem

# smiles = "CC1COC(=O)C2(C)C3=CC=C(C1)C2=C3"  # 에탄올
smiles = "c12c3c4c5c1c1c6c7c2c2c8c3c3c9c4c4c%10c5c5c1c1c6c6c%11c7c2c2c7c8c3c3c8c9c4c4c9c%10c5c5c1c1c6c6c%11c2c2c7c3c3c8c4c4c9c5c1c1c6c2c3c41"  # 풀러렌

mol = Chem.MolFromSmiles(smiles)

# 분자의 원자 정보 출력
for atom in mol.GetAtoms():
    print(f"원자: {atom.GetSymbol()}, 원자 번호: {atom.GetAtomicNum()}")

# 분자의 결합 정보 출력
for bond in mol.GetBonds():
    print(f"결합: {bond.GetBondType()} between {bond.GetBeginAtomIdx()} and {bond.GetEndAtomIdx()}")
