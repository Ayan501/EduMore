import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models.institutions import Institution
from app.db.models.users import User


class UserRepository:
    """Database operations related to users and institutions."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_email_and_institution(
        self,
        email: str,
        institution_id: uuid.UUID,
    ) -> User | None:
        """Find a user by normalized email and institution."""

        statement = select(User).where(
            User.email == email.strip().lower(),
            User.institution_id == institution_id,
        )

        return self.db.scalar(statement)

    def get_institution_by_code(
        self,
        institution_code: str,
    ) -> Institution | None:
        """Find an institution by its code."""

        statement = select(Institution).where(
            Institution.code == institution_code.strip(),
        )

        return self.db.scalar(statement)

    def get_by_id(
        self,
        user_id: uuid.UUID,
        institution_id: uuid.UUID,
    ) -> User | None:
        """Find a user within the specified institution."""

        statement = select(User).where(
            User.id == user_id,
            User.institution_id == institution_id,
        )

        return self.db.scalar(statement)

