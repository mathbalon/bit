# Custom Skills

This directory contains custom skills for this Claude Code project.

## Structure

Each skill should be organized as:

```
skills/
├── skill-name/
│   ├── manifest.json
│   ├── prompt.md
│   └── [optional additional files]
└── manifest.json (root manifest)
```

## Creating a Skill

1. Create a folder for your skill: `skills/my-skill/`
2. Add a `manifest.json` with skill metadata
3. Add a `prompt.md` with the skill's behavior/instructions
4. Register in the root `manifest.json`

## Example Manifest Structure

```json
{
  "name": "my-skill",
  "description": "What this skill does",
  "version": "1.0",
  "commands": ["skill-command"],
  "prompt": "prompt.md"
}
```
