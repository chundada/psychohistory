# Install Psychohistory skills to Claude/Cursor directory
# Run: PowerShell -ExecutionPolicy Bypass .\_install_skills.ps1

$sourceDir = "C:\Users\周春宇\Desktop\Psychohistory\series\game-theory\skills"
$targetDir = "$env:USERPROFILE\.claude\skills\Psychohistory"

Write-Host "Installing Psychohistory skills..."
Write-Host "Source: $sourceDir"
Write-Host "Target: $targetDir`n"

# Create target directory
New-Item -ItemType Directory -Path $targetDir -Force | Out-Null

# Copy all skill files
$files = Get-ChildItem -Path $sourceDir -Filter "*.md"
$count = 0
foreach ($f in $files) {
    Copy-Item $f.FullName "$targetDir\$($f.Name)" -Force
    $count++
}

Write-Host "Installed $count skills to $targetDir"
Write-Host "`nYour AI assistant (Claude Code / Cursor) can now call these skills."
