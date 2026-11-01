# B04 课堂数据

tree-classification.csv 完整沿用 T07 的 160 行合成批次，输入、缺失位置、标签、编号与 split 均相同。建材脚本读取前单元 CSV 复制；发放后本单元可独立运行。

输入 planned_load_ratio 和 ambient_index 均在开工前取得；over_limit 为完工后标签，编号和 split 不进入模型。仅原 train 的 120 行参与三折，原 validation40 行不评价。每折 80 行拟合中位数填补与树、40 行验证；分层三折种子 42，shuffle=True。

树固定 criterion=gini、min_samples_leaf=2、random_state=42。候选深度按本人实验 Notebook 的要求提前确定，并说明理由。并列选择更浅者。score_std 仅描述折间波动，不作置信区间。

综合任务数据另放 project/development.csv，为新的模拟质量任务，不能与课堂分数直接比较；其保留数据仅在 teacher 目录，不发学生。
