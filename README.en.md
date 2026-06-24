# Open Construction Skills ES

Open skills in Spanish for AI agents working on concrete construction tasks.

The repository is intentionally narrow at this stage. The current canonical skill is `cronograma-preliminar-obra`.

The current approach is:

- keep `skills/` as the canonical source;
- require only `SKILL.md` as the minimum contract;
- avoid extra folders unless they clearly improve usage or maintenance;
- document one well-resolved skill before expanding the catalog.

Current reference skill:

- `cronograma-preliminar-obra`: creates a preliminary construction schedule in Spanish from a scope narrative, descriptive memo, quantity takeoff, budget, or partial project information.

The other skill folders currently present in the repository are under review and should not be treated as the active editorial standard.

Validation:

```bash
python3 scripts/validate_repo.py
```

This repository does not include proprietary pricing data, scraping, vendor recommendations, or private datasets.

License: MIT.
