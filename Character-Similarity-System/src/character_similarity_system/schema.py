from pydantic import BaseModel, ConfigDict, field_serializer

class CreateProfile(BaseModel):

    strength: int
    agility: int
    magic: int
    defense: int
    intelligence: int

class ResponseProfile(CreateProfile):
    
    model_config = ConfigDict(from_attributes=True)
    id: int

class ResponseProfileList(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    lista: list[ResponseProfile]

class ResponseSimilarity(BaseModel):

    similarity: float

    @field_serializer("similarity")
    def serialize_similarity(self, value: float) -> float:
        return round(value, 2)

