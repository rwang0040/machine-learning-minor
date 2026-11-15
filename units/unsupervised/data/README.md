# T12/B06 数据说明

preprocessing-classification.csv 与 T11 课堂 CSV 相同：160 行合成批次，planned_load_ratio 与 ambient_index 为开工前特征，over_limit 为分类目标。仅 120 行 train 作为开发数据，同一分层三折 shuffle=True/random_state=42，每折 80 训练/40 验证。旧 40 行 validation 不使用。

错误演示在这 120 行全部 fit 填补/标准化，再做三折；仅用于识别泄漏，不是可采纳的评估。正确分支按折 fit 完整 Pipeline。固定 KNN 的 K=5、等权、欧氏距离、brute，与 T11 一致。不改变数据来追求修复后分数下降。


PCA 投影片使用四个共线手工点(-2,-2)、(-1,-1)、(1,1)、(2,2)，只示意方向和一维投影，并非真实数据或一般无损降维保证。

综合项目沿用学生已有 development.csv，本目录不另存项目副本、不读取任何保留测试。
