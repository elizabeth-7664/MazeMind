import uuid
from datetime import datetime
from sqlalchemy import  String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class User(Base):
    __tablename__ = "users"


id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
hashed_password: Mapped[str] = mapped_column(String, nullable=False)
is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
role: Mapped[str] = mapped_column(String, default="user")
created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

#one-to-many relationships
blog_posts = relationship("BlogPost", back_populates="author", cascade="all, delete-orphan")
vents = relationship("Vent", back_populates="user", cascade="all, delete-orphan")
accountability_logs = relationship("AccountabilityLog", back_populates="user", cascade="all, delete-orphan")
maze_challenges = relationship("MazeChallenge", back_populates="user", cascade="all, delete-orphan")
vault_entries = relationship("VaultEntry", back_populates="user", cascade="all, delete-orphan")
mind_dumps = relationship("MindDump", back_populates="user", cascade="all, delete-orphan")
pinned_items = relationship("PinnedItem", back_populates="user", cascade="all, delete-orphan")