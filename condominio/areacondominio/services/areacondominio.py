from abc import ABC, abstractmethod
from typing import List, Optional

class AreaCondominio(ABC):
    def __init__(self, nome: str, descricao: Optional[str] = None):
        self.nome = nome
        self.descricao = descricao

    @abstractmethod
    def reservar(self, usuario_id: int, data: str) -> bool:
        pass

    @abstractmethod
    def cancelar_reserva(self, reserva_id: int) -> bool:
        pass

    @abstractmethod
    def listar_reservas(self) -> List[dict]:
        pass