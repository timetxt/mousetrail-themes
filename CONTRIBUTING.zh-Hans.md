# 贡献主题

*[English](CONTRIBUTING.md)*

感谢你愿意为社区分类贡献主题。这是一个简单、机械化的流程：编写主题文件、在本地
验证、提交 Pull Request。

## 1. 编写主题文件

在 `themes/community/<kebab-case-名称>.json` 新建文件，例如
`themes/community/midnight-teal.json`。名称应具有描述性，且不与现有主题冲突（文件内
的 `name` 字段——主题名称——必须在整个仓库范围内唯一，而不仅仅是你的文件内唯一）。

请遵循 **[THEME-FORMAT.zh-Hans.md](THEME-FORMAT.zh-Hans.md)** 中的确切 JSON
格式：文件结构（`version`、`themes`）、每个主题的 `name` 与 `style`，以及三种
`colorMode` 形式（`rainbow`、`fixed`、`gradient`）。`gradient` 主题需要 2–5 个色标，
并使用 `version: 2`；仅使用 `rainbow`/`fixed` 的文件使用 `version: 1`。

一个最小示例：

```json
{
  "version": 2,
  "themes": [
    {
      "name": "Midnight Teal",
      "style": {
        "colorMode": {
          "gradient": {
            "stops": [
              { "red": 0.02, "green": 0.11, "blue": 0.16, "alpha": 1, "location": 0 },
              { "red": 0.04, "green": 0.36, "blue": 0.42, "alpha": 1, "location": 0.5 },
              { "red": 0.30, "green": 0.80, "blue": 0.76, "alpha": 1, "location": 1 }
            ]
          }
        },
        "lifetime": 0.6,
        "widthScale": 1.0
      }
    }
  ]
}
```

## 2. 本地验证

在提交 PR 前运行仓库自带的纯 stdlib 验证器——无需安装任何依赖：

```
python3 scripts/validate_themes.py
```

该脚本会检查 JSON 有效性、必填字段、取值范围、色标数量、`version` 与内容是否一致，
以及主题名称在全仓库范围内是否唯一。如果有问题，脚本会以非零状态退出并列出每一条
违规项，请先修复。

## 3. 提交 Pull Request

针对本仓库提交一个仅包含 `themes/community/` 下新文件的 PR。`validate-themes` 这个
GitHub Actions 工作流会在你的 PR 上自动运行相同的验证器，并额外做一次 JSON Schema
校验——它**只是一个辅助工具**：不会自动合并任何内容，检查通过也不代表一定会被接受。
**合并由维护者人工审核决定。**

PR 模板中有一个简短的检查清单，请填写；它与上述步骤一一对应。

## 许可协议

提交主题即表示你同意将你的贡献以与本仓库其余内容相同的
**[CC BY-NC 4.0](LICENSE)** 协议进行许可。
