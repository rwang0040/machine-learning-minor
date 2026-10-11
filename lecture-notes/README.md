# 机器学习辅修：学生讲义阅读入口

讲义是本课程的核心学习资料，与课堂投影片、纸笔活动和实验配合使用。请按章节顺序阅读；课前熟悉任务与例子，课后独立完成自查，再对照解析。自查用于学习反馈，不增加必交报告。

| 章节 | 讲义 | 课堂材料 | 实验衔接 |
|---|---|---|---|
| T01 任务、数据与基线 | [PDF，10 页](pdf/minor-48/t01.pdf) | [投影片](../lecture/t01/index.html) · [纸笔活动 PDF，4 页](../units/task-data-baseline/worksheets/student.pdf) · [文字版](../units/task-data-baseline/worksheets/student.md) | 输入整理在 B01 中提供支持 |
| T02 划分与基本评价 | [PDF，13 页](pdf/minor-48/t02.pdf) | [投影片](../lecture/t02/index.html) · [纸笔活动 PDF，4 页](../units/split-evaluation/worksheets/student.pdf) · [文字版](../units/split-evaluation/worksheets/student.md) | T02 后完成 [B01 辅修练习](../units/split-evaluation/labs/B01-minor.ipynb) |
| T03 线性模型与平方损失 | [PDF，8 页](pdf/minor-48/t03.pdf) | [投影片](../lecture/t03/index.html) · [纸笔活动 PDF，4 页](../units/linear-regression/worksheets/student.pdf) · [文字版](../units/linear-regression/worksheets/student.md) | 用纸笔核对参数、预测与损失 |
| T04 梯度下降、学习率与尺度 | [PDF，11 页](pdf/minor-48/t04.pdf) | [投影片](../lecture/t04/index.html) · 上述纸笔活动的 T04 部分 | T04 后完成 [B02 练习](../units/linear-regression/labs/B02-minor.ipynb) |

实验遇到划分、训练、预测或指标函数问题时，回看 T02 第 8 节；B02 的梯度、更新和结果核对回看 T04 第 8 节。完成 TODO 后删除该处停止提示，保留检查代码；重启内核并运行全部，保存自己的 Notebook。B01 和 B02 只有训练集和验证集，结果不能称为独立最终测试表现。

请保留课程文件的相对目录结构，不单独移动 PDF 或 Notebook。投影片通过课程 HTTP 预览入口打开；T02—T04 交互演示首次加载需要联网，运行不成时可以使用页面的静态算例。后续讲义会随授课进度补充到此入口。

## 课后作业

T02 学习后完成 [作业一：从任务定义到可信评价](../homework/t01-t02/student.md)，预计 60 分钟，可查阅讲义及使用计算器。无需先完成 B01，不要求编程；按题号提交一份答案，具体时间和渠道以教师发布为准。

T04 学习后完成 [作业二：从模型参数到可信的更新结果](../homework/t03-t04/student.md)，预计 60 分钟，可查阅讲义及使用计算器。无需先完成 B02，代码题只需阅读和写出最小修正，不要求运行；按题号提交一份答案，具体时间和渠道以教师发布为准。
