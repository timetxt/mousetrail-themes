# MouseTrail 主题库

*[English](README.md)*

一个面向 **MouseTrail**（macOS 鼠标轨迹应用）的公开渐变轨迹主题库。这里的每个主题都是
一个简单、可读的 JSON 文件，描述轨迹的颜色模式（`rainbow` 彩虹、`fixed` 固定色，或
2–5 个色标的 `gradient` 渐变）、持续时间和宽度——仅此而已。你可以浏览主题库网站一键
添加主题到应用，也可以下载 `.json` 文件自行导入。

## 如何使用主题

**方式一：主题库网站的"添加到 MouseTrail"（推荐）**

打开主题库网站（`docs/index.html`，通过 GitHub Pages 发布），点击任意主题卡片上的
**添加到 MouseTrail**。这会打开一个 `mousetrail://import?url=...` 深链接，将该主题的
原始 JSON 文件地址传给应用；应用会下载该文件、弹出确认对话框列出主题名称，只有在你
确认后才会导入——不会静默生效。

此功能需要支持渐变主题的 MouseTrail 版本。如果你使用的是较旧版本，导入包含
`gradient` 颜色模式的主题时会显示**"请更新 MouseTrail"**的提示，而不会静默失败或
错误导入——只使用 `rainbow`/`fixed` 颜色模式的主题在旧版本上仍可正常导入。

**方式二：下载后手动导入**

点击主题卡片上的**下载 .json**（或直接从 `themes/` 目录获取任意文件），然后在
MouseTrail 中依次打开**设置 → 轨迹 → 导入…**，选择该文件。此方式在所有 MouseTrail
版本上都可用——只是渐变主题在较旧版本上仍会显示"请更新 MouseTrail"的提示。

## 主题分类

| 分类 | 路径 | 说明 |
|---|---|---|
| **设计师精选**（旗舰） | `themes/official/designer/` | 精心策划的高级多色标渐变——追求柔和、统一的色彩叙事，而非随意的 RGB 取值。 |
| **霓虹** | `themes/official/neon/` | 明亮饱和的多色标渐变，包含应用内置的 **Aurora（极光流光）** 和 **Sunset（日落霞光）** 预设。 |
| **社区** | `themes/community/` | 通过 Pull Request 贡献，合并前由维护者审核。 |

## 手动编写主题文件

完整的文件格式说明——每个字段、取值范围及实例讲解（包括如何将十六进制颜色转换为本
格式使用的 `0`–`1` sRGB 数值）请见
**[THEME-FORMAT.zh-Hans.md](THEME-FORMAT.zh-Hans.md)**。

## 参与贡献

想为社区分类贡献自己的主题？请见 **[CONTRIBUTING.zh-Hans.md](CONTRIBUTING.zh-Hans.md)**，
了解如何编写、验证并通过 Pull Request 提交主题。

## 许可协议

本项目的主题与仓库内容采用 **[CC BY-NC 4.0](LICENSE)**（署名-非商业性使用）许可协议
发布——可自由使用与分享，附带署名，但不得用于商业用途。该许可协议仅适用于本仓库的
主题与内容，与 MouseTrail 应用本身的许可协议相互独立。
