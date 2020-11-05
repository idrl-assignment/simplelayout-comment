---
presentation:
  width: 1920
  height: 1080
  theme: solarized.css
---

<!-- slide -->

# simplelayout
## 0-warm-up

## 作业讲评

<!-- slide -->

## 要求

- 符合 PEP 8 代码规范
- 将所需第三方 package 放到 `requirements.txt` 中
- 编写 `plot_matrix.py` 中 `TODO` 部分，使程序满足以下功能：
  1. `generate_matrix(m, n)` 生成 m 行 n 列的二值**随机矩阵**（每个元素随机为 0 或 1）
  2. `save_matrix(matrix, file_name)` 将 `matirx` 保存成图片形式
- 通过单元测试，系统会赋予相应分值；可本地执行 `pytest` 查看测试结果
- 个人作业仓库在每次 push 后会执行自动评分，并自动生成带反馈结果的 pull request，其中包含生成的图片结果（待执行结束后）

<!-- slide -->


## git 的使用

- git 的基础知识还是要靠大家自行学习
- 基本作业流程
  1. clone 自己的仓库 
  2. cd 进去，或者用 IDE 打开
  3. 根据作业的 `README.md` 要求编写代码
  4. 本地测试
  5. commit、push 到 github
  6. github 将自动运行测试，进入自己的相应的仓库，查看 Pull request 里的测试结果
  7. 若项目仓库里没有自动生成 pull request，可以手动创建，将 base 选为 feedback 分支
- 注意
  - 不要添加跟项目无关的文件、或者是本地 IDE 的辅助文件，可以将他们添加到 `.gitignore` 中
  - `commit` 可以添加便于理解的信息
<!-- slide -->

## 代码规范

- [PEP 8: Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- 本次任务采用 [flake8](https://flake8.pycqa.org/): 代码样式、质量检测
- IDE 可以帮助静态检测，看到提示要注意修改
- 例如下列**存在问题**的代码
    ```python
    import matplotlib.pyplot as plt
    import numpy as np
    import os

    def generate_random_matrix(m, n):
        matrix= np.random.randint(0, 2, size=(m, n));
        return matrix
    ```
- 推荐使用 [black](https://github.com/psf/black) 对代码自动格式化（black 是 PEP8 的严格子集）

<!-- slide vertical=true -->

## Black

- **Black** is the **uncompromising** Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.
- **Blackened code looks the same regardless of the project you're reading.** Formatting becomes transparent after a while and you can focus on the content instead.
- Black makes code review faster by producing the smallest diffs possible.

- 实操举例

<!-- slide -->

## `requirements.txt`

- requirements.txt 供测试环境的 pip 进行安装，在评分系统中会先运行
    ```
    pip install -r requirements.txt
    ```
- requirements.txt 提供了项目所需**第三方**依赖，官方的[标准库](https://docs.python.org/3/library/index.html)无需添加
- requirements.txt 里每一行为一个 package 的名称，可以对版本加以限制，[参考](https://packaging.python.org/tutorials/installing-packages/#installing-packages)


<!-- slide -->

## `generate_matrix(m, n)`

- generate_matrix(m, n) 生成 m 行 n 列的二值随机矩阵（每个元素随机为 0 或 1）
- 可使用 `numpy.random` 的 `randint()`、`choice()` 等
- 测试程序会判断尺寸、随机性、元素值

<!-- slide -->

## `save_matrix(matrix, file_name) `

- `save_matrix(matrix, file_name)` 将 `matirx` 保存成图片形式
- 推荐使用 matplotlib 作图，由于只供结果展示，可以使用 `imshow`、`matshow` 等函数
- 注意参数 `file_name` 为文件路径字符串

<!-- slide -->

## 结果/存在问题

- [结果展示](https://classroom.github.com/classrooms/63539802-idrl-assignment-classroom-python/assignments/0-warm-up?sort_by=Created+at)
- 大家基本都完成了功能点，熟悉了作业流程
- 不要修改测试程序，实现相应功能即可
- 我会对在大家仓库内的 pull request 里进行 code review，提出建议
- 遇到问题大家可以在[讨论组](https://www.yuque.com/idrl/topics)进行讨论，不要害怕提问

