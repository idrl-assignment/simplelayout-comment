---
presentation:
  width: 1920
  height: 1080
  theme: solarized.css
---

<!-- slide -->

# simplelayout

## 3-simplelayout-package

## 作业讲评

<!-- slide -->

## 基本要求

- 将个人完成的 `2-simplelayout-generator` 项目中的 `simplelayout` 目录复制到本次作业的 `src` 目录下。
- 编写 `setup.py`
  - 参考[官方文档](https://docs.python.org/3/distributing/index.html#reading-the-python-packaging-user-guide)，与 [Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/)，正确配置 `setuptools.setup()`，确保能被 `pip` 正确安装，要求
    - package 名称设置为 `simplelayout-github账号名`
    - 正确包含 `src/simplelayout` 这个 package
    - `install_requires` 包含 `simplelayout` 的相关依赖
    - 正确配置 `entry_points`，使命令 `simplelayout` 对应 `simplelayout/__main__.py` 中的 `main()` 函数
- 参考 [文档](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project)，正确打包
- 参考 [文档](https://packaging.python.org/guides/distributing-packages-using-setuptools/#id77)，正确上传到 PyPI
- 根据[参考教程](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)，创建 `docs` 目录，并创建 `Sphinx` 项目。
  - 在执行 `sphinx-quickstart` 时输入相关信息
  - Sphinx 默认使用 rst 格式（[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) ）编写文档，可进行配置使用 [Markdown](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#using-markdown-with-sphinx) 进行文档编写。
  - 选做：[参考](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) 配置 autodoc、napoleon 插件，自动生成 simplelayout 中的 docstring API。
  - 在本地生成正确的 Sphinx 文档
- 注册 [Read the Docs](https://readthedocs.org/)，将个人仓库中的文档正确托管
- 将个人项目 PyPI 仓库的链接、read the docs 链接以评论的方式发在 `Feedback` 上


<!-- slide -->


## `setup.py`

- [参考文档](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
- `setup.py` 两个主要作用：
  1. It’s the file where various aspects of your project are configured. The primary feature of `setup.py` is that it contains a global `setup()` function. The keyword arguments to this function are how specific details of your project are defined.
  2. It’s the command line interface for running various commands that relate to packaging tasks. To get a listing of available commands, run `python setup.py --help-commands`.
  - [`setup()` 参数](https://packaging.python.org/guides/distributing-packages-using-setuptools/#setup-args)
  - 注意 [version](https://packaging.python.org/guides/distributing-packages-using-setuptools/#version)，可以使用 [bunmp2version](https://pypi.org/project/bump2version/#description)、[zest.releaser](https://pypi.org/project/zest.releaser/)
  - [entry_points](https://packaging.python.org/guides/distributing-packages-using-setuptools/#entry-points)
  - [Working in “development mode”](https://packaging.python.org/guides/distributing-packages-using-setuptools/#working-in-development-mode)


<!-- slide -->


## `Packaging your project`

- [相关词汇表](https://packaging.python.org/glossary/#glossary)
- [Source distribution](https://packaging.python.org/guides/distributing-packages-using-setuptools/#source-distributions)
- [Wheels](https://packaging.python.org/guides/distributing-packages-using-setuptools/#wheels)
- [Uploading your Project to PyPI](https://packaging.python.org/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi)
  - 主意版本

<!-- slide -->

## `Sphinx`

- 使用脚本 `sphinx-quickstart`
- 配置 `conf.py`
  - 可配置**插件**、**主题**等等
- 默认使用 `rst`，可配置支持 `md`
- 文档也是要配合**版本控制**的

<!-- slide -->

## `Read the Docs`

- [官网](https://readthedocs.org/)，查看一下基本功能
- 示例，[requests](https://requests.readthedocs.io/en/master/)
- 跟 github 仓库绑定  


<!-- slide -->


## 结果/存在问题

- [结果展示](https://classroom.github.com/classrooms/63539802-idrl-assignment-classroom-python/assignments/3-simplelayout-package)
- 注意查看 Feedbacks
- version 的一致性
- 遵守规范能够方便使用 CI/CD 的工具，例如 github action


