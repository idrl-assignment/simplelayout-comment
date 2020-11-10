---
presentation:
  width: 1920
  height: 1080
  theme: solarized.css
---

<!-- slide -->

# simplelayout

## 1-simplelayout-CLI

## 作业讲评

<!-- slide -->

## 要求

- 实现一个简单的命令行接口
```bash
python simplelayout.py --board_grid 100 --unit_grid 10 --unit_n 3 --positions 1 15 33 --outdir dir1/dir2 --file_name example
```
- 需要大家掌握 `argparse` 的基本用法
- 基本类型参数类型判断、逻辑判断
- 当参数不符合要求时退出

<!-- slide -->

## `argparse`

- 进阶用法
  - 说明文档
  - 版本
  - 子命令
  - 配置文件
- git 命令就是一个完整的命令行接口

<!-- slide -->



## 结果/存在问题

- [结果展示](https://classroom.github.com/classrooms/63539802-idrl-assignment-classroom-python/assignments/1-simplelayout-cli)
- 注意功能逻辑
  - 当目录不存在时创建目录
  - 不管目录存不存在都应按要求生成所需文件

