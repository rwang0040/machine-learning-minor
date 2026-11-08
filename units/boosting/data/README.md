# B05 数据与固定设置

boosting-classification.csv 沿用 T09 的 160 行缺失分类数据，只用原 train 的 120 行作分层三折（shuffle=True、random_state=42）。每折 80 训练/40 验证，旧 validation40 行不评价。生成读取前单元 CSV，发放后自包含。

特征 planned_load_ratio、ambient_index 在开工前已知；over_limit 为完工后标签，编号与 split 不作输入。所有模型折内中位数填补；逻辑回归再作训练内标准化。主指标 accuracy 固定，同时记录 OOF 混淆计数；score_std 只描述折间波动。

LogisticRegression C=1/max_iter=1000；DecisionTree 深度 5/min_samples_leaf=2/seed42；RandomForest50 棵/深度 5/min_samples_leaf=2/max_features=1/bootstrap=True/seed42/n_jobs=1；GradientBoosting loss=log_loss/50 轮/learning_rate=0.1/max_depth=1/min_samples_leaf=2/seed42。其余沿用环境默认，不进行搜索或声称各模型最优。

持续项目复用 T08 已发布的 120 行开发数据，继续使用原项目目录的 development.csv。该任务不同于课堂超限预测，分数分别解释。B05 没有复制项目保留测试文件。基线只依训练标签多数类；项目主指标和划分沿用事先计划。
