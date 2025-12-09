import re
from typing import Literal

# Your keyword sets (organized for tiered classification)
SECURITY_KEYWORDS = {
    "cve", "vulnerability", "vulnerabilities", 
    "buffer", "injection", "overflow", "npe", "security"
}
CRASH_KEYWORDS = {"crash"}
BUG_KEYWORDS = {"bug", "error", "issue", "fault", "defect", "fix"}
MAINT_KEYWORDS = {"patch", "resolve", "correct", "repair", "lint"}

# Precompile case-insensitive, word-boundary regex for speed
def _make_pattern(words):
    escaped = [re.escape(w) for w in words]
    return re.compile(r'\b(?:' + '|'.join(escaped) + r')\b', re.IGNORECASE)

SECURITY_PATTERN = _make_pattern(SECURITY_KEYWORDS)
CRASH_PATTERN = _make_pattern(CRASH_KEYWORDS)
BUG_PATTERN = _make_pattern(BUG_KEYWORDS)
MAINT_PATTERN = _make_pattern(MAINT_KEYWORDS)

FixType = Literal["security", "crash", "bug", "maintenance", "other"]

def classify_fix_type(msg: str) -> FixType:
    """Classify commit message into fix category (prioritized)."""
    if not isinstance(msg, str) or not msg.strip():
        return "other"
    
    lower = msg.lower()
    
    # Priority order: security > crash > bug > maintenance
    if SECURITY_PATTERN.search(msg):
        return "security"
    if CRASH_PATTERN.search(msg):
        return "crash"
    if BUG_PATTERN.search(msg):
        return "bug"
    if MAINT_PATTERN.search(msg):
        return "maintenance"
    return "other"

def is_fix_commit(msg: str) -> bool:
    """Binary: is this a fix (any kind)?"""
    return classify_fix_type(msg) != "other"