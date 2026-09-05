# Krishna Puri

<img src="profile-banner.png" alt="Krishna Puri — systems-minded engineer. Two flagships: VoltHub CSMS (two-engine EV charging) and Q-Trust (post-quantum trust protocol). The portrait sits in an indigo ring with one cyan notch: five-sixths earned, one-sixth still to be earned — the ring deliberately never closes." width="100%">

**Systems-minded engineer — I build the deterministic parts (money paths, concurrency, protocols) and the emerging parts (post-quantum cryptography, attestations) with the same discipline: trade-offs named, claims receipted, races proven in CI.**

> Hi — I'm Krishna. The ring around my portrait is five-sixths indigo and one-sixth cyan: five-sixths earned, one-sixth still to be earned. That is the whole philosophy of this profile — every badge below is a live status, not a claim. If a pipeline goes red, the badge goes red with it.

---

## Live receipts

| VoltHub CSMS | Q-Trust |
| --- | --- |
| [![ci](https://github.com/humoge7502/VoltHub-CSMS/actions/workflows/ci.yml/badge.svg)](https://github.com/humoge7502/VoltHub-CSMS/actions/workflows/ci.yml) [![release](https://github.com/humoge7502/VoltHub-CSMS/actions/workflows/release.yml/badge.svg)](https://github.com/humoge7502/VoltHub-CSMS/actions/workflows/release.yml) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/humoge7502/VoltHub-CSMS/badge)](https://scorecard.dev/viewer.html?url=github.com/humoge7502/VoltHub-CSMS) [![docs site](https://img.shields.io/badge/docs-site-c6f24e)](https://humoge7502.github.io/VoltHub-CSMS/) | [![ci](https://github.com/humoge7502/q-trust/actions/workflows/ci.yml/badge.svg)](https://github.com/humoge7502/q-trust/actions/workflows/ci.yml) [![security](https://github.com/humoge7502/q-trust/actions/workflows/security.yml/badge.svg)](https://github.com/humoge7502/q-trust/actions/workflows/security.yml) [![pqc self-scan](https://github.com/humoge7502/q-trust/actions/workflows/pqc-scan.yml/badge.svg)](https://github.com/humoge7502/q-trust/actions/workflows/pqc-scan.yml) [![docs site](https://img.shields.io/badge/docs-mkdocs%20material-00D9FF)](https://humoge7502.github.io/q-trust) |

---

## The flagships

<table>
<tr>
<td width="50%" valign="top">

### ⚡ [VoltHub CSMS](https://github.com/humoge7502/VoltHub-CSMS)

EV charging management where **the race demo is the shortest honest proof of
the architecture**: two parallel bookings hit the same connector — exactly one
`201 BOOKED`, one `409 OVERLAP`. CI fires that race on **every push, on both
database engines**.

- **Oracle 23ai** money path — 25 relations, 7 PL/SQL packages, no DELETE anywhere
- **TimescaleDB** telemetry — hypertables, 1m/1h caggs, compression, retention
- **OCPP 1.6J** gateway + simulator fleet; **outbox + relay** joins the engines
- 48 REST routes with an OpenAPI **drift gate**; 6-job CI; zero known CVEs
- Every claim receipted: [`docs/verification.md`](https://github.com/humoge7502/VoltHub-CSMS/blob/main/docs/verification.md) · [7 ADRs](https://github.com/humoge7502/VoltHub-CSMS/tree/main/docs/adr) with named rejected alternatives

```text
$ simulator --scenario race
POST /api/v1/reservations   201 BOOKED
POST /api/v1/reservations   409 OVERLAP
```

</td>
<td width="50%" valign="top">

### 🔐 [Q-Trust](https://github.com/humoge7502/q-trust)

Post-quantum cryptography migration & attestation protocol: **scan your
cryptographic estate · score it against NIST & CNSA 2.0 · plan migration with a
GNN · seal tamper-proof attestations on Base L2.**

- **CBOM scanning** (CycloneDX) — the "SBOM, but for cryptography"
- **GNN planner** ranks migration order from the crypto graph
- **Solidity attestation registry** on Base L2 (Foundry + **Halmos symbolic** CI)
- Dogfooded: the scanner runs on **its own repo** in CI (`pqc-scan.yml`)
- PyPI + Docker publish pipelines, mkdocs Material docs site

```text
$ qtrust scan --deep --cbom
→ 12 algorithms found · 3 not PQ-ready
→ migration plan: 5 waves (GNN-ranked)
→ attestation sealed on Base L2
```

</td>
</tr>
</table>

## What I actually do

```text
backend & data   Oracle PL/SQL · TimescaleDB · outbox patterns · concurrency & race safety
protocols        OCPP 1.6J (WebSocket gateways, simulator fleets) · REST/OpenAPI contracts
security         post-quantum migration (NIST/CNSA 2.0) · CBOM · attestation design
emerging         GNN planning models · Solidity/Base L2 · Halmos symbolic execution
platform         Node.js 20/22 · Express 5 · Next.js 16 · Python · TypeScript · Docker · GitHub Actions
discipline       conventional commits · ADRs · CI-gated audits · receipts over claims
```

## How I work

- **Trade-offs, not fashion.** Every stack decision names its rejected
  alternative — [ADRs on VoltHub](https://github.com/humoge7502/VoltHub-CSMS/tree/main/docs/adr),
  design-kit notes on Q-Trust.
- **Honest limits.** The READMEs say what each project is _not_: simulated
  chargers, prepaid wallet, single-VM deploy, local-store default path. Trust
  compounds faster than hype.
- **Evidence on every push.** `npm audit`, CodeQL and the PQC self-scan are
  red/green CI gates. If CI can't re-prove a claim, the claim comes off the README.

## Now

- Hardening VoltHub's telemetry path (full-profile benchmarks from `bench/`)
- Studying the OCPP 2.0.1 (IEC 63584) migration path — the store surface is
  already protocol-neutral by design
- Extending Q-Trust's CBOM coverage toward CNSA 2.0 compliance reporting

## Find me

[**LinkedIn**](https://www.linkedin.com/in/krishna-puri-3a9bba432) ·
[**VoltHub CSMS**](https://github.com/humoge7502/VoltHub-CSMS) ·
[**VoltHub docs**](https://humoge7502.github.io/VoltHub-CSMS/) ·
[**Q-Trust**](https://github.com/humoge7502/q-trust) ·
[**Q-Trust docs**](https://humoge7502.github.io/q-trust)

<!-- PROFILE README v2 (photo variant) — changes vs the pack's v2:
1. Banner moved above the positioning line so the portrait is the first thing
   rendered (GitHub social cards and LinkedIn previews take the first image).
2. Added the one-paragraph photo opener: the ring is 5/6 indigo, 1/6 cyan —
   "five-sixths earned, one-sixth still to be earned" ties the portrait to the
   receipts-over-claims positioning. Delete the blockquote if you prefer the
   v1 layout; everything else stands alone.
3. Banner alt text carries the same story (screen readers + social scrapers).
4. "Find me" relinked to the photo-bearing LinkedIn profile.
Nothing else changed from the pack's v2 README. -->
