"""Small local retriever over the knowledge corpus (markdown, one chunk per '## ' heading).

Pure Python, no vector database. Every chunk keeps a source id so the report can cite it.
"""
import math
import re
from pathlib import Path

_WORD = re.compile(r"[a-z0-9]{3,}")


def _tokens(text: str) -> list:
    return _WORD.findall(text.lower())


def load_chunks(knowledge_dir: str = "knowledge") -> list:
    chunks = []
    for path in sorted(Path(knowledge_dir).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        parts = re.split(r"(?m)^## ", text)
        for i, part in enumerate(parts[1:], start=1):
            title, _, body = part.partition("\n")
            chunks.append({
                "source_id": f"G-{path.stem}#{i}",
                "title": title.strip(),
                "text": body.strip(),
            })
    return chunks


def retrieve(query: str, chunks: list, k: int = 3) -> list:
    if not chunks:
        return []
    docs = [_tokens(c["title"] + " " + c["text"]) for c in chunks]
    df: dict = {}
    for d in docs:
        for t in set(d):
            df[t] = df.get(t, 0) + 1
    n = len(docs)
    q = set(_tokens(query))
    scored = []
    for chunk, d in zip(chunks, docs):
        if not d:
            continue
        score = sum((1 + math.log(d.count(t))) * math.log(1 + n / df[t]) for t in q if t in df and t in d)
        score /= math.sqrt(len(d))
        if score > 0:
            scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [dict(c, score=round(s, 3)) for s, c in scored[:k]]
