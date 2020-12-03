---
presentation:
  width: 1920
  height: 1080
  theme: solarized.css
---

<!-- slide -->

# simplelayout

## 4-simplelayout-pytest
## 作业讲评

<!-- slide -->

## 基本要求


本次作业已经包含了之前实现的 simplelayout 库（`src/simplelayout`），但该版本并不完全满足之前的全部需求，本次作业不需要修改这部分代码。
- 按 `TODO` 要求实现目录 `tests` 下的测试代码，包括
  - `test_core.py`
  - `test_utils.py`
  - `test_cli.py`
- 本地实验步骤
  - `pip install -e .` 以开发者模式安装 package
  - `pytest --cov-report=html --cov=src` 运行测试，并以网页方式保存代码覆盖结果
  - 打开网页 `htmlcov/index.html` 查看代码覆盖情况

<!-- slide -->

## `pytest`

- [pytest 官方文档](https://docs.pytest.org/en/stable/)
- [Getting Started](https://docs.pytest.org/en/stable/getting-started.html#getstarted)

- **Features**
  - Detailed info on failing assert statements (no need to remember self.assert* names)
  - Auto-discovery of test modules and functions
  - Modular fixtures for managing small or parametrized long-lived test resources
  - Can run unittest (including trial) and nose test suites out of the box
  - Rich plugin architecture, with over 315+ external plugins and thriving community
- 这次仅考察了基本的测试方法，强大的 `fixture` 等功能需要大家自己学习 
- [插件](https://docs.pytest.org/en/stable/plugins.html)，[pytest Plugins Compatibility](http://plugincompat.herokuapp.com/)

<!-- slide -->

## `coverage`

- 代码覆盖率，[coverage.py](https://coverage.readthedocs.io/)  
  > `Coverage.py` is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.
- 插件 `pytest-cov` 已经集成
- 可按要求生成不同类型的报告
  - 文本
  - 网页
  - 配合第三方平台比如 `codecov`
- 看个例子：[pytorch-lightning](https://github.com/PyTorchLightning/pytorch-lightning)


<!-- slide -->

## 结果/存在问题

- [结果展示](https://classroom.github.com/classrooms/63539802-idrl-assignment-classroom-python/assignments/4-simplelayout-pytest)
- 抽个同学讲一下
- 完成本次作业的代码其实在之前几次作业里都有，最好先自己实现
- 由于需要检测的 package 在 src 目录下，本地测试注意流程
- 考虑环境的不同，比如每个开发者的环境、开发人员与测试、用户之间的环境，引出了 devops 的重要性



