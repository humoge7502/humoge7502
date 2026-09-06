# Krishna Puri

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-console.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-console-light.svg" />
  <img src="assets/hero-console.svg" width="100%" alt="Operator console for Krishna Puri, systems engineer. Status online. Left panel: operator license with photo slot and an XP bar with five of six segments earned, the last deliberately open. Right panel: terminal with the working rule — trade-offs named, claims receipted, CI re-proves — and a status grid: VoltHub CI six jobs on both engines, Q-Trust CI eleven workflows, security audit and CodeQL gated, two docs sites, ten tagged releases, zero known CVEs." />
</picture>

**Systems engineer. I build the deterministic parts — money paths, concurrency, protocols — and the emerging parts — post-quantum crypto, attestations — with the same discipline: trade-offs named, claims receipted, races proven in CI.**

> Every badge on this console is a **live status**, not a claim. If a pipeline goes red, the badge goes red with it. The XP bar above is five-sixths earned and one-sixth open — deliberately. That slot closes the day the next real thing ships.

---

## `//00` LIVE TELEMETRY

<img src="assets/strip-live-telemetry.svg" width="100%" alt="Section: live telemetry — CI status" />

| [**VOLTHUB CSMS**](https://github.com/humoge7502/VoltHub-CSMS) — two-engine EV charging | [**Q-TRUST**](https://github.com/humoge7502/q-trust) — post-quantum migration & attestation |
| :--- | :--- |
| [![CI](https://img.shields.io/github/actions/workflow/status/humoge7502/VoltHub-CSMS/ci.yml?style=flat-square&label=CI&logo=github&color=22D3EE)](https://github.com/humoge7502/VoltHub-CSMS/actions/workflows/ci.yml) [![RELEASE](https://img.shields.io/github/v/release/humoge7502/VoltHub-CSMS?style=flat-square&label=RELEASE&logo=semver&color=22D3EE)](https://github.com/humoge7502/VoltHub-CSMS/releases) [![SECURITY](https://img.shields.io/github/actions/workflow/status/humoge7502/VoltHub-CSMS/security.yml?style=flat-square&label=SECURITY&logo=githubactions&color=22D3EE)](https://github.com/humoge7502/VoltHub-CSMS/actions/workflows/security.yml) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/humoge7502/VoltHub-CSMS/badge)](https://scorecard.dev/viewer.html?url=github.com/humoge7502/VoltHub-CSMS) | [![CI](https://img.shields.io/github/actions/workflow/status/humoge7502/q-trust/ci.yml?style=flat-square&label=CI&logo=github&color=A78BFA)](https://github.com/humoge7502/q-trust/actions/workflows/ci.yml) [![SECURITY](https://img.shields.io/github/actions/workflow/status/humoge7502/q-trust/security.yml?style=flat-square&label=SECURITY&logo=githubactions&color=A78BFA)](https://github.com/humoge7502/q-trust/actions/workflows/security.yml) [![PQC SELF-SCAN](https://img.shields.io/github/actions/workflow/status/humoge7502/q-trust/pqc-scan.yml?style=flat-square&label=PQC%20SELF-SCAN&color=A78BFA)](https://github.com/humoge7502/q-trust/actions/workflows/pqc-scan.yml) [![RELEASE](https://img.shields.io/github/v/release/humoge7502/q-trust?style=flat-square&label=RELEASE&logo=semver&color=A78BFA)](https://github.com/humoge7502/q-trust/releases) |
| [![docs](https://img.shields.io/badge/docs-site-22D3EE?style=flat-square&logo=readthedocs&logoColor=white)](https://humoge7502.github.io/VoltHub-CSMS/) [![coverage](https://codecov.io/gh/humoge7502/VoltHub-CSMS/graph/badge.svg)](https://codecov.io/gh/humoge7502/VoltHub-CSMS) | [![docs](https://img.shields.io/badge/docs-mkdocs%20material-A78BFA?style=flat-square&logo=readthedocs&logoColor=white)](https://humoge7502.github.io/q-trust) [![pypi](https://img.shields.io/github/actions/workflow/status/humoge7502/q-trust/publish-pypi.yml?style=flat-square&label=PYPI&logo=pypi&logoColor=white&color=A78BFA)](https://github.com/humoge7502/q-trust/actions/workflows/publish-pypi.yml) |

---

## `//01` MISSIONS

<img src="assets/strip-missions.svg" width="100%" alt="Section: missions — flagship systems" />

### MISSION 01 — VOLT HUB CSMS

<a href="https://github.com/humoge7502/VoltHub-CSMS">
  <img src="assets/mission-volthub.svg" width="100%" alt="Mission 01: VoltHub CSMS — two-engine EV charging — Oracle money path + TimescaleDB telemetry + OCPP 1.6J. Status ACTIVE, patch v1.4.0." />
</a>

**Objective — an EV charging platform where the money path is race-safe by construction.** Two databases behind one store port: **Oracle 23ai** owns billing, reservations and the ledger (25 relations, 7 PL/SQL packages, no `DELETE` privilege anywhere); **TimescaleDB** owns telemetry (hypertables, continuous aggregates, compression, retention). An **OCPP 1.6J** gateway with a simulator fleet drives both, and an **outbox + relay** joins the engines with effectively-once delivery.

| Field | Value |
| :--- | :--- |
| Threat model | two bookings, one connector — exactly one may win |
| Proof | parallel double-reserve + double-pay fired in CI on **every push, both engines** |
| Contract | 49 OpenAPI paths / 53 routes behind an OpenAPI **drift gate** |
| Decisions | 7 ADRs, each naming its rejected alternative · [`docs/verification.md`](https://github.com/humoge7502/VoltHub-CSMS/blob/main/docs/verification.md) receipts every claim |
| Deploys | tag-driven GitHub Releases from a Keep-a-Changelog `CHANGELOG.md` · `v1.1.0 → v1.4.0` |

```text
$ simulator --scenario race
POST /api/v1/reservations   201 BOOKED
POST /api/v1/reservations   409 OVERLAP
```

> [Repo](https://github.com/humoge7502/VoltHub-CSMS) · [Docs site](https://humoge7502.github.io/VoltHub-CSMS/) · [Race suite](https://github.com/humoge7502/VoltHub-CSMS/blob/main/apps/api/test/race.js) · [ADR index](https://github.com/humoge7502/VoltHub-CSMS/tree/main/docs/adr)

### MISSION 02 — Q-TRUST

<a href="https://github.com/humoge7502/q-trust">
  <img src="assets/mission-qtrust.svg" width="100%" alt="Mission 02: Q-Trust — post-quantum migration and attestation protocol. Status ACTIVE, patch v2.2.1." />
</a>

**Objective — make a cryptographic estate post-quantum before the deadlines make it someone else's incident.** Scan the estate into a **CBOM** (CycloneDX — "SBOM, but for cryptography"), score it against **NIST & CNSA 2.0**, rank migration waves with a **GNN**, and seal tamper-proof attestations on **Base L2**.

| Field | Value |
| :--- | :--- |
| On-chain | 11 UUPS registries · EIP-712 gasless · 7-day timelock (Foundry) |
| Formal layer | **Halmos symbolic execution** runs in CI on every push |
| Dogfooding | the PQC scanner scans **its own repo** in CI (`pqc-scan.yml`) |
| Contracts | 213 tests — unit · invariant · fuzz · attack |
| Coverage | 7 compliance frameworks — NIST · CNSA 2.0 · FIPS · NIS2 · FISMA · FedRAMP · CMMC |

```text
$ qtrust scan --deep --cbom
→ 12 algorithms found · 3 not PQ-ready
→ migration plan: 5 waves (GNN-ranked)
→ attestation sealed on Base L2
```

> [Repo](https://github.com/humoge7502/q-trust) · [Docs site](https://humoge7502.github.io/q-trust) · [Showcase](https://humoge7502.github.io/q-trust/showcase/) · [Halmos workflow](https://github.com/humoge7502/q-trust/actions/workflows/halmos.yml)

---

## `//02` LOADOUT

<img src="assets/strip-loadout.svg" width="100%" alt="Section: loadout — the stack, and why" />

```text
primary    backend & data   Oracle PL/SQL · TimescaleDB · outbox patterns · race-safe concurrency
secondary  protocols        OCPP 1.6J (WebSocket gateways · simulator fleets) · REST/OpenAPI drift gates
utility    security         post-quantum migration (NIST IR 8547 · CNSA 2.0) · CBOM · attestation design
exotic     emerging         GNN planning · Solidity / Base L2 · Halmos symbolic execution
carrier    platform         Node 20/22 · Express 5 · Next.js 16 · Python · TypeScript · Docker · Actions
modifiers  discipline       conventional commits · ADRs · CI-gated audits · receipts over claims
```

**How I work**

- **Trade-offs, not fashion.** Every stack decision names its rejected alternative — [ADRs on VoltHub](https://github.com/humoge7502/VoltHub-CSMS/tree/main/docs/adr), design-kit notes on Q-Trust.
- **Honest limits.** The READMEs say what each system is *not*: simulated chargers, prepaid wallet, single-VM deploy. Trust compounds faster than hype.
- **Evidence on every push.** `npm audit`, CodeQL and the PQC self-scan are red/green CI gates. If CI can't re-prove a claim, the claim comes off the README.

---

## `//03` ACHIEVEMENTS

<img src="assets/strip-achievements.svg" width="100%" alt="Section: achievements — verified unlocks" />

<a href="#missions">
  <img src="assets/achievements-strip.svg" width="100%" alt="Achievements unlocked: FIRST CONTACT; FORMAL PROOF; SELF-TARGET; RACE PROVEN; ZERO CVE — all verifiable from repository history." />
</a>

Every unlock is checkable from repository history. No vanity badges:

- **FIRST CONTACT** — [q-trust was forked](https://github.com/humoge7502/q-trust/forks) by an external developer (2026-08-30). First outside signal that the work is useful.
- **FORMAL PROOF** — [Halmos symbolic execution](https://github.com/humoge7502/q-trust/actions/workflows/halmos.yml) runs against the attestation contracts in CI.
- **SELF-TARGET** — [the PQC scanner scans its own repo](https://github.com/humoge7502/q-trust/actions/workflows/pqc-scan.yml). The tooling survives pointing at itself.
- **RACE PROVEN** — [the race suite](https://github.com/humoge7502/VoltHub-CSMS/blob/main/apps/api/test/race.js) proves exactly-one-winner on two database engines, every push.
- **ZERO CVE** — `npm audit` [fails CI](https://github.com/humoge7502/VoltHub-CSMS/actions/workflows/ci.yml) on either lockfile; zero known CVEs at current release.

---

## `//04` DATALOG

<img src="assets/strip-datalog.svg" width="100%" alt="Section: datalog — current focus" />

- Hardening VoltHub's telemetry path — full-profile benchmarks from `bench/`
- Studying the **OCPP 2.0.1 (IEC 63584)** migration path — the store surface is protocol-neutral by design
- Extending Q-Trust's CBOM coverage toward **CNSA 2.0** compliance reporting

<details>
<summary><b>MISSION LOG</b> — honest deferrals & what shipped</summary>

**shipped**

- `v1.4.0` — httpOnly refresh cookie, family-wide logout, CORS allow-list (SEC-012, regression-gated)
- 0 known CVEs across both lockfiles, held by a CI audit gate
- BUG-021 stale-socket race fixed with a regression test **validated to catch the bug**

**deferred by design**

- `oracledb 7` — held until db-backed CI validates it (drivers are not blind-bumped)
- Full-profile benchmarks — blocked by disk space on the dev box; local-profile numbers are re-measured instead

</details>

---

## `//05` ACTIVITY

<img src="assets/strip-activity.svg" width="100%" alt="Section: activity — contribution grid" />

The grid is a game — the snake replays it daily:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/humoge7502/humoge7502/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/humoge7502/humoge7502/output/github-contribution-grid-snake.svg" />
  <img src="https://raw.githubusercontent.com/humoge7502/humoge7502/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Contribution grid snake — an animated snake eats through the daily contribution cells; regenerated daily by the Generate Snake workflow." />
</picture>

**Recent transmissions** — rebuilt daily from the public events API, no third-party services:

<!-- START:ACTIVITY -->
- 🗑️ delete in **q-trust**
- 💬 issue comment in **q-trust**
- 💬 issue comment in **q-trust**
- 🗑️ delete in **q-trust**
- 💬 issue comment in **q-trust**
<!-- END:ACTIVITY -->

---

## `//06` COMMS

<img src="assets/strip-comms.svg" width="100%" alt="Section: comms — open channel" />

[**LinkedIn**](https://www.linkedin.com/in/krishna-puri-3a9bba432) · [**VoltHub CSMS**](https://github.com/humoge7502/VoltHub-CSMS) · [**VoltHub docs**](https://humoge7502.github.io/VoltHub-CSMS/) · [**Q-Trust**](https://github.com/humoge7502/q-trust) · [**Q-Trust docs**](https://humoge7502.github.io/q-trust) · [**email**](mailto:orayan1267@gmail.com)

<sub>save file: `krishna-2026` · engines online: **2/2** · status: **buildable, tested, honest** — every badge on this console is a live pipeline.</sub>

---

<details>
<summary><b>⌘ CHEAT CODES</b> <em>(nothing here affects your stats)</em></summary>

```text
↑ ↑ ↓ ↓ ← → ← → B A
```

Nothing happens — GitHub sanitizes JavaScript, and this console doesn't need cheats anyway.
Switch your GitHub theme between dark and light: the hero re-renders in both.

```text
MISSION PASSED · RESPECT +
┌─────────────────────────────────────┐
│  you read the whole profile.        │
│  that's rarer than you think.       │
│  the interesting evidence is in the │
│  repos — go run the race suite.     │
└─────────────────────────────────────┘
```

</details>

<!-- K/OS Operator Console — profile README v3 (game-HUD edition).
     Design + assets: tools/build_assets.py (regenerates everything in assets/).
     To bake a real portrait into the hero: drop photo.jpg next to this file
     and run `python3 tools/build_assets.py --photo photo.jpg`, then commit
     both regenerated hero SVGs.
     Preserve the START:ACTIVITY / END:ACTIVITY markers — the
     update-activity.yml workflow rewrites only the block between them. -->