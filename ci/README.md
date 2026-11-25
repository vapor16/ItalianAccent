# CI workflows (pending activation)

`validate.yml` and `release-check.yml` are the project's GitHub Actions workflows. They are stored here because the
automated session that published v1.0.0 had a GitHub token without the `workflow` scope, and GitHub refuses
pushes that create files under `.github/workflows/` from such tokens.

A maintainer activates them with:

```bash
git mv ci/workflows .github/workflows && git commit -m "ci: activate GitHub Actions workflows" && git push
```

Both workflows use `permissions: contents: read`, need no secrets and never publish releases.
