# T14 纸笔活动

姓名________ 班级________ 日期________。

## A．反向计算

x=y=1，z=wx+b，h=ReLU(z)，s=vh+c，p=σ(s)。旧参数 w=v=1、b=c=0。给定 p≈0.731059，dL/ds=p−y。

1. 写出 z、h、s。
2. 依次求 dL/dv、dL/dc、dL/dh、dL/dz、dL/dw、dL/db。
3. 哪一步使用了 ReLU 的局部导数？

<!-- print:answer-lines=16 -->

<!-- print:pagebreak -->

## B．一次更新

η=0.1。写出四个新参数，再重新前向计算新 s。为什么不能先更新 v 再用新 v 计算 w 的本轮梯度？

<!-- print:answer-lines=16 -->

<!-- print:pagebreak -->

## C．批量与故障

1. n 个样本平均交叉熵，dS 应为 P−y 还是(P−y)/n？后面还要再除一次 n 吗？
2. 某次训练梯度非零、学习率 0、参数差 0，损失曲线水平。说明原因与本次修复。
3. 只有一条水平曲线、未检查配置和梯度，能唯一确定原因吗？

<!-- print:answer-lines=16 -->

<!-- print:pagebreak -->

## D．离堂

反向传播是否就是参数更新？训练损失下降是否证明验证改善？验证标签是否应该进入训练梯度？逐条判断并说明依据。

<!-- print:answer-lines=16 -->
