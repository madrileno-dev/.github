<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/madrileno-dev/.github/main/brand/logo-stacked-dark.svg">
    <img alt="madrileño" src="https://raw.githubusercontent.com/madrileno-dev/.github/main/brand/logo-stacked.svg" width="220">
  </picture>
</p>

Two templates for building a web product in Scala 3 and React, written to be worked on with a coding assistant.

| Repo | What it is |
|---|---|
| [madrileno](https://github.com/madrileno-dev/madrileno) | Scala 3 backend: http4s, Skunk, cats-effect, Postgres. Auth, scheduled jobs, outbox, feature flags, OpenTelemetry. Ships a committed `.mcp.json` (Metals plus a docs/source MCP server) and a `docs/` tree that doubles as the assistant's knowledge base. |
| [madrileno-frontend](https://github.com/madrileno-dev/madrileno-frontend) | React 19 and TypeScript: Vite, TanStack Query, shadcn/ui. Built against an oRPC contract generated from the backend's routes, so backend drift is a compile error. SPA by default, SSR opt-in. |

The worked example in both is a wine auction site. A rename script strips it and gives the project your own name.

Docs: [Quick start](https://github.com/madrileno-dev/madrileno#quick-start), [AI-assisted development](https://github.com/madrileno-dev/madrileno/blob/main/docs/ai-assisted-dev.md), [Architecture](https://github.com/madrileno-dev/madrileno/blob/main/docs/architecture.md).

Apache-2.0.
