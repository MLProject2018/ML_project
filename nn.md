# 机器学习Project调参记录

### nodecay

- 使用lr为1e-3， 在100个epoch达到最优，之后loss上升
- acc 0.8, loss 0.65 

### decay

- 初始lr为1e-3，每10个epoch 学习率 decay 0.9， 110个epoch达到最优，之后loss上升
- acc 0.822, loss 0.584

### decay_nothread

- 不考虑线程数，<u>效果下降</u>
- acc 0.79 loss 0.65

### decay_withlinesnum

- 考虑代码行数，有一定效果，但不明显
- acc 0.826， loss 0.59

### decay_withlinesnum_1_1

- 将linesnum和threadnum归一化到-1,1之间，没有效果
