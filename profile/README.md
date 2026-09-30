<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/madrileno-dev/.github/main/brand/logo-stacked-dark.svg">
    <img alt="madrileño" src="https://raw.githubusercontent.com/madrileno-dev/.github/main/brand/logo-stacked.svg" width="220">
  </picture>
</p>

A Scala 3 backend template, written to be worked on with a coding assistant.

**[madrileno](https://github.com/madrileno-dev/madrileno)** is the project. http4s, Skunk, cats-effect and Postgres, with auth, scheduled jobs, an outbox, feature flags and OpenTelemetry already wired up. It ships a committed `.mcp.json` (Metals plus a docs/source MCP server) and a `docs/` tree that doubles as the assistant's knowledge base. The worked example is a wine auction site; `init-project` strips it and renames the project to yours.

**[madrileno-frontend](https://github.com/madrileno-dev/madrileno-frontend)** is a companion starting point: a small React 19 and TypeScript app (Vite, TanStack Query, shadcn/ui) built against the oRPC contract generated from the backend's routes, so backend drift is a compile error. It covers the app shell, auth and the demo pages.

**[madrileno-mobile](https://github.com/madrileno-dev/madrileno-mobile)** is the same idea for phones: a React Native app (Expo, Expo Router, TanStack Query, NativeWind) on the same generated contract. It adds what a native app needs: deep links, over-the-air updates through EAS and optional OpenObserve monitoring that traces each request into the backend.

Site: [madrileno.dev](https://madrileno.dev/). Docs: [Quick start](https://madrileno.dev/docs/getting-started/), [AI-assisted development](https://madrileno.dev/docs/ai-assisted-dev/), [Architecture](https://madrileno.dev/docs/architecture/). The [manifesto](https://madrileno.dev/manifesto/) is the reasoning behind the choices.

Built and maintained by [Iterators](https://www.iteratorshq.com/), a software consulting company. Paid support and consulting at [madrileno.dev/support](https://madrileno.dev/support/).

Apache-2.0.
