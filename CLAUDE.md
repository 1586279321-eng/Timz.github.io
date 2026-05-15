# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 项目概述

基于 [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 主题的个人学术博客，部署在 GitHub Pages。

# 技术栈

- **静态站点生成器**: Jekyll（GitHub Pages 原生支持）
- **主题**: jekyll-theme-chirpy（gem 方式引入）
- **内容格式**: Markdown + YAML frontmatter
- **评论系统**: Utterances（基于 GitHub Issues）
- **数学公式**: MathJax
- **PWA**: 支持离线访问和安装

# 构建与预览命令

```bash
# 本地预览（不执行，仅建议）
bundle install
bundle exec jekyll serve --livereload

# 构建（GitHub Pages 在 push 后自动执行）
bundle exec jekyll build
```

# 目录结构

```
.
├── _config.yml              # Jekyll 配置（站点标题、URL、评论、分析等）
├── _posts/                  # 博客文章（YYYY-MM-DD-slug.md）
├── _tabs/                   # 侧边栏导航页面（about, categories, tags, archives）
├── _data/                   # 数据文件
│   ├── authors.yml          #   作者信息
│   ├── contact.yml          #   联系方式（侧边栏图标）
│   └── locales/             #   多语言文本（zh-CN.yml）
├── _layouts/                # 页面模板（default, post, page, home, archives 等）
├── _includes/               # 可复用 HTML 片段
├── _sass/                   # SCSS 样式源文件
├── _javascript/             # JS 源文件
├── assets/
│   ├── css/                 # 编译后的 CSS
│   ├── js/                  # 编译后的 JS
│   └── img/                 # 图片（头像 avatar.jpg、favicons）
└── index.html               # 首页入口
```

# 文章 Frontmatter 格式

```yaml
---
title: "文章标题"
author: timz
date: 2025-03-19
categories: [3D重建, NeRF]
tags: [NeRF, 体积渲染]
---
```

- `author`: 对应 `_data/authors.yml` 中的 key
- `categories`: 用方括号数组格式，支持层级分类
- `tags`: 标签数组

# 配置关键点

- `lang: zh-CN` 启用中文界面（由 `_data/locales/zh-CN.yml` 定义全部 UI 文本）
- `timezone: Asia/Shanghai`
- 文章路径格式：`/posts/:title/`（在 `defaults` 中定义，不要修改）
- 导航页面在 `_tabs/` 目录，通过 `order` 字段排序
- 暗色模式侧边栏底部有切换按钮，也可在 `_config.yml` 的 `theme_mode` 强制指定

# 注意事项

- GitHub Pages 只支持白名单内的 Jekyll 插件，Chirpy 已处理此限制
- Utterances 需在 GitHub 仓库 `Timz/Timz.github.io` 安装 Utterances App
- 头像放在 `assets/img/avatar.jpg`，favicon 在 `assets/img/favicons/`
- 文章图片建议走图床外链，本地图片放 `assets/img/` 下，引用路径用 `/assets/img/xxx.png`
- `jekyll-theme-chirpy-master/` 是原始下载的模板目录，已在 `exclude` 中排除，构建时会被忽略
