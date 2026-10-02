param()
$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$manifest = Get-Content -LiteralPath (Join-Path $repositoryRoot 'plugin.json') -Raw -Encoding utf8 | ConvertFrom-Json
if ($manifest.version -notmatch '^\d+\.\d+\.\d+$') {
    throw 'La versión debe tener el formato mayor.menor.parche.'
}
$pendingChanges = git -C $repositoryRoot status --porcelain --untracked-files=all
if ($LASTEXITCODE -ne 0 -or $pendingChanges) {
    throw 'Confirma los cambios del repositorio antes de generar el paquete.'
}
$outputDirectory = Join-Path $repositoryRoot 'dist'
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null
$archiveName = "gorvet-creative-suite-$($manifest.version).zip"
$archivePath = Join-Path $outputDirectory $archiveName
if (Test-Path -LiteralPath $archivePath) {
    throw "El paquete $archiveName ya existe. Revisa el archivo o usa una versión nueva."
}
git -C $repositoryRoot archive --format=zip "--output=$archivePath" HEAD -- plugin.json README.md LICENSE skills
if ($LASTEXITCODE -ne 0) {
    throw 'No se pudo generar el paquete desde el commit actual.'
}
$hash = (Get-FileHash -LiteralPath $archivePath -Algorithm SHA256).Hash.ToLowerInvariant()
"$hash  $archiveName" | Set-Content -LiteralPath (Join-Path $outputDirectory 'SHA256SUMS.txt') -Encoding ascii
Write-Output $archivePath
