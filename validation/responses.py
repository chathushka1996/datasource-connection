from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class GeneralResponse(Generic[T]):
    success: bool
    message: Optional[str] = None
    data: Optional[T] = None