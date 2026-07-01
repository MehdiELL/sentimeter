<div align="center">

# 📊 SentiMeter

### AI sentiment analysis on GenLayer

[![GenLayer](https://img.shields.io/badge/GenLayer-Bradbury-ff4d6d)](https://genlayer.com)
[![chainId](https://img.shields.io/badge/chainId-4221-4dd0e1)](https://docs.genlayer.com/developers/networks)
[![Intelligent Contract](https://img.shields.io/badge/intelligent%20contract-Python%20GenVM-8a63d2)](https://docs.genlayer.com/developers/intelligent-contracts/introduction)
[![License](https://img.shields.io/badge/license-MIT-2dd4bf)](#license)

</div>

---

## What is this

Submit a review or message; validators independently classify its sentiment with an LLM and agree on the result by consensus.

**Deployed contract (Testnet Bradbury):** [`0xF095343b5178a9B3b39936f3229e39efd88a9819`](https://explorer-bradbury.genlayer.com/address/0xF095343b5178a9B3b39936f3229e39efd88a9819)

## Why GenLayer

This is a subjective judgment over real-world text input - exactly what a
deterministic VM cannot do. GenLayer runs the LLM evaluation **inside consensus**, so the
result gets the same Byzantine-fault tolerance a normal chain gives to arithmetic.

## How it works

1. **`submit(text)`** - submit text to be evaluated.
2. **`evaluate(id)`** - each validator classifies the content
   (one of: positive, neutral, negative) and scores it 0-100, then must **agree** on the label and a
   similar score via the Equivalence Principle.
3. The **label, score, and reasoning** are written on chain.

## The Intelligent Contract

`contracts/sentimeter.py` targets the GenVM Python runner (pinned by hash):

- **Integers only** - the intensity score is `u8` (0-100); no floats.
- **Coarse-band equivalence** - validators must agree on the label and land within **+/-25**
  score, so heterogeneous LLMs converge instead of returning `Undetermined`.
- **Prompt-injection defense** - the input is treated as untrusted data.
- **Low-RPC reads** - `get_info()` / `list_items()` return state in one call.

Public methods: `submit`, `evaluate`, `get_item`, `list_items`, `get_info`.

## Develop & test

```bash
pip install -r requirements.txt        # Python 3.12+
genvm-lint check contracts/sentimeter.py
pytest tests/direct/ -v
```

## Deploy

```bash
npm install -g genlayer
genlayer network set testnet-bradbury
bash deploy/deploy.sh
```

## Network

| | |
| --- | --- |
| Network | GenLayer Bradbury testnet |
| Chain ID | 4221 |
| RPC | https://rpc-bradbury.genlayer.com |
| Explorer | https://explorer-bradbury.genlayer.com |
| Faucet | https://testnet-faucet.genlayer.foundation |

## License

MIT.
