from fastapi import APIRouter, Depends, HTTPException

from .schema import CreateProfile, ResponseSimilarity, ResponseProfile, ResponseProfileList

from domain.character_profile import CharacterProfile
from domain.similarity_engine import SimilarityEngine

from .database import SessionDep

from .model import ProfileModel



router = APIRouter(prefix="/similaridades")

@router.post("/criar-personagem", response_model=int)
def criar_personagem(profile: CreateProfile, db: SessionDep):
    dados = ProfileModel(**profile.model_dump())
    db.add(dados)
    db.commit()
    db.refresh(dados)
    return dados.id


@router.get("/lista-profile", response_model=ResponseProfileList)
def lista_profile(db: SessionDep):
    dados = db.query(ProfileModel).all()
    return ResponseProfileList(lista=dados)




@router.get("/mais-similar/{id}", response_model=ResponseProfile)
def mais_similar(id: int, db: SessionDep):
    reference = db.get(ProfileModel, id)
    if reference is None:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")

    candidates = db.query(ProfileModel).filter(ProfileModel.id != id).all()
    if not candidates:
        raise HTTPException(status_code=404, detail="Não há outro perfil para comparar")

    def to_domain(row: ProfileModel) -> CharacterProfile:
        data = ResponseProfile.model_validate(row).model_dump(exclude={"id"})
        return CharacterProfile(**data)

    domain_candidates = [to_domain(row) for row in candidates]
    winner = SimilarityEngine(domain_candidates).most_similar(to_domain(reference))
    winner_index = next(
        i for i, profile in enumerate(domain_candidates)
        if profile is winner
    )
    return candidates[winner_index]


