# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## PowerShell Commands

- `.\bin\test.ps1`: Run Pester tests to validate all manifests in the bucket
- `.\bin\checkver.ps1`: Check for version updates across all manifests
- `.\bin\checkhashes.ps1`: Validate file hashes in manifests
- `.\bin\formatjson.ps1`: Format JSON manifests consistently
- `.\bin\checkurls.ps1`: Verify URLs in manifests are accessible
- `.\bin\auto-pr.ps1`: Create pull requests for automated updates
- `.\Scoop-Bucket.Tests.ps1`: Main test entry point (imports Scoop bucket tests)

**IMPORTANT**: All scripts automatically detect and set `SCOOP_HOME` environment variable.

### Running PowerShell Scripts

Use `-NoProfile` flag to avoid PowerShell profile loading issues:
```powershell
powershell.exe -NoProfile -Command ".\bin\checkver.ps1 app-name"
powershell.exe -NoProfile -Command ".\bin\checkhashes.ps1 app-name"
powershell.exe -NoProfile -Command ".\bin\formatjson.ps1 app-name"
```

For scripts requiring execution policy bypass:
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\bin\test.ps1"
```

## Repository Context

This is a personal Scoop bucket for Windows package management. Scoop buckets contain JSON manifest files that define how to install, update, and manage Windows applications via the command line.

## Code Structure

- `bucket/`: JSON manifest files, one per application
- `bucket/app-name.json.template`: Template for creating new manifests
- `bin/`: PowerShell utility scripts for bucket maintenance
- `deprecated/`: Deprecated manifests no longer maintained

## Manifest Schema

Each JSON manifest in `bucket/` contains:
- `version`: Current version of the application
- `architecture`: Download URLs and hashes per CPU architecture (64bit, 32bit, arm64)
- `checkver`: Configuration for automatic version checking
- `autoupdate`: Configuration for automatic manifest updates
- `bin`: Executable file(s) to add to PATH

## Development Workflow

1. Copy `bucket/app-name.json.template` and rename for new apps
2. Run `.\bin\test.ps1` after any changes
3. Use `.\bin\formatjson.ps1` to maintain consistent formatting
4. Rely on automated Excavator workflow for version updates

## Important Notes

- **YOU MUST** run `.\bin\test.ps1` before committing any manifest changes
- The README apps table is automatically maintained - do not edit manually
- CI runs on both PowerShell and Windows PowerShell environments
- Excavator workflow runs every 4 hours for automatic updates
- All manifests should support automatic updates via `autoupdate` configuration
