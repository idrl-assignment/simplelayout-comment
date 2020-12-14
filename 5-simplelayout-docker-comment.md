---
presentation:
  width: 1920
  height: 1080
  theme: solarized.css
---

<!-- slide -->

# simplelayout

## 5-simplelayout-docker
## 作业讲评

<!-- slide -->

## 基本要求

- 将 `3-simplelayout-package` 作业中完成的 `src` 目录、`setup.py` 复制到本次作业的目录下
- 相关依赖填写 `requirements.txt`
- 注册 [dockerhub](https://hub.docker.com/)，并将用户名填入 `username.py` 中
- 编写 `Dockerfile`
- 构建 docker 镜像
  - 若本机已经安装 `docker`，可以本地 build
  - 若没有安装，可以使用 [play with docker](https://labs.play-with-docker.com/)，相当于一个有网络支持的虚拟环境，把自己的代码 clone 下来，再 build
  - 镜像名称为 `dockerhub 用户名/simplelayout`


<!-- slide -->

## `DevOps`

- DevOps 一词的来自于 Development 和 Operations 的组合，突出重视软件开发人员和运维人员的沟通合作，通过自动化流程来使得软件构建、测试、发布更加快捷、频繁和可靠。
- 三个部分：开发、测试和运维
- git、pytest、docker、github action 都是重要组成部分



<!-- slide -->


## `docker`

- 多人协作时经常出现的痛点
  - 开发、测试时用到的库版本不一致
  - 开发、测试时基础环境不一致
  - 新人加入环境要从新配置
  - 希望交付一个开箱即用的应用
  
- [官网](https://www.docker.com/why-docker)
- 简单理解 docker 就是一种轻量化的虚拟机
  - image: 镜像，container: 容器
  - 需要掌握基本概念，掌握基本 docker CLI
- [docker hub](https://www.docker.com/products/docker-hub): 官方镜像仓库
  - 国内网速原因可以配置源，比如阿里、Azure中国、中科大等等
  - 国内云服务商也有仓库服务
  - 实验室内部的 harbor 就是搭建的私有仓库

<!-- slide -->

## `Dockerfile`

- 通过一条条指令构建镜像，按层（layer）构建
- 已有的层会复用
- [官方文档](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- 选用合适的基础镜像
- 可以和代码一同发布出去

<!-- slide -->


## 构建 `python` 应用

- 推荐使用 `dockerhub` [官方python基础镜像](https://hub.docker.com/_/python)
- 选用适合自己应用的基础镜像 tag
- 可配合 CI/CD 比如 github action，举例 [layout-generagor](https://github.com/zweien/layout-generator)


<!-- slide -->

## 结果/存在问题

- [结果展示](https://classroom.github.com/classrooms/63539802-idrl-assignment-classroom-python/assignments/5-simplelayout-docker)
- 抽个同学讲一下
- docker push 之前先 login
- Dockerfile 

