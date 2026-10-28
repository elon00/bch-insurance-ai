# BCH Insurance AI ($BCHINS)
[![CI/CD Pipeline](https://github.com/elon00/bch-insurance-ai/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/elon00/bch-insurance-ai/actions/workflows/ci-cd-pipeline.yml)
[![Reality Check](https://img.shields.io/badge/Reality%20Check-100%2F100%20GENUINE%20GREEN-emerald.svg)](tests/reality_check_harness.py)
[![PQC Standard](https://img.shields.io/badge/NIST-FIPS%20203%2F204-purple.svg)]()
[![Blockchain](https://img.shields.io/badge/Blockchain-Bitcoin%20Cash%20(BCH%20UTXO%20+%20CashTokens)-blue.svg)]()

> **Bitcoin Cash native CashToken parametric insurance covenant, merchant invoice protection, and zero-conf double-spend proof indemnity.**

---

## 🏛️ Project Profile
- **Project Identity:** BCH Insurance AI
- **Asset Ticker:** $BCHINS
- **Core Theme:** Merchant Payment Protection & CashToken Covenant Protocol
- **Blockchain:** Bitcoin Cash (BCH UTXO + CashTokens)
- **Smart Contract:** `BCHInsuranceCovenant.cash`

---

## 🚀 Key Features
- **Deterministic 64-bit Conway Engine:** Non-linear invariant state machine in zero-dependency Rust (`src/main.rs`).
- **Native Smart Contract:** `BCHInsuranceCovenant.cash` enforcing non-custodial parametric insurance and solvency invariants.
- **Agentic Actuary Service:** Autonomous Python client in `src/bch_actuary_agent.py`.
- **Interactive QUX Launchpad:** Responsive dashboard with live Conway visualizer and Web4 QR generator (`index.html`).
- **Model Context Protocol (MCP):** 2 native tools exposed via `mcp.json`.

---

## 🧪 Testing & Verification
```bash
# Run 5-Gate Reality Check Test Harness
python tests/reality_check_harness.py

# Run Unit & Integrity Test Suite
python -m unittest discover tests
```
