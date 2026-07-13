# Install Psychohistory — full system
# Run: PowerShell -ExecutionPolicy Bypass .\_install_skills.ps1

$projectRoot = "C:\Users\周春宇\Desktop\Psychohistory"

Write-Host "🧠 Psychohistory — Full System Install" -ForegroundColor Cyan
Write-Host "======================================`n" -ForegroundColor Cyan

# ─── 1. Install skills to Claude Code global directory ───
$claudeSkillDir = "$env:USERPROFILE\.claude\skills\Psychohistory"
Write-Host "[1/4] Installing skills to Claude Code..." -ForegroundColor Yellow
New-Item -ItemType Directory -Path $claudeSkillDir -Force | Out-Null
$files = Get-ChildItem -Path "$projectRoot\skills" -Filter "*.md"
$count = 0
foreach ($f in $files) {
    Copy-Item $f.FullName "$claudeSkillDir\$($f.Name)" -Force
    $count++
}
Write-Host "      ✓ $count skills → $claudeSkillDir" -ForegroundColor Green

# ─── 2. Install system prompt ───
$systemPromptDest = "$claudeSkillDir\PSYCHOHISTORY_SYSTEM_PROMPT.md"
Copy-Item "$projectRoot\PSYCHOHISTORY_SYSTEM_PROMPT.md" $systemPromptDest -Force
Write-Host "[2/4] ✓ System prompt → $systemPromptDest" -ForegroundColor Green

# ─── 3. Install rules for Claude Code (project-level) ───
$claudeRulesDir = "$projectRoot\.claude\rules"
if (Test-Path "$claudeRulesDir\psychohistory-activation.mdc") {
    Write-Host "[3/4] ✓ Claude Code rules already in project" -ForegroundColor Green
}

# ─── 4. Install rules for Cursor (project-level) ───
$cursorRulesDir = "$projectRoot\.cursor\rules"
if (Test-Path "$cursorRulesDir\psychohistory.mdc") {
    Write-Host "[4/4] ✓ Cursor rules already in project" -ForegroundColor Green
}

Write-Host "`n====================================== ✅" -ForegroundColor Cyan
Write-Host "Install complete!" -ForegroundColor Cyan
Write-Host "`n📖 HOW TO USE" -ForegroundColor White
Write-Host "─────────────" -ForegroundColor Gray
Write-Host ""
Write-Host "Option A: Claude Code (in project directory)" -ForegroundColor Yellow
Write-Host "  cd Psychohistory"
Write-Host "  → The .claude/rules/ and CLAUDE.md files"
Write-Host "    auto-activate Psychohistory persona"
Write-Host ""
Write-Host "Option B: Claude Code (ANY project)" -ForegroundColor Yellow
Write-Host "  Skills installed to ~/.claude/skills/Psychohistory/"
Write-Host "  → @Psychohistory 可调: /skill Psychohistory"
Write-Host ""
Write-Host "Option C: Any AI (Claude.ai / ChatGPT / etc.)" -ForegroundColor Yellow
Write-Host "  Copy PSYCHOHISTORY_SYSTEM_PROMPT.md content as system prompt"
Write-Host "  → Full person activation"
Write-Host ""
Write-Host "Option D: Cursor" -ForegroundColor Yellow
Write-Host "  .cursor/rules/psychohistory.mdc auto-activates"
Write-Host ""
Write-Host "💡 After install, ask your AI:" -ForegroundColor Magenta
Write-Host '  "用 Psychohistory 体系分析当前的中美关系"' -ForegroundColor Magenta
Write-Host '  "从多重框架视角预测俄乌战争下一步"' -ForegroundColor Magenta
Write-Host '  "我想用 Psychohistory 分析这个问题，帮我选择最相关的技能"' -ForegroundColor Magenta
