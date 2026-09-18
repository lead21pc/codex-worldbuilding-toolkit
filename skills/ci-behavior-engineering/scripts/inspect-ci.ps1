[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Path,

    [string]$ComparePath,

    [int]$MaxChars = 0,

    [int]$MaxBytes = 0,

    [ValidateSet('Any', 'CRLF', 'LF')]
    [string]$ExpectedLineEnding = 'Any',

    [int[]]$ExpectedDiffLine,

    [switch]$RequireFinalNewline,

    [switch]$ForbidBom,

    [switch]$ForbidTrailingWhitespace
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Read-CiFile {
    param([Parameter(Mandatory = $true)][string]$LiteralPath)

    $resolved = (Resolve-Path -LiteralPath $LiteralPath).Path
    $bytes = [System.IO.File]::ReadAllBytes($resolved)
    $utf8 = New-Object System.Text.UTF8Encoding($false, $true)
    $text = $utf8.GetString($bytes)
    $hasBom = $bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF

    [PSCustomObject]@{
        Path = $resolved
        Bytes = $bytes.Length
        Chars = $text.Length
        Hash = (Get-FileHash -Algorithm SHA256 -LiteralPath $resolved).Hash
        Text = $text
        Lines = [System.IO.File]::ReadAllLines($resolved)
        HasBom = $hasBom
        Crlf = [regex]::Matches($text, "`r`n").Count
        BareLf = [regex]::Matches($text, '(?<!\r)\n').Count
        BareCr = [regex]::Matches($text, '\r(?!\n)').Count
        FinalNewline = $text.EndsWith("`r`n") -or $text.EndsWith("`n") -or $text.EndsWith("`r")
        TrailingWhitespace = [regex]::Matches($text, '[ \t]+(?=\r?$)', [System.Text.RegularExpressions.RegexOptions]::Multiline).Count
    }
}

$failures = New-Object System.Collections.Generic.List[string]
$item = Read-CiFile -LiteralPath $Path

if ($MaxChars -gt 0 -and $item.Chars -gt $MaxChars) {
    $failures.Add("chars $($item.Chars) exceed $MaxChars")
}
if ($MaxBytes -gt 0 -and $item.Bytes -gt $MaxBytes) {
    $failures.Add("bytes $($item.Bytes) exceed $MaxBytes")
}
if ($ExpectedLineEnding -eq 'CRLF' -and ($item.BareLf -gt 0 -or $item.BareCr -gt 0)) {
    $failures.Add('line endings are not CRLF-only')
}
if ($ExpectedLineEnding -eq 'LF' -and ($item.Crlf -gt 0 -or $item.BareCr -gt 0)) {
    $failures.Add('line endings are not LF-only')
}
if ($RequireFinalNewline -and -not $item.FinalNewline) {
    $failures.Add('final newline is missing')
}
if ($ForbidBom -and $item.HasBom) {
    $failures.Add('UTF-8 BOM is present')
}
if ($ForbidTrailingWhitespace -and $item.TrailingWhitespace -gt 0) {
    $failures.Add("trailing whitespace count is $($item.TrailingWhitespace)")
}

Write-Output "PATH=$($item.Path)"
Write-Output "CHARS=$($item.Chars)"
Write-Output "BYTES=$($item.Bytes)"
Write-Output "SHA256=$($item.Hash)"
Write-Output "BOM=$($item.HasBom)"
Write-Output "CRLF=$($item.Crlf)"
Write-Output "BARE_LF=$($item.BareLf)"
Write-Output "BARE_CR=$($item.BareCr)"
Write-Output "FINAL_NEWLINE=$($item.FinalNewline)"
Write-Output "TRAILING_WHITESPACE=$($item.TrailingWhitespace)"

if ($ComparePath) {
    $other = Read-CiFile -LiteralPath $ComparePath
    $maxLineCount = [Math]::Max($item.Lines.Count, $other.Lines.Count)
    $differentLines = New-Object System.Collections.Generic.List[int]

    for ($index = 0; $index -lt $maxLineCount; $index++) {
        $left = if ($index -lt $item.Lines.Count) { $item.Lines[$index] } else { $null }
        $right = if ($index -lt $other.Lines.Count) { $other.Lines[$index] } else { $null }
        if ($left -cne $right) {
            $differentLines.Add($index + 1)
        }
    }

    Write-Output "COMPARE_PATH=$($other.Path)"
    Write-Output "DIFF_LINES=$($differentLines -join ',')"

    if ($null -ne $ExpectedDiffLine) {
        $actual = @($differentLines | Sort-Object -Unique)
        $expected = @($ExpectedDiffLine | Sort-Object -Unique)
        if (($actual -join ',') -cne ($expected -join ',')) {
            $failures.Add("diff lines '$($actual -join ',')' do not equal expected '$($expected -join ',')'")
        }
    }
}

if ($failures.Count -gt 0) {
    Write-Output 'STRUCTURAL_RESULT=FAIL'
    foreach ($failure in $failures) {
        Write-Output "FAILURE=$failure"
    }
    exit 1
}

Write-Output 'STRUCTURAL_RESULT=PASS'
Write-Output 'RUNTIME_RESULT=NOT_TESTED'
