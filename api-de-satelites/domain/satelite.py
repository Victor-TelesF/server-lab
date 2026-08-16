from .enum_status import Status
from .exceptions import BateriaInsuficienteError, TransicaoInvalidaError, AtributosError

class Satelite:
    def __init__(self, id: int | None, nome: str, nivel_bateria: int):
        self.id = id
        self.nome = nome
        self.status = Status.DESATIVADO
        self.nivel_bateria = nivel_bateria


    @classmethod
    def reconstruir(cls, id: int, nome: str, nivel_bateria: int, status: Status):

        satelite = cls(id, nome, nivel_bateria)
        satelite.status = status
        
        return satelite

    
    @property
    def id(self) -> int | None:
        return self._id

    @id.setter
    def id(self, value: int | None) -> None:
        if isinstance(value, int) or value is None:
            self._id = value
        else:
            raise AtributosError("ID tem que ser None ou int")

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        if not isinstance(value, str):
            raise AtributosError("nome tem que ser do tipo str")

        self._nome = value

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        if not isinstance(value, Status):
            raise AtributosError("status tem que ser do tipo Status")

        self._status = value

    @property
    def nivel_bateria(self) -> int:
        return self._nivel_bateria

    
    @nivel_bateria.setter
    def nivel_bateria(self, value: int) -> None:
        if not isinstance(value, int):
            raise AtributosError("nivel da bateria tem que ser do tipo int")

        if value < 0 or value > 100:
            raise AtributosError("nivel da bateria não pode ser menor que 0 ou maior que 100")

        self._nivel_bateria = value
        


    def ativar_satelite(self) -> None:

        if self.nivel_bateria < 20:
            raise BateriaInsuficienteError(f"Não é possivel ativar um satélite com a bateria abaixo de 20%, bateria atual: {self.nivel_bateria}%")

        else:
            self.status = Status.EM_ORBITA

    def desativar_satelite(self) -> None:
        self.status = Status.DESATIVADO

    def entrar_manutencao(self) -> None:

        if self.nivel_bateria == 0:
            raise TransicaoInvalidaError("Não é possivel um satélite com bateria vazia entrar em manuntenção")

        self.status = Status.MANUTENCAO