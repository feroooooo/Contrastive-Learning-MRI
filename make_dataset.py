# import pandas as pd
# import os

# path = 'C:/Custom/DataSet/ADNI_预处理后/pheno_ADNI_longitudinal_new.csv'
# data_dir = 'C:/Custom/DataSet/ADNI_预处理后/Image'

# # 被试字典
# subject_dict = {}

# csv = pd.read_csv(path)

# total = 0
# flag = True
# for index, row in csv.iterrows():
#     # 排除多余数据
#     img_path = os.path.join(data_dir, f"brain_adni_{row['Subject'][-4:]}_{row['Image Data ID']}_fsld.nii.gz")
#     if not os.path.exists(img_path):
#         continue
    
#     total += 1
#     if row['Subject'] not in subject_dict:
#         subject_dict[row['Subject']] = {}
#         subject_dict[row['Subject']]['num'] = 0
#         subject_dict[row['Subject']]['group'] = row['Group']
#     else:
#         if subject_dict[row['Subject']]['group'] != row['Group']:
#             flag = False
#     subject_dict[row['Subject']]['num'] += 1

# # 同一被试的结果是否出现变化
# if flag:
#     print("no group change")
# else:
#     print("group change")

# print('subject num:', len(subject_dict))
# print('total num:', total)


import pandas as pd
from sklearn.model_selection import train_test_split
import os

# 加载数据
data_dir = 'C:/Custom/DataSet/ADNI_预处理后/Image'
data_path = 'C:/Custom/DataSet/ADNI_预处理后/pheno_ADNI_longitudinal_new.csv'
df = pd.read_csv(data_path)


list_for_del = []
for index, row in df.iterrows():
    img_path = os.path.join(data_dir, f"brain_adni_{row['Subject'][-4:]}_{row['Image Data ID']}_fsld.nii.gz")
    if not os.path.exists(img_path):
        list_for_del.append(row['Image Data ID'])
df = df[~df['Image Data ID'].isin(list_for_del)]

# 按照subject分组，确保同一个subject的所有图像保持在同一组中
groups = df.groupby('Subject')

# 初始化集合
train_subjects = []
val_subjects = []
test_subjects = []

# 按类别分组，为每个类别分配subject
for group_name, group_df in df.groupby('Group'):
    subjects = group_df['Subject'].unique()
    # 分割subject，确保验证集和测试集中至少有30%的subject
    train_subs, test_val_subs = train_test_split(subjects, test_size=0.3, random_state=42)
    val_subs, test_subs = train_test_split(test_val_subs, test_size=0.5, random_state=42)
    
    # 添加到各自的列表中
    train_subjects.extend(train_subs)
    val_subjects.extend(val_subs)
    test_subjects.extend(test_subs)

# 根据分配的subject生成最终的数据集
train_df = pd.concat([groups.get_group(sub) for sub in train_subjects])
val_df = pd.concat([groups.get_group(sub) for sub in val_subjects])
test_df = pd.concat([groups.get_group(sub) for sub in test_subjects])

# 保存或处理分割后的数据集
train_df.to_csv('C:/Custom/DataSet/ADNI_预处理后/train label.csv', index=False)
val_df.to_csv('C:/Custom/DataSet/ADNI_预处理后/validation label.csv', index=False)
test_df.to_csv('C:/Custom/DataSet/ADNI_预处理后/test label.csv', index=False)

print(f"Train set: {len(train_df)} images")
print(f"Validation set: {len(val_df)} images")
print(f"Test set: {len(test_df)} images")
