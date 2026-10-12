# Chroma Vector DB Practice

Small scripts to learn **ChromaDB**: collections, metadata, filtered query, update/delete, and optional **multimodal** (image) search with OpenCLIP.

## Files

| File | Purpose |
|------|---------|
| `basic_chroma.py` | CRUD-style ops: `add`, `update`, `get`, `query` with `where_document`, `delete` |
| `multimodal_chrome.py` | Image collection with `OpenCLIPEmbeddingFunction` + text-to-image query |

## Setup

```bash
cd chroma-vector-practice
pip install -r requirements.txt
```

For multimodal script, Chroma will download embedding dependencies on first run. Run from this folder so `./images/` paths resolve.

## Run

```bash
python basic_chroma.py
python multimodal_chrome.py
```

Local `chromadb/` and `chromadb_multimodal/` folders are created at runtime and are gitignored.

## Interview talking points

- Vector DB stores **documents + optional metadata + embeddings** (built-in or custom).
- `query_texts` for semantic search; metadata / `where_document` for filtering.
- Multimodal: same API pattern with `uris` and image embedding functions.
