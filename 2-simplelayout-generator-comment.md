---
presentation:
  width: 1920
  height: 1080
  theme: solarized.css
---

<!-- slide -->

# simplelayout

## 2-simplelayout-generator

## 作业讲评

<!-- slide -->

## 要求

- 本次作业将实现生成器的数据生成部分，也就是 1-simplelayout-cli 中的主要逻辑部分。同时考察 package、module 的相关知识。
- 目录结构为 
  ```
  simplelayout
  │  ├─cli
  │  │  └─__init__.py
  │  │  └─cli_generate.py
  │  ├─generator
  │  │  └─__init__.py
  │  │  └─core.py
  │  │  └─utils.py
  │  └─__init__.py
  │  └─__main__.py
  ```
- 按照 `TODO ` 提示完成相应功能点
  1. `/simplelayout/cli/cli_generate.py`
  2. `/simplelayout/cli/__init__.py`
  3. `/simplelayout/generator/core.py`
  4. `/simplelayout/generator/utils.py`
  5. `/simplelayout/__main__.py`
<!-- slide -->


## 目录结构

- [推荐阅读](https://dabeaz-course.github.io/practical-python/Notes/09_Packages/01_Packages.html)
- 目录结构为 
  ```
  simplelayout
  │  ├─cli
  │  │  └─__init__.py
  │  │  └─cli_generate.py
  │  ├─generator
  │  │  └─__init__.py
  │  │  └─core.py
  │  │  └─utils.py
  │  └─__init__.py
  │  └─__main__.py
  ```
- `__init__.py`
- `__main__.py`
  - `python -m simplelayout ...`
- 以 `PyTorch` 作为例子
<!-- slide -->


## 主体逻辑

- 在矩阵指定的位置上填上信息
- 不限实现算法
- 基本测试
  ```python
  def test_generate_matrix():
      matrix = generate_matrix(4, 2, 3, [1, 2, 4])
      matrix_true = [
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 1, 1],
          [0, 0, 1, 1],
      ]
      assert np.array_equal(matrix, matrix_true)
  ```
- 抽个同学讲下思路

<!-- slide -->



## 结果/存在问题

- [结果展示](https://classroom.github.com/classrooms/63539802-idrl-assignment-classroom-python/assignments/2-simplelayout-generator)
- 有些同学在 Feedback 中没有正确生成图片，说明 comment 那个 action 没有通过
- 注意要求
  ```python
  from simplelayout.cli import get_options  # TODO: 保证不修改本行也可以正确导入
  ```
  本意是希望对 `simplelayout/cli/__init__.py` 进行修改，使上面正确导入
- `requirements.txt` 中不要添加 Python 自带的标准库
- **变量名称**最好跟语义相符
- 推荐 `pathlib` ( 原因？)

