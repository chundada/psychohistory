#Requires -Version 5.1
<#
.SYNOPSIS
    Psychohistory 技能库安装脚本（重写版）
.DESCRIPTION
    将 skills/ 下的技能文件安装为 Claude Code 可识别的技能目录结构：
    每个 skills/<基名>.md → <TargetDir>\psychohistory-<基名>\SKILL.md
    （Claude Code 技能必须是独立目录 + SKILL.md，平铺拷贝不会被识别）
    另将系统提示等参考文档拷贝到 <TargetDir>\psychohistory-docs\ 备用。
.PARAMETER TargetDir
    安装目标目录，默认 $HOME\.claude\skills；测试时可指向临时目录。
.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\_install_skills.ps1
.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\_install_skills.ps1 -TargetDir C:\tmp\ph-test
#>
[CmdletBinding()]
param(
    [string]$TargetDir = (Join-Path $HOME '.claude\skills')
)

$ErrorActionPreference = 'Stop'
$projectRoot = $PSScriptRoot

# 控制台中文输出兼容（Windows PowerShell 5.1 默认 GBK 控制台）
try { [Console]::OutputEncoding = [Text.Encoding]::UTF8 } catch {}

Write-Host "🧠 Psychohistory 技能库安装" -ForegroundColor Cyan
Write-Host "======================================"
Write-Host "目标目录: $TargetDir`n"

# ─── 1. 每个技能文件 → 独立目录 + SKILL.md ───
$skillsSrc = Join-Path $projectRoot 'skills'
$skillFiles = @(Get-ChildItem -Path $skillsSrc -Filter '*.md' -File | Sort-Object Name)
if ($skillFiles.Count -eq 0) {
    Write-Error "未在 $skillsSrc 找到任何 .md 技能文件，安装中止。"
}

$installed = 0
foreach ($f in $skillFiles) {
    $baseName = [IO.Path]::GetFileNameWithoutExtension($f.Name)
    $skillDir = Join-Path $TargetDir "psychohistory-$baseName"
    New-Item -ItemType Directory -Path $skillDir -Force | Out-Null
    # 字节级复制：完整保留原文件内容与 frontmatter（name/description），不改变编码
    Copy-Item -LiteralPath $f.FullName -Destination (Join-Path $skillDir 'SKILL.md') -Force
    $installed++
}
Write-Host "[1/2] ✓ 已安装 $installed 个技能 → $TargetDir\psychohistory-*\SKILL.md" -ForegroundColor Green

# ─── 2. 参考文档 → psychohistory-docs（备用，不作为技能）───
$docsDir = Join-Path $TargetDir 'psychohistory-docs'
New-Item -ItemType Directory -Path $docsDir -Force | Out-Null
$docNames = @('PSYCHOHISTORY_SYSTEM_PROMPT.md', 'PSYCHOHISTORY_LITE.md', 'QUICK_START.md')
$docCopied = 0
foreach ($d in $docNames) {
    $src = Join-Path $projectRoot $d
    if (Test-Path -LiteralPath $src) {
        Copy-Item -LiteralPath $src -Destination (Join-Path $docsDir $d) -Force
        $docCopied++
    } else {
        Write-Host "      ⚠ 跳过（源文件不存在）: $d" -ForegroundColor DarkYellow
    }
}
Write-Host "[2/2] ✓ 已拷贝 $docCopied 个参考文档 → $docsDir" -ForegroundColor Green

# ─── 验证：随机抽查 3 个技能目录，确认 SKILL.md 存在且非空 ───
Write-Host "`n验证抽查:" -ForegroundColor Yellow
$sampleCount = [Math]::Min(3, $skillFiles.Count)
$sample = $skillFiles | Get-Random -Count $sampleCount
$verifyOk = $true
foreach ($f in $sample) {
    $baseName = [IO.Path]::GetFileNameWithoutExtension($f.Name)
    $p = Join-Path $TargetDir "psychohistory-$baseName\SKILL.md"
    if ((Test-Path -LiteralPath $p) -and ((Get-Item -LiteralPath $p).Length -gt 0)) {
        Write-Host "  ✓ psychohistory-$baseName\SKILL.md 存在且非空" -ForegroundColor Green
    } else {
        Write-Host "  ✗ psychohistory-$baseName\SKILL.md 缺失或为空" -ForegroundColor Red
        $verifyOk = $false
    }
}

# ─── 统计 ───
$actualDirs = @(Get-ChildItem -Path $TargetDir -Directory -Filter 'psychohistory-*' |
    Where-Object { $_.Name -ne 'psychohistory-docs' }).Count
Write-Host "`n======================================"
Write-Host "安装统计: 技能 $installed 个 / 技能目录 $actualDirs 个 / 参考文档 $docCopied 个" -ForegroundColor Cyan
if ($verifyOk -and $actualDirs -eq $installed) {
    Write-Host "✅ 安装完成，验证通过" -ForegroundColor Green
} else {
    Write-Host "⚠ 安装完成但验证异常，请检查上方输出" -ForegroundColor Red
    exit 1
}

Write-Host "`n📖 使用方式" -ForegroundColor White
Write-Host "─────────────" -ForegroundColor Gray
Write-Host "  Claude Code（任意项目）: 技能已安装到 $TargetDir"
Write-Host "  系统提示备用文档: $docsDir"
Write-Host '  示例提问: "用 Psychohistory 体系分析当前的中美关系"' -ForegroundColor Magenta
