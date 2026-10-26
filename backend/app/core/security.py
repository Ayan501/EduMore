import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from pwdlib import PasswordHash

from app.core.config import get_settings


settings = get_settings()

password_hash = PasswordHash.recommended()

ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    """Hash a password before storing it."""
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against its stored hash."""
    return password_hash.verify(password, hashed_password)


def create_access_token(
    user_id: uuid.UUID,
    institution_id: uuid.UUID,
    role: str,
) -> str:
    """Create a short-lived JWT access token."""

    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    payload = {
        "sub": str(user_id),
        "institution_id": str(institution_id),
        "role": role,
        "type": "access",
        "iat": now,
        "exp": expires_at,
        "jti": str(uuid.uuid4()),
    }

    return jwt.encode(
        payload,
        settings.access_token_secret,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str) -> dict[str, Any]:
    """Decode and validate an access token."""

    payload = jwt.decode(
        token,
        settings.access_token_secret,
        algorithms=[ALGORITHM],
        options={"require": ["sub", "exp", "iat", "jti", "type"]},
    )

    if payload.get("type") != "access":
        raise jwt.InvalidTokenError("Invalid token type")

    # Reject malformed identifiers before using token claims.
    uuid.UUID(payload["sub"])
    uuid.UUID(payload["institution_id"])

    if not payload.get("role"):
        raise jwt.InvalidTokenError("Missing role")

    return payload
